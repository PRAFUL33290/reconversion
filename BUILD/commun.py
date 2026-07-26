# -*- coding: utf-8 -*-
"""Éléments partagés par les générateurs de pages (en-tête, pied, coquille HTML).

Le menu n'est écrit qu'ici : toute modification est ensuite répercutée dans
LANGAGES/ et AXES/ en relançant les générateurs. La page d'accueil
(index.html) reste écrite à la main et doit être alignée manuellement.
"""

RACINE = "/Users/julien/Desktop/RECONVERSION PRO"

# Icônes du menu principal : SVG au trait, 24x24, sans remplissage.
ICONES_MENU = {
    "accueil": '<path d="M4 10.5 12 4l8 6.5V19a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 19z"/><path d="M9.5 20.5v-6h5v6"/>',
    "objectif": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r=".6" fill="currentColor" stroke="none"/>',
    "competences": '<path d="M4 7.5h9"/><path d="M4 12h13"/><path d="M4 16.5h7"/><path d="M17.5 16.5l2 2 3-3.5"/>',
    "marche": '<path d="M4 19V5"/><path d="M4 19h16"/><path d="M7.5 15.5l3.5-4 3 2.5 4.5-6"/>',
    "renforcer": '<path d="M12 3.5v12"/><path d="M8 7.5 12 3.5l4 4"/><path d="M5 20.5h14"/><path d="M5 20.5v-3"/><path d="M19 20.5v-6"/>',
    "atomisation": '<circle cx="12" cy="12" r="2.6"/><ellipse cx="12" cy="12" rx="9" ry="4" transform="rotate(30 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="4" transform="rotate(-30 12 12)"/>',
    "technologies": '<path d="M8.5 8.5 5 12l3.5 3.5"/><path d="M15.5 8.5 19 12l-3.5 3.5"/><path d="M13.4 5.5l-2.8 13"/>',
}

# (clé d'icône, libellé court affiché, libellé complet, cible relative à la racine)
MENU = [
    ("accueil", "Accueil", "Accueil — tableau de bord du projet", "index.html"),
    ("objectif", "Objectif", "Objectif professionnel", "AXES/objectif.html"),
    ("competences", "Compétences", "Compétences actuelles", "AXES/competences-actuelles.html"),
    ("marche", "Marché", "Besoins du marché", "AXES/besoins-marches.html"),
    ("renforcer", "Renforcer", "Compétences à renforcer", "AXES/competences-a-renforcer.html"),
    ("atomisation", "Atomisation", "Atomisation — le positionnement unique", "AXES/atomisation.html"),
]


def icone(cle, classe="nav-icon"):
    return (f'<svg class="{classe}" viewBox="0 0 24 24" aria-hidden="true">'
            f'{ICONES_MENU[cle]}</svg>')


def entete(home="../", actif=""):
    """`home` = chemin vers la racine du site. `actif` = cible du menu courant."""
    liens = ""
    for cle, court, complet, cible in MENU:
        courant = ' aria-current="page"' if cible == actif else ""
        liens += f"""
                <li>
                    <a href="{home}{cible}" title="{complet}"{courant}>
                        {icone(cle)}
                        {court}
                    </a>
                </li>"""

    lignes_mobiles = []
    for _, _, complet, cible in MENU:
        courant = ' aria-current="page"' if cible == actif else ""
        lignes_mobiles.append(
            f'                    <a href="{home}{cible}"{courant}>{complet}</a>')
    liens_mobiles = "\n".join(lignes_mobiles)

    return f"""    <a class="skip-link" href="#contenu">Aller au contenu</a>

    <div class="background-shapes" aria-hidden="true">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
    </div>

    <header class="glass-header">
        <a class="logo project-logo" href="{home}index.html" aria-label="Retour à l’accueil">
            Reconversion<span>Pro.</span>
        </a>
        <nav aria-label="Navigation principale">
            <ul class="nav-list">{liens}
                <li class="learning-menu">
                    <details>
                        <summary class="btn-primary">Les technologies</summary>
                        <div class="learning-dropdown">
                            <div class="learning-dropdown-head">
                                <div>
                                    <span class="learning-overline">Parcours d’apprentissage</span>
                                    <p>Chaque technologie, expliquée simplement</p>
                                </div>
                                <span class="progress-count">10 modules</span>
                            </div>
                            <div class="progress-track" aria-label="10 modules disponibles"><span></span></div>
                            <ol></ol>
                            <div class="learning-links">
                                <a class="learning-overview" href="{home}LANGAGES/index.html">
                                    Les langages expliqués simplement <span aria-hidden="true">→</span>
                                </a>
                                <a class="learning-overview" href="{home}index.html#formation">
                                    Voir le parcours de formation <span aria-hidden="true">→</span>
                                </a>
                            </div>
                        </div>
                    </details>
                </li>
            </ul>
        </nav>
        <details class="mobile-menu">
            <summary>Menu <span aria-hidden="true">⌄</span></summary>
            <div class="mobile-menu-panel">
                <nav aria-label="Navigation mobile">
{liens_mobiles}
                    <a href="{home}LANGAGES/index.html">Les langages</a>
                </nav>
                <p>Les technologies du parcours</p>
                <ol></ol>
            </div>
        </details>
    </header>
"""


def pied(home="../"):
    return f"""    <footer>
        <a class="logo project-logo" href="{home}index.html">Reconversion<span>Pro.</span></a>
        <p>Projet de transition professionnelle — Julien Guerrier</p>
        <p>2026</p>
    </footer>
    <script src="{home}FORMATIONS/modules-catalog.js"></script>
    <script src="{home}FORMATIONS/navigation.js"></script>
"""


def page(titre, description, corps, feuille, home="../", actif=""):
    return f"""<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{description}">
    <meta name="theme-color" content="#f9f8f7">
    <title>{titre}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{home}styles.css">
    <link rel="stylesheet" href="{feuille}">
</head>
<body>
{entete(home, actif)}
{corps}
{pied(home)}
</body>
</html>
"""
