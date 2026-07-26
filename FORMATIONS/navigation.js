const formationModules = window.FORMATION_MODULES || [];

/* Le menu est partagé par trois emplacements : la racine, /FORMATIONS/ et
   /LANGAGES/. Le préfixe des liens s'adapte au dossier courant. */
const path = window.location.pathname;
const formationPrefix = path.includes("/FORMATIONS/") ? ""
    : path.includes("/LANGAGES/") ? "../FORMATIONS/"
    : "FORMATIONS/";
const currentFile = window.location.pathname.split("/").pop();

/* Les modules sont affichés par famille (« Le site visible », « Les coulisses »,
   « Le CMS municipal ») pour que le menu explique le parcours au lieu de se
   contenter de le lister. */
function groupedModules(modules) {
    const groups = [];
    modules.forEach((module) => {
        const last = groups[groups.length - 1];
        if (last && last.name === module.group) last.items.push(module);
        else groups.push({ name: module.group, items: [module] });
    });
    return groups;
}

function dropdownMarkup(modules) {
    return groupedModules(modules).map(({ name, items }) => `
        <li class="menu-group"><span>${name}</span></li>
        ${items.map(({ number, name: label, file, tagline }) => `
        <li class="module-current">
            <a href="${formationPrefix}${file}"${file === currentFile ? ' aria-current="page"' : ""}>
                <span class="module-number">${number}</span>
                <span><strong>${label}</strong><small>${tagline}</small></span>
                <span class="module-status">${file === currentFile ? "Module actuel" : "Ouvrir"}</span>
            </a>
        </li>`).join("")}`).join("");
}

document.querySelectorAll(".learning-dropdown ol").forEach((list) => {
    list.innerHTML = dropdownMarkup(formationModules);
});

document.querySelectorAll(".mobile-menu-panel ol").forEach((list) => {
    list.innerHTML = formationModules.map(({ number, name, file, tagline }) => `
        <li><a href="${formationPrefix}${file}"${file === currentFile ? ' aria-current="page"' : ""}>
            <span>${number}</span>
            <span><strong>${name}</strong><small>${tagline}</small></span>
        </a></li>`).join("");
});

document.querySelectorAll(".progress-count").forEach((label) => {
    label.textContent = `${formationModules.length} modules`;
});

document.querySelectorAll(".progress-track").forEach((track) => {
    track.setAttribute("aria-label", `${formationModules.length} modules disponibles`);
    const bar = track.querySelector("span");
    if (bar) bar.style.width = "100%";
});
