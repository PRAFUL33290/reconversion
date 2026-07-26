#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages LANGAGES/*.html à partir d'une source unique."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import RACINE, page as coquille  # noqa: E402

ROOT = os.path.join(RACINE, "LANGAGES")
os.makedirs(ROOT, exist_ok=True)

ICONS = {
    "html": '<path d="M4 4h16l-1.5 15.5L12 21l-6.5-1.5z"/><path d="M8.5 8.5h7l-.5 4.5H10l.3 3 1.7.5 1.7-.5.2-1.5"/>',
    "css": '<path d="M12 3.5a8.5 8.5 0 1 0 0 17c1.2 0 1.8-.8 1.8-1.7 0-1.6 1-2.3 2.4-2.3h1.3a3 3 0 0 0 3-3A8.5 8.5 0 0 0 12 3.5Z"/><circle cx="8.5" cy="9" r=".9" fill="currentColor" stroke="none"/><circle cx="12" cy="7.6" r=".9" fill="currentColor" stroke="none"/><circle cx="15.4" cy="9.4" r=".9" fill="currentColor" stroke="none"/><circle cx="8" cy="13" r=".9" fill="currentColor" stroke="none"/>',
    "javascript": '<rect x="3.5" y="3.5" width="17" height="17" rx="3"/><path d="M10 10v4.5a1.6 1.6 0 0 1-3 .4"/><path d="M17 10.6a1.9 1.9 0 0 0-2.8.5c-.4 1 .4 1.6 1.4 1.9s1.7 1 1.3 2a2 2 0 0 1-2.9.4"/>',
    "php": '<ellipse cx="12" cy="12" rx="9.5" ry="5.5"/><path d="M7 14.5 8.2 9h1.9c1 0 1.4.6 1.2 1.5-.2 1-.9 1.5-1.9 1.5H8"/><path d="M13.5 14.5 14.7 9h1.9c1 0 1.4.6 1.2 1.5-.2 1-.9 1.5-1.9 1.5h-1.4"/>',
    "mysql": '<ellipse cx="12" cy="6" rx="7.5" ry="3"/><path d="M4.5 6v12c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3V6"/><path d="M4.5 12c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3"/>',
    "symfony": '<circle cx="12" cy="12" r="9"/><path d="M8.5 15.5c1.5 1 3-.2 3.6-2 .7-2 1.2-4.4 2.6-4.9 1-.4 1.6.5 1.1 1.2-.6.8-1.8.2-1.4-.9"/><path d="M9 11.2h3.6"/>',
    "wordpress": '<circle cx="12" cy="12" r="9"/><path d="M4 9.5h5"/><path d="M7 9.5 10.5 19 13 12"/><path d="M13.5 9.5 16.5 19 19.5 11"/>',
}

# name, slug, kicker, résumé, histoire (liste de paragraphes), points clés, rôle dans le projet
PAGES = [
    dict(
        slug="html", name="HTML", family="Le site visible",
        tagline="La structure de la page",
        summary="HTML décrit le contenu d’une page web et son organisation : "
                "les titres, les paragraphes, les images, les liens, les formulaires. "
                "C’est le squelette — sans lui, il n’y a rien à afficher.",
        history=[
            "HTML naît en 1991 au CERN, en Suisse. Tim Berners-Lee cherche un moyen "
            "simple de relier entre eux les documents des chercheurs : il invente le "
            "lien hypertexte, et avec lui le web.",
            "Les premières versions ne servent qu’à écrire du texte structuré. Au fil "
            "des années 1990, les navigateurs ajoutent chacun leurs propres balises, et "
            "le web devient un patchwork. Le W3C est créé pour remettre de l’ordre et "
            "publier des normes communes.",
            "HTML5, finalisé en 2014, marque la maturité du langage : vidéo et audio "
            "sans greffon, balises qui décrivent le sens du contenu (en-tête, "
            "navigation, article), et une attention nouvelle portée à l’accessibilité.",
        ],
        keys=[
            ("Un langage de balisage, pas de programmation",
             "HTML ne calcule rien et ne prend aucune décision : il nomme et ordonne le contenu."),
            ("La sémantique compte",
             "Choisir la bonne balise aide les moteurs de recherche et les lecteurs d’écran à comprendre la page."),
            ("Toujours lisible",
             "Une page HTML reste un simple fichier texte, ouvrable et modifiable dans n’importe quel éditeur."),
        ],
        role="C’est le premier module du parcours, et la base de tout le reste : "
             "un site municipal bien structuré est un site que tout le monde peut lire, "
             "y compris avec une aide technique.",
        module="MODULE_01_HTML5.html",
    ),
    dict(
        slug="css", name="CSS", family="Le site visible",
        tagline="L’apparence et la mise en page",
        summary="CSS décide de l’allure du site : couleurs, polices, espacements, "
                "colonnes, comportement sur mobile. Le même contenu HTML peut prendre "
                "mille apparences différentes selon la feuille de style appliquée.",
        history=[
            "En 1994, Håkon Wium Lie propose de séparer le contenu de sa présentation. "
            "L’idée est adoptée : CSS 1 sort en 1996, CSS 2 en 1998.",
            "Pendant longtemps, chaque navigateur interprète les règles à sa manière et "
            "les développeurs bricolent des mises en page avec des tableaux. La "
            "situation s’assainit dans les années 2000 avec la standardisation.",
            "CSS3, développé par modules à partir de 2011, apporte les outils modernes : "
            "les media queries pour le responsive, puis Flexbox et Grid, qui permettent "
            "enfin de composer une page comme on compose une affiche.",
        ],
        keys=[
            ("Une règle, un sélecteur",
             "On cible un élément de la page, puis on lui applique des propriétés : couleur, taille, position."),
            ("La cascade",
             "Plusieurs règles peuvent viser le même élément ; des priorités déterminent laquelle gagne."),
            ("Responsive par défaut",
             "Une même feuille de style adapte la page au téléphone, à la tablette et à l’écran de bureau."),
        ],
        role="C’est le terrain où l’expérience en création graphique se transpose "
             "directement : la sensibilité visuelle acquise ailleurs devient ici une "
             "compétence technique.",
        module="MODULE_02_CSS3_PRAFUL_CITY_CMS.html",
    ),
    dict(
        slug="javascript", name="JavaScript", family="Le site visible",
        tagline="Les interactions dans le navigateur",
        summary="JavaScript rend la page vivante : un menu qui s’ouvre, un filtre "
                "d’actualités, une carte interactive, un formulaire qui vérifie ce "
                "qu’on saisit avant l’envoi. C’est le premier véritable langage de "
                "programmation du trio du web.",
        history=[
            "1995 : Brendan Eich écrit le langage en dix jours pour Netscape. Il devait "
            "s’appeler LiveScript ; le nom JavaScript est un coup de marketing, sans "
            "aucun lien de parenté avec Java.",
            "Les années 2000 sont celles de la guerre des navigateurs, où le même script "
            "se comporte différemment partout. L’arrivée d’AJAX puis de bibliothèques "
            "comme jQuery permet enfin d’écrire du code portable.",
            "Depuis ES6 (2015), le langage se modernise chaque année. Avec Node.js, il "
            "sort aussi du navigateur et s’exécute côté serveur — ce qui en fait "
            "aujourd’hui l’un des langages les plus utilisés au monde.",
        ],
        keys=[
            ("Il s’exécute chez le visiteur",
             "Le code part avec la page et tourne dans le navigateur, sans aller-retour vers le serveur."),
            ("Événementiel",
             "On réagit à des actions : un clic, une saisie, un défilement, le chargement de la page."),
            ("Un usage mesuré vaut mieux",
             "Un site doit rester utilisable même quand un script échoue : c’est une question d’accessibilité."),
        ],
        role="Troisième module du parcours. L’objectif n’est pas la performance "
             "technique, mais l’autonomie : savoir ajouter une interaction utile sans "
             "casser la page.",
        module="MODULE_03_JAVASCRIPT.html",
    ),
    dict(
        slug="mysql", name="MySQL", family="Les coulisses",
        tagline="La base de données",
        summary="MySQL est l’armoire de rangement du site : les actualités, les "
                "événements, les comptes rendus, les comptes utilisateurs y sont "
                "stockés sous forme de tables, et on les interroge avec le langage SQL.",
        history=[
            "SQL naît chez IBM dans les années 1970, à partir des travaux d’Edgar Codd "
            "sur le modèle relationnel : ranger les données dans des tables liées entre "
            "elles plutôt que dans des fichiers isolés.",
            "MySQL apparaît en 1995, développé en Suède. Gratuit, rapide et simple à "
            "installer, il devient le compagnon naturel de PHP et l’un des piliers du "
            "web des années 2000.",
            "Racheté par Sun puis par Oracle, il coexiste aujourd’hui avec son "
            "descendant libre MariaDB. La logique reste la même, et elle se réapprend "
            "d’un système à l’autre.",
        ],
        keys=[
            ("Des tables et des relations",
             "Une table « actualités », une table « auteurs », et un lien entre les deux : les données ne sont saisies qu’une fois."),
            ("SQL est déclaratif",
             "On décrit ce que l’on veut obtenir, pas la manière de le chercher."),
            ("La sauvegarde fait partie du métier",
             "Une base sans sauvegarde régulière est un risque, pas un outil."),
        ],
        role="Indispensable dès qu’un site municipal cesse d’être une vitrine figée "
             "pour devenir un outil que les agents alimentent au quotidien.",
        module="MODULE_04_MYSQL.html",
    ),
    dict(
        slug="php", name="PHP", family="Les coulisses",
        tagline="Le code côté serveur",
        summary="PHP travaille sur le serveur, avant que la page n’arrive au visiteur : "
                "il va chercher les données dans la base, assemble le HTML, gère les "
                "connexions et les formulaires. Le visiteur ne voit jamais ce code.",
        history=[
            "1994 : Rasmus Lerdorf écrit quelques outils pour suivre les visites de sa "
            "page personnelle et les nomme Personal Home Page Tools.",
            "PHP 3 puis PHP 4, à la fin des années 1990, en font un vrai langage de "
            "programmation. Avec Apache et MySQL, il équipe une grande partie du web et "
            "récolte au passage une solide réputation de désordre.",
            "PHP 7 (2015) puis PHP 8 changent la donne : bien plus rapide, mieux typé, "
            "outillé pour un code propre. Aujourd’hui, une large majorité des sites du "
            "monde tourne encore sur PHP — WordPress en tête.",
        ],
        keys=[
            ("Exécuté avant l’affichage",
             "Le serveur produit une page HTML finie ; le code source reste invisible."),
            ("Le langage de WordPress",
             "Comprendre PHP, c’est pouvoir dépasser les réglages d’un thème et intervenir réellement."),
            ("La sécurité est centrale",
             "Toute donnée envoyée par un utilisateur doit être vérifiée avant d’être utilisée."),
        ],
        role="C’est la charnière du parcours : le passage de « faire une page » à "
             "« faire un outil » que des agents utilisent chaque semaine.",
        module="MODULE_05_PHP.html",
    ),
    dict(
        slug="symfony", name="Symfony", family="Les coulisses",
        tagline="Un cadre de travail PHP",
        summary="Symfony n’est pas un langage mais un framework : une boîte à outils "
                "PHP qui fournit déjà les briques courantes — routes, sécurité, "
                "formulaires, accès à la base — et impose une organisation claire du "
                "code.",
        history=[
            "L’idée de framework s’impose au milieu des années 2000 : plutôt que de "
            "réécrire les mêmes fondations à chaque projet, on part d’une structure "
            "éprouvée et partagée.",
            "Symfony sort en 2005, développé par la société française SensioLabs. Il "
            "devient une référence en Europe, en particulier dans le secteur public.",
            "Ses composants sont si solides que d’autres projets les réutilisent, "
            "notamment Drupal et Laravel : apprendre Symfony, c’est comprendre une "
            "bonne partie du PHP moderne.",
        ],
        keys=[
            ("Des conventions plutôt que des habitudes",
             "Chaque fichier a sa place ; un nouveau développeur retrouve ses repères immédiatement."),
            ("Modèle-Vue-Contrôleur",
             "Les données, l’affichage et la logique restent séparés — plus simple à corriger et à faire évoluer."),
            ("Pensé pour durer",
             "Versions de support long terme, documentation abondante : un choix raisonnable pour une collectivité."),
        ],
        role="Sixième module : c’est l’étape où l’on écrit un code que quelqu’un "
             "d’autre pourra reprendre. Un critère décisif pour un site public.",
        module="MODULE_06_SYMFONY.html",
    ),
    dict(
        slug="wordpress", name="WordPress", family="Les outils du métier",
        tagline="Le CMS le plus répandu",
        summary="WordPress est un système de gestion de contenu écrit en PHP : il permet "
                "de publier et de mettre à jour un site sans écrire de code. C’est "
                "l’outil que l’on trouve le plus souvent en poste, en mairie comme "
                "ailleurs.",
        history=[
            "2003 : deux développeurs reprennent un projet de blog abandonné, b2/"
            "cafelog, et le relancent sous le nom de WordPress.",
            "Les thèmes puis les extensions transforment l’outil de blog en plateforme "
            "généraliste. Sites vitrines, boutiques, intranets : tout devient possible "
            "sans partir de zéro.",
            "Il propulse aujourd’hui plus de quatre sites sur dix dans le monde. Son "
            "éditeur par blocs, Gutenberg, a rapproché le travail de publication d’une "
            "mise en page visuelle.",
        ],
        keys=[
            ("Publier sans coder",
             "Une secrétaire de mairie peut mettre en ligne un arrêté sans passer par un prestataire."),
            ("Thèmes et extensions",
             "Beaucoup de besoins sont déjà couverts — à condition de choisir des sources fiables et maintenues."),
            ("Les mises à jour ne sont pas optionnelles",
             "Sa popularité en fait une cible : maintenance et sauvegardes font partie du poste."),
        ],
        role="C’est la compétence déjà partiellement acquise, à consolider : "
             "administration, sécurité, accessibilité et maintenance au quotidien.",
        module=None,
    ),
]

def shell(title, description, body, home="../", langhome="index.html", langcurrent=""):
    """Coquille commune ; l'en-tête et le pied viennent de BUILD/commun.py."""
    return coquille(titre=title, description=description, corps=body,
                    feuille="langages.css", home=home)


def icon_svg(slug, cls="lang-icon"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">'
            f'{ICONS[slug]}</svg>')


# ---------- pages individuelles ----------
for i, p in enumerate(PAGES):
    prev_p = PAGES[i - 1] if i > 0 else None
    next_p = PAGES[i + 1] if i < len(PAGES) - 1 else None

    history = "\n".join(
        f"                    <li><p>{par}</p></li>" for par in p["history"])
    keys = "\n".join(f"""                <article class="lang-key">
                    <h3>{t}</h3>
                    <p>{d}</p>
                </article>""" for t, d in p["keys"])

    module_link = ""
    if p["module"]:
        module_link = (f'\n                <a class="btn-primary large" '
                       f'href="../FORMATIONS/{p["module"]}">'
                       f'Ouvrir le module {p["name"]}</a>')

    nav_prev = (f'<a class="lang-prev" href="{prev_p["slug"]}.html">'
                f'<span>Précédent</span><strong>{prev_p["name"]}</strong></a>'
                if prev_p else '<span></span>')
    nav_next = (f'<a class="lang-next" href="{next_p["slug"]}.html">'
                f'<span>Suivant</span><strong>{next_p["name"]}</strong></a>'
                if next_p else '<span></span>')

    body = f"""    <main id="contenu" class="lang-page">
        <nav class="breadcrumb" aria-label="Fil d’ariane">
            <a href="../index.html">Accueil</a>
            <span aria-hidden="true">/</span>
            <a href="index.html">Les langages</a>
            <span aria-hidden="true">/</span>
            <span aria-current="page">{p['name']}</span>
        </nav>

        <section class="section lang-hero">
            <p class="section-kicker">{p['family']}</p>
            <div class="lang-hero-title">
                {icon_svg(p['slug'], 'lang-icon lang-icon-large')}
                <h1>{p['name']}</h1>
            </div>
            <p class="lang-tagline">{p['tagline']}</p>
            <p class="lang-summary">{p['summary']}</p>
        </section>

        <section class="section lang-block">
            <h2>D’où ça vient</h2>
            <ol class="lang-history">
{history}
            </ol>
        </section>

        <section class="section lang-block">
            <h2>Ce qu’il faut retenir</h2>
            <div class="lang-keys">
{keys}
            </div>
        </section>

        <section class="section lang-block">
            <h2>Dans ce projet</h2>
            <div class="lang-role glass-panel">
                <p>{p['role']}</p>{module_link}
            </div>
        </section>

        <nav class="lang-nav" aria-label="Autres langages">
            {nav_prev}
            {nav_next}
        </nav>
    </main>
"""
    page = shell(
        title=f"{p['name']} — Reconversion Pro",
        description=f"{p['name']} : {p['tagline']}. Explication simple et repères "
                    f"historiques, dans le cadre du projet de reconversion.",
        body=body,
        langcurrent="",
    )
    with open(os.path.join(ROOT, f"{p['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(page)

# ---------- index ----------
families = []
for p in PAGES:
    if not families or families[-1][0] != p["family"]:
        families.append((p["family"], []))
    families[-1][1].append(p)

cards = ""
for family, items in families:
    cards += f'\n            <h2 class="lang-family">{family}</h2>\n            <div class="lang-grid">\n'
    for p in items:
        cards += f"""                <a class="lang-card" href="{p['slug']}.html">
                    {icon_svg(p['slug'])}
                    <strong>{p['name']}</strong>
                    <span>{p['tagline']}</span>
                    <p>{p['summary'].split('.')[0]}.</p>
                </a>
"""
    cards += "            </div>\n"

index_body = f"""    <main id="contenu" class="lang-page">
        <nav class="breadcrumb" aria-label="Fil d’ariane">
            <a href="../index.html">Accueil</a>
            <span aria-hidden="true">/</span>
            <span aria-current="page">Les langages</span>
        </nav>

        <section class="section lang-hero">
            <p class="section-kicker">Comprendre avant d’apprendre</p>
            <h1>Les langages du web, expliqués simplement</h1>
            <p class="lang-summary">
                Avant d’écrire une ligne de code, il est utile de savoir à quoi sert
                chaque brique et pourquoi elle existe. Ces pages donnent l’essentiel :
                le rôle du langage, son histoire en trois temps, et sa place dans ce
                projet de reconversion.
            </p>
        </section>

        <section class="section lang-block">
            <h2>Une très courte histoire des langages</h2>
            <ol class="lang-history">
                <li><p>Dans les années 1950, programmer signifie écrire dans le langage
                de la machine : des suites de nombres. Fortran puis COBOL introduisent
                une idée décisive — écrire dans une langue lisible par un humain, et
                laisser un traducteur produire le code machine.</p></li>
                <li><p>Les décennies suivantes cherchent la clarté : C (1972) pour la
                maîtrise fine du matériel, puis la programmation orientée objet, qui
                range le code en morceaux réutilisables. Un principe s’installe : un
                programme est d’abord lu par des humains, l’ordinateur ne fait que
                l’exécuter.</p></li>
                <li><p>À partir de 1991, le web ajoute sa propre famille de langages —
                HTML, CSS, JavaScript, PHP — conçus pour être publiés aussitôt
                qu’écrits. C’est cette famille que suit le parcours de formation, du
                visible jusqu’aux coulisses.</p></li>
            </ol>
        </section>

        <section class="section lang-block">
{cards}        </section>
    </main>
"""

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(shell(
        title="Les langages — Reconversion Pro",
        description="Les langages et technologies du web expliqués simplement : HTML, "
                    "CSS, JavaScript, MySQL, PHP, Symfony, WordPress.",
        body=index_body,
        langcurrent=' aria-current="page"',
    ))

print("ok", len(PAGES) + 1, "pages")
