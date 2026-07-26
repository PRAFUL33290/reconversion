const progressItems = [...document.querySelectorAll("[data-progress-item]")];
const completionBar = document.querySelector("#completion-bar");
const completionLabel = document.querySelector("#completion-label");
const readingBar = document.querySelector("#reading-progress-bar");
const copyButtons = document.querySelectorAll("[data-copy-code]");
const navLinks = [...document.querySelectorAll(".course-nav a")];

function updateCompletion() {
    const completed = progressItems.filter((item) => item.checked).length;
    const percentage = progressItems.length
        ? Math.round((completed / progressItems.length) * 100)
        : 0;

    completionBar.style.width = `${percentage}%`;
    completionLabel.textContent = `${percentage} %`;

    const state = progressItems.map((item) => item.checked);
    const moduleName = document.body.dataset.module || "course";
    localStorage.setItem(`${moduleName}-progress`, JSON.stringify(state));
}

function restoreCompletion() {
    try {
        const moduleName = document.body.dataset.module || "course";
        const state = JSON.parse(localStorage.getItem(`${moduleName}-progress`));
        if (Array.isArray(state)) {
            progressItems.forEach((item, index) => {
                item.checked = Boolean(state[index]);
            });
        }
    } catch {
        const moduleName = document.body.dataset.module || "course";
        localStorage.removeItem(`${moduleName}-progress`);
    }
    updateCompletion();
}

function updateReadingProgress() {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const percentage = scrollable > 0 ? (window.scrollY / scrollable) * 100 : 0;
    readingBar.style.width = `${Math.min(100, percentage)}%`;
}

function updateActiveSection() {
    const currentPosition = window.scrollY + 160;
    let activeId = "";

    navLinks.forEach((link) => {
        const section = document.querySelector(link.getAttribute("href"));
        if (section && section.offsetTop <= currentPosition) {
            activeId = link.getAttribute("href");
        }
    });

    navLinks.forEach((link) => {
        link.classList.toggle("active", link.getAttribute("href") === activeId);
    });
}

progressItems.forEach((item) => item.addEventListener("change", updateCompletion));

copyButtons.forEach((button) => {
    button.addEventListener("click", async () => {
        const code = button.closest(".code-block").querySelector("code").innerText;

        try {
            await navigator.clipboard.writeText(code);
            button.textContent = "Copié !";
            setTimeout(() => {
                button.textContent = "Copier";
            }, 1600);
        } catch {
            button.textContent = "Sélectionne le code";
        }
    });
});

window.addEventListener("scroll", () => {
    updateReadingProgress();
    updateActiveSection();
}, { passive: true });

restoreCompletion();
updateReadingProgress();
updateActiveSection();
