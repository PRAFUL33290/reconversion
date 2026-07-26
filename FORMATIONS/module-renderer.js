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
        ${modules.map(({ number, name: label, file, tagline }) => `
        <li class="module-current">
            <a href="${file}"${number === currentModule ? ' aria-current="page"' : ""}>
                <span class="module-number">${number}</span>
                <span><strong>${label}</strong><small>${tagline}</small></span>
                <span class="module-status">${number === currentModule ? "Module actuel" : "Ouvrir"}</span>
            </a>
        </li>`).join("")}`).join("");

    const mobileItems = moduleCatalog.map(({ number, name, file, tagline }) => `
        <li><a href="${file}"${number === currentModule ? ' aria-current="page"' : ""}>
            <span>${number}</span>
            <span><strong>${name}</strong><small>${tagline}</small></span>
        </a></li>`).join("");

    return `<header class="glass-header">
        <a class="logo project-logo" href="../index.html" aria-label="Retour à l’accueil">Reconversion<span>Pro.</span></a>
        <nav aria-label="Navigation principale">
            <ul class="nav-list">
                <li><a href="../index.html#projet">Le projet</a></li>
                <li><a href="../index.html#axes">Les 5 axes</a></li>
                <li><a href="../index.html#document">La synthèse</a></li>
                <li class="learning-menu"><details><summary class="btn-primary">Les technologies <span class="menu-chevron" aria-hidden="true">⌄</span></summary>
                    <div class="learning-dropdown">
                        <div class="learning-dropdown-head"><div><span class="learning-overline">Parcours d’apprentissage</span><p>Chaque technologie, expliquée simplement</p></div><span class="progress-count">${moduleCatalog.length} modules</span></div>
                        <ol>${items}</ol>
                        <a class="learning-overview" href="../index.html#formation">Voir le parcours complet <span aria-hidden="true">→</span></a>
                    </div>
                </details></li>
            </ul>
        </nav>
        <details class="mobile-menu"><summary>Technologies <span aria-hidden="true">⌄</span></summary>
            <div class="mobile-menu-panel"><nav aria-label="Navigation mobile"><a href="../index.html#projet">Le projet</a><a href="../index.html#axes">Les 5 axes</a><a href="../index.html#formation">Le parcours</a></nav>
                <p>Les technologies du parcours</p><ol>${mobileItems}</ol>
            </div>
        </details>
    </header>`;
}

async function loadModule() {
    document.body.insertAdjacentHTML("afterbegin", headerMarkup());
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
