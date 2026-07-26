const moduleCatalog = window.FORMATION_MODULES || [];

const currentModule = document.body.dataset.moduleNumber;
const sourceFile = document.body.dataset.source;
const moduleTitle = document.body.dataset.title;
const moduleSubtitle = document.body.dataset.subtitle;

function escapeHtml(value) {
    return value.replace(/[&<>"']/g, (character) => ({
        "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;"
    })[character]);
}

function inlineMarkdown(value) {
    return escapeHtml(value)
        .replace(/`([^`]+)`/g, "<code>$1</code>")
        .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
        .replace(/\*([^*]+)\*/g, "<em>$1</em>");
}

function slugify(value) {
    return value.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
        .toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}

function renderMarkdown(markdown) {
    const lines = markdown.replace(/\r/g, "").split("\n");
    const output = [];
    const nav = [];
    let paragraph = [];
    let listType = "";
    let inCode = false;
    let codeLines = [];

    const flushParagraph = () => {
        if (paragraph.length) {
            output.push(`<p>${inlineMarkdown(paragraph.join(" "))}</p>`);
            paragraph = [];
        }
    };
    const closeList = () => {
        if (listType) {
            output.push(`</${listType}>`);
            listType = "";
        }
    };

    lines.forEach((line) => {
        if (line.startsWith("```")) {
            flushParagraph();
            closeList();
            if (inCode) {
                output.push(`<div class="code-block"><div class="code-toolbar"><span>Code</span></div><pre><code>${escapeHtml(codeLines.join("\n"))}</code></pre></div>`);
                codeLines = [];
            }
            inCode = !inCode;
            return;
        }
        if (inCode) {
            codeLines.push(line);
            return;
        }

        const heading = line.match(/^(#{1,3})\s+(.+)$/);
        if (heading) {
            flushParagraph();
            closeList();
            const level = heading[1].length === 1 ? 2 : Math.min(4, heading[1].length + 1);
            const cleanTitle = heading[2].replace(/^[^\p{L}\p{N}]+/u, "").replace(/---/g, "—");
            const id = slugify(cleanTitle);
            output.push(`<h${level} id="${id}">${inlineMarkdown(cleanTitle)}</h${level}>`);
            if (level === 3) nav.push([id, cleanTitle]);
            return;
        }

        const unordered = line.match(/^\s*[-*]\s+(.+)$/);
        const ordered = line.match(/^\s*\d+[.)]\s+(.+)$/);
        if (unordered || ordered) {
            flushParagraph();
            const nextType = ordered ? "ol" : "ul";
            if (listType !== nextType) {
                closeList();
                listType = nextType;
                output.push(`<${listType}>`);
            }
            output.push(`<li>${inlineMarkdown((unordered || ordered)[1])}</li>`);
            return;
        }

        if (!line.trim()) {
            flushParagraph();
            closeList();
        } else {
            paragraph.push(line.trim());
        }
    });
    flushParagraph();
    closeList();
    return { html: output.join("\n"), nav };
}

/* Même regroupement par famille que navigation.js : le menu explique le
   parcours (site visible / coulisses / CMS) au lieu de le lister à plat. */
function groupedCatalog() {
    const groups = [];
    moduleCatalog.forEach((module) => {
        const last = groups[groups.length - 1];
        if (last && last.name === module.group) last.items.push(module);
        else groups.push({ name: module.group, items: [module] });
    });
    return groups;
}

function headerMarkup() {
    const items = groupedCatalog().map(({ name, items: modules }) => `
        <li class="menu-group"><span>${name}</span></li>
        ${modules.map(({ number, name: label, file }) => `
        <li>
            <a href="${file}"${number === currentModule ? ' aria-current="page"' : ""}>
                <span class="module-number">${number}</span>
                ${label}
            </a>
        </li>`).join("")}`).join("");

    const mobileItems = moduleCatalog.map(({ number, name, file, tagline }) => `
        <li><a href="${file}"${number === currentModule ? ' aria-current="page"' : ""}>
            <span>${number}</span>
            <span><strong>${name}</strong><small>${tagline}</small></span>
        </a></li>`).join("");

    return `<header class="glass-header">
        <a class="logo project-logo" href="../index.html" aria-label="Retour à l’accueil">
            <img src="../ASSETS/LOGO T.png" alt="Reconversion Pro" class="logo-image">
        </a>
        <nav aria-label="Navigation principale">
            <ul class="nav-list">
                <li>
                    <a href="../index.html" title="Accueil — tableau de bord du projet">
                        <svg class="nav-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 10.5 12 4l8 6.5V19a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 19z"/><path d="M9.5 20.5v-6h5v6"/></svg>
                        Accueil
                    </a>
                </li>
                <li class="nav-dropdown axes-menu">
                    <span class="nav-link-summary" tabindex="0">
                        <svg class="nav-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="2.6"/><ellipse cx="12" cy="12" rx="9" ry="4" transform="rotate(30 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="4" transform="rotate(-30 12 12)"/></svg>
                        Les 5 axes
                        <svg class="menu-chevron" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 8.5 12 15l7-6.5"/></svg>
                    </span>
                    <ul class="dropdown-panel">
                        <li><a href="../AXES/objectif.html"><svg class="nav-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r=".6" fill="currentColor" stroke="none"/></svg>Objectif</a></li>
                        <li><a href="../AXES/competences-actuelles.html"><svg class="nav-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7.5h9"/><path d="M4 12h13"/><path d="M4 16.5h7"/><path d="M17.5 16.5l2 2 3-3.5"/></svg>Compétences</a></li>
                        <li><a href="../AXES/besoins-marches.html"><svg class="nav-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19V5"/><path d="M4 19h16"/><path d="M7.5 15.5l3.5-4 3 2.5 4.5-6"/></svg>Marché</a></li>
                        <li><a href="../AXES/competences-a-renforcer.html"><svg class="nav-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5v12"/><path d="M8 7.5 12 3.5l4 4"/><path d="M5 20.5h14"/><path d="M5 20.5v-3"/><path d="M19 20.5v-6"/></svg>Renforcer</a></li>
                        <li><a href="../AXES/atomisation.html"><svg class="nav-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="2.6"/><ellipse cx="12" cy="12" rx="9" ry="4" transform="rotate(30 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="4" transform="rotate(-30 12 12)"/></svg>Atomisation</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
        <div class="header-cta nav-dropdown formation-menu">
            <span class="btn-primary btn-icon" tabindex="0">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 2 8l10 5 8-4.2V15h2V8Z"/><path d="M6 11.5V16c0 1.4 2.7 3 6 3s6-1.6 6-3v-4.5"/></svg>
                FORMATION
                <svg class="menu-chevron" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 8.5 12 15l7-6.5"/></svg>
            </span>
            <div class="dropdown-panel formation-dropdown">
                <ul class="formation-panel">${items}</ul>
                <div class="dropdown-footer">
                    <a href="../LANGAGES/index.html">Les langages expliqués simplement <span aria-hidden="true">→</span></a>
                    <a href="../index.html#formation">Voir le parcours de formation <span aria-hidden="true">→</span></a>
                </div>
            </div>
        </div>
        <details class="mobile-menu"><summary>Technologies <span aria-hidden="true">⌄</span></summary>
            <div class="mobile-menu-panel"><div class="mobile-menu-brand"><img src="../ASSETS/LOGO T.png" alt="Reconversion Pro" class="logo-image"></div><nav aria-label="Navigation mobile"><a href="../index.html">Accueil</a><a href="../AXES/objectif.html">Les 5 axes</a><a href="../index.html#formation">Le parcours</a></nav>
                <p>Les technologies du parcours</p><ol>${mobileItems}</ol>
            </div>
        </details>
    </header>`;
}

/* Le volet mobile se referme au clic sur un lien ou en dehors de son
   panneau (clic sur le fond assombri). */
function wireMobileMenu() {
    document.querySelectorAll(".mobile-menu").forEach((menu) => {
        menu.querySelectorAll(".mobile-menu-panel a").forEach((link) => {
            link.addEventListener("click", () => { menu.open = false; });
        });
    });
    document.addEventListener("click", (event) => {
        document.querySelectorAll(".mobile-menu[open]").forEach((menu) => {
            if (!menu.contains(event.target)) menu.open = false;
            else if (event.target.closest("summary") === null && event.target.closest(".mobile-menu-panel") === null) {
                menu.open = false;
            }
        });
    });
}

async function loadModule() {
    document.body.insertAdjacentHTML("afterbegin", headerMarkup());
    wireMobileMenu();
    const response = await fetch(sourceFile);
    if (!response.ok) throw new Error("Le contenu du module est indisponible.");
    const markdown = await response.text();
    const rendered = renderMarkdown(markdown);
    const course = document.querySelector("#course-content");
    course.innerHTML = rendered.html;
    document.querySelector("#course-nav").innerHTML = rendered.nav
        .map(([id, title], index) => `<li><a href="#${id}"><span>${String(index + 1).padStart(2, "0")}</span>${escapeHtml(title)}</a></li>`).join("");
    document.querySelector("#module-title").textContent = moduleTitle;
    document.querySelector("#module-subtitle").textContent = moduleSubtitle;
    document.querySelector("#module-number").textContent = `Module ${currentModule}`;
    document.title = `Module ${currentModule} — ${moduleTitle} | Reconversion Pro`;
}

loadModule().catch((error) => {
    document.querySelector("#course-content").innerHTML = `<div class="callout"><span>!</span><div><strong>Erreur de chargement</strong><p>${escapeHtml(error.message)}</p></div></div>`;
});
