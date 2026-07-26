#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les cinq pages d'axes dans AXES/.

Le contenu s'appuie sur CV.md (document de synthèse) : chaque page reprend la
définition de l'axe, le récit de sa construction, et l'outil concret qui permet
de le piloter (grille de transfert, matrice, sprints, protocole de test).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import RACINE, page  # noqa: E402

DOSSIER = os.path.join(RACINE, "AXES")
os.makedirs(DOSSIER, exist_ok=True)


def tableau(entetes, lignes, legende=None):
    th = "".join(f"<th scope=\"col\">{h}</th>" for h in entetes)
    corps = ""
    for ligne in lignes:
        cellules = f'<th scope="row">{ligne[0]}</th>' + "".join(
            f"<td>{c}</td>" for c in ligne[1:])
        corps += f"                        <tr>{cellules}</tr>\n"
    cap = f"\n                    <caption>{legende}</caption>" if legende else ""
    return f"""            <div class="table-scroll">
                <table class="axe-table">{cap}
                    <thead>
                        <tr>{th}</tr>
                    </thead>
                    <tbody>
{corps}                    </tbody>
                </table>
            </div>"""


AXES = [
    dict(
        slug="objectif", numero="01", label="Définir",
        titre="L’objectif professionnel",
        menu="AXES/objectif.html",
        lead="Un cap unique, formulé assez précisément pour trier les offres, "
             "assez large pour ne pas fermer de portes.",
        definition=[
            "Quitter progressivement l’animation pour un poste en communication "
            "numérique, création web ou informatique, en mairie, collectivité ou "
            "structure locale autour de Parempuyre et de Bordeaux Métropole.",
            "Le poste le plus cohérent aujourd’hui est <strong>chargé de communication "
            "digitale avec une forte compétence web</strong>. Le profil visé n’est pas "
            "celui d’un spécialiste unique mais d’un trio : communication digitale, "
            "webmaster, support numérique.",
        ],
        blocs=[
            ("Cible principale", [
                "Chargé de communication digitale",
                "Webmaster / gestionnaire de site internet",
                "Assistant communication et numérique",
            ]),
            ("Évolutions possibles", [
                "Intégrateur WordPress / webdesigner",
                "Médiateur ou conseiller numérique",
                "Support informatique de proximité",
                "Administrateur systèmes et réseaux junior, à moyen terme",
            ]),
            ("Zone recherchée", [
                "Parempuyre, Blanquefort, Le Pian-Médoc",
                "Saint-Médard-en-Jalles, Eysines, Le Bouscat",
                "Services communication et numériques de Bordeaux Métropole",
            ]),
        ],
        histoire=[
            "Au départ, l’intention tenait en une phrase vague : « travailler dans le "
            "numérique ». Une phrase impossible à transformer en candidature, parce "
            "qu’elle ne désigne ni un métier, ni un employeur, ni un niveau.",
            "Le cap s’est resserré en confrontant deux réalités : d’un côté les "
            "compétences déjà solides — création graphique, WordPress, vidéo, outils "
            "numériques ; de l’autre les intitulés qui reviennent réellement dans les "
            "offres des communes de la métropole. L’intersection des deux a désigné un "
            "métier plutôt qu’un domaine.",
            "La formulation finale ajoute une contrainte volontaire : rester sur le "
            "territoire et dans le service public. Ce n’est pas une limite, c’est ce "
            "qui rend le profil pertinent — dix ans d’animation en collectivité ne se "
            "valorisent nulle part mieux qu’en collectivité.",
        ],
        outil_titre="Comment il se mesure et se révise",
        outil_intro="Un objectif qui ne se mesure pas devient une intention. Cinq "
                    "indicateurs suffisent, relevés à date fixe.",
        outil_html=tableau(
            ["Indicateur", "Cible", "Rythme de relevé"],
            [
                ["Modules de formation terminés", "10 sur 10", "Mensuel"],
                ["Projets publiés au portfolio", "3, dont 1 institutionnel", "Trimestriel"],
                ["Candidatures ciblées envoyées", "4 par mois en phase active", "Mensuel"],
                ["Entretiens obtenus", "1 pour 8 candidatures", "Trimestriel"],
                ["Compétences critiques comblées", "5 sur 5 (voir axe 04)", "Trimestriel"],
            ],
            "Indicateurs de pilotage de l’objectif professionnel",
        ),
        outil_apres=[
            "<strong>Révision trimestrielle.</strong> Trois questions, dans cet ordre : "
            "les offres réelles correspondent-elles toujours à l’intitulé visé ? les "
            "indicateurs progressent-ils ou stagnent-ils ? faut-il élargir la zone "
            "géographique ou le type de structure ?",
            "L’objectif n’est réécrit que si deux relevés consécutifs stagnent. En "
            "dessous, il s’agit de patience, pas d’un problème de cap.",
        ],
    ),
    dict(
        slug="competences-actuelles", numero="02", label="Valoriser",
        titre="Les compétences actuelles",
        menu="AXES/competences-actuelles.html",
        lead="L’inventaire de ce qui est déjà là — outils maîtrisés, savoir-être, "
             "et dix ans d’expérience de terrain traduits en langage territorial.",
        definition=[
            "Une reconversion ne part jamais de zéro. Cet axe recense ce qui est "
            "immédiatement mobilisable, en séparant ce qui se prouve par un livrable "
            "de ce qui se raconte en entretien.",
            "L’atout central n’est pas un outil en particulier : c’est le "
            "<strong>profil hybride</strong> — expérience humaine de terrain, créativité "
            "visuelle, maîtrise d’outils numériques et capacité à transmettre.",
        ],
        blocs=[
            ("Communication &amp; création", [
                "Photoshop, Illustrator, Canva",
                "Visuels, affiches, logos, chartes graphiques",
                "Montage vidéo : Premiere Pro, Final Cut Pro",
                "Notions d’After Effects, apprentissage de la 3D",
                "Contenus pour les réseaux sociaux",
            ]),
            ("Web &amp; numérique", [
                "Création et administration de sites WordPress",
                "Elementor et Gutenberg",
                "Maintenance, sauvegardes, gestion d’hébergement",
                "Premières compétences en SEO",
                "GitHub, no-code et outils IA",
                "Notions de MySQL, début d’apprentissage du PHP",
            ]),
            ("Savoir-être", [
                "Pédagogie, écoute, patience",
                "Sens du service public",
                "Adaptabilité, autonomie, organisation",
                "Créativité et curiosité numérique",
                "Polyvalence",
            ]),
        ],
        histoire=[
            "L’exercice a commencé par une liste brute, sans filtre : tout ce qui avait "
            "déjà été fait, des affiches de centre de loisirs aux sites WordPress "
            "livrés. Une liste longue, désordonnée, et surtout impossible à envoyer "
            "telle quelle à un recruteur.",
            "Le tri s’est fait avec une seule question, appliquée à chaque ligne : "
            "<em>est-ce que je peux le montrer ?</em> Ce qui se montre devient un "
            "livrable pour le portfolio. Ce qui ne se montre pas mais s’est vécu "
            "devient une histoire à raconter en entretien. Ce qui ne fait ni l’un ni "
            "l’autre sort de la liste.",
            "La révélation est venue de la troisième colonne, celle de l’animation. "
            "Gérer un groupe d’enfants, expliquer une règle à des familles, monter un "
            "événement avec des partenaires : formulé en langage territorial, cela "
            "décrit exactement ce qu’une mairie attend d’un chargé de communication.",
        ],
        outil_titre="La grille de transfert",
        outil_intro="Chaque compétence d’animation est traduite dans le vocabulaire du "
                    "poste visé, avec la preuve qui l’accompagne. C’est cette grille "
                    "qui alimente le CV et les réponses en entretien.",
        outil_html=tableau(
            ["Acquis dans l’animation", "Traduction pour le poste visé", "Preuve mobilisable"],
            [
                ["Animer un groupe, tenir un cadre",
                 "Animer une communauté en ligne, modérer les échanges avec les usagers",
                 "Pages et contenus réseaux sociaux gérés"],
                ["Expliquer une règle, rassurer une famille",
                 "Médiation numérique, accompagnement des agents et des habitants",
                 "Situations vécues, à raconter en entretien"],
                ["Monter un événement avec des partenaires",
                 "Gestion de projet de communication, coordination inter-services",
                 "Événements organisés, rétroplannings"],
                ["Créer les supports d’une activité",
                 "Production de visuels institutionnels, respect d’une charte",
                 "Affiches, logos, chartes graphiques réalisés"],
                ["Rendre compte à une hiérarchie et à des élus",
                 "Reporting, synthèse mensuelle pour la direction",
                 "Bilans d’activité rédigés"],
                ["S’adapter à un imprévu en cinq minutes",
                 "Réactivité éditoriale : alerte, fermeture, information urgente",
                 "Exemples concrets de terrain"],
            ],
            "Traduction des acquis de l’animation vers le métier visé",
        ),
        outil_apres=[
            "La grille sert aussi de garde-fou : rien n’y entre sans preuve ni "
            "situation racontable. C’est ce qui évite d’annoncer une maîtrise là où il "
            "n’y a que des notions — notamment sur PHP et MySQL, présentés comme en "
            "cours d’apprentissage et non comme acquis.",
        ],
    ),
    dict(
        slug="besoins-marches", numero="03", label="Comprendre",
        titre="Les besoins du marché",
        menu="AXES/besoins-marches.html",
        lead="Ce que les collectivités demandent réellement aujourd’hui — pas ce "
             "qu’on imagine qu’elles demandent.",
        definition=[
            "Les collectivités cherchent des profils capables de gérer la "
            "communication, les contenus web, les outils numériques et "
            "l’accompagnement des services ou des usagers. Dans les petites et "
            "moyennes communes, la polyvalence est plus recherchée que "
            "l’ultra-spécialisation.",
            "C’est une bonne nouvelle pour un profil hybride : ce qui ressemble à une "
            "dispersion dans le privé devient un argument dans une commune de "
            "quelques milliers d’habitants, où une seule personne couvre souvent "
            "l’ensemble de la chaîne.",
        ],
        blocs=[
            ("Métiers qui reviennent", [
                "Chargé de communication (digitale)",
                "Community manager territorial",
                "Webmaster, gestionnaire de site",
                "Intégrateur WordPress, webdesigner",
                "Technicien informatique, support de proximité",
                "Conseiller ou médiateur numérique",
            ]),
            ("Compétences techniques attendues", [
                "WordPress",
                "HTML / CSS",
                "Référencement naturel",
                "Accessibilité numérique",
                "Création graphique",
                "Réseaux sociaux et outils collaboratifs",
            ]),
            ("Attentes professionnelles", [
                "Sens du service public",
                "Travail en équipe, gestion de projet",
                "Qualités rédactionnelles",
                "Relation avec les usagers",
                "Autonomie et polyvalence",
            ]),
        ],
        histoire=[
            "Le point de départ n’a pas été une étude de marché mais la lecture "
            "répétée des offres publiées par les communes de la métropole. À force, "
            "les mêmes formulations reviennent — et les mêmes absences : presque "
            "jamais de framework à la mode, presque toujours WordPress, "
            "l’accessibilité et le SEO.",
            "L’observation des sites municipaux existants a complété le tableau. "
            "Agendas jamais à jour, actualités republiées à la main sur trois canaux, "
            "documents officiels difficiles à trouver, formulaires inaccessibles : les "
            "besoins ne sont pas théoriques, ils se voient depuis le navigateur.",
            "Les échanges avec des agents ont confirmé le décalage le plus utile à "
            "connaître : le problème n’est presque jamais l’outil, c’est le temps. Une "
            "compétence qui fait gagner des heures vaut plus qu’une compétence "
            "impressionnante.",
        ],
        outil_titre="La matrice Douleur / Fréquence / Budget",
        outil_intro="Chaque besoin observé est noté sur trois axes : l’intensité de "
                    "la gêne pour l’équipe, la fréquence à laquelle elle revient, et "
                    "la probabilité qu’un budget ou un poste y soit consacré. Les "
                    "lignes fortes sur les trois colonnes indiquent où se placer.",
        outil_html=tableau(
            ["Besoin observé", "Douleur", "Fréquence", "Budget", "Lecture"],
            [
                ["Republier chaque actualité sur le site, Facebook, l’appli et la newsletter",
                 "Forte", "Hebdomadaire", "Moyen",
                 "Cible prioritaire : gain de temps immédiat et visible"],
                ["Collecter les événements des associations pour l’agenda et le bulletin",
                 "Forte", "Mensuelle", "Moyen",
                 "Cible prioritaire : chaîne entière à structurer"],
                ["Traiter les demandes de visuels des autres services",
                 "Moyenne", "Hebdomadaire", "Faible",
                 "Facile à améliorer, bon sujet de démonstration"],
                ["Maintenir le site à jour : sécurité, sauvegardes, contenus",
                 "Forte", "Continue", "Fort",
                 "Cœur du poste de webmaster"],
                ["Mettre le site en conformité d’accessibilité (RGAA)",
                 "Moyenne", "Ponctuelle", "Fort",
                 "Obligation légale : budget existant, compétence rare"],
                ["Accompagner agents et habitants sur les outils numériques",
                 "Moyenne", "Continue", "Moyen",
                 "Terrain naturel du profil hybride"],
                ["Produire le bilan mensuel pour les élus",
                 "Moyenne", "Mensuelle", "Faible",
                 "Peu valorisé mais très automatisable"],
            ],
            "Priorisation des besoins observés dans les communes de la métropole",
        ),
        outil_apres=[
            "Trois lignes ressortent sur les trois colonnes à la fois : la "
            "republication multicanale, la collecte des événements et la maintenance "
            "du site. Ce sont elles qui orientent le choix des compétences à renforcer "
            "et le contenu du portfolio.",
            "L’accessibilité RGAA occupe une place à part : la douleur ressentie est "
            "modérée, mais l’obligation est légale et la compétence peu répandue. "
            "C’est un différenciateur à faible coût d’entrée.",
        ],
    ),
    dict(
        slug="competences-a-renforcer", numero="04", label="Progresser",
        titre="Les compétences à renforcer",
        menu="AXES/competences-a-renforcer.html",
        lead="Le delta précis entre ce qui est acquis et ce que le marché demande, "
             "découpé en sprints qui produisent chacun un livrable.",
        definition=[
            "Cet axe est la soustraction des deux précédents : besoins du marché "
            "moins compétences actuelles. Ce qui reste est le programme — rien de "
            "plus, pour éviter de se former à ce dont personne n’a besoin.",
            "L’ordre compte autant que le contenu : <strong>HTML/CSS → JavaScript → "
            "PHP + MySQL → WordPress avancé → accessibilité, SEO et sécurité → bases "
            "systèmes et réseaux</strong>. Chaque étape rend la suivante compréhensible.",
        ],
        blocs=[
            ("Développement web", [
                "Consolider HTML et CSS",
                "Apprendre les bases de JavaScript",
                "Poursuivre PHP, consolider MySQL",
                "Comprendre le fonctionnement du back-end",
            ]),
            ("Web professionnel", [
                "WordPress avancé",
                "Sécurité et maintenance web",
                "Référencement naturel avancé",
                "Accessibilité numérique et RGAA",
                "Analyse des statistiques web",
            ]),
            ("Terrain territorial", [
                "Communication institutionnelle",
                "Stratégie éditoriale, rédaction pour les habitants",
                "Réseaux sociaux municipaux",
                "Bases de Linux, support utilisateurs",
                "Gestion de parc, notions de réseaux et systèmes",
            ]),
        ],
        histoire=[
            "La première version de cette liste était décourageante : une trentaine de "
            "sujets, tous présentés comme prioritaires. Un programme de plusieurs "
            "années, donc un programme qu’on abandonne au troisième mois.",
            "Le tri est venu de la matrice de l’axe 03. En ne gardant que ce qui "
            "conditionne les besoins réellement budgétés, la liste s’est réduite à "
            "<strong>cinq compétences critiques</strong> : JavaScript, PHP/MySQL, "
            "WordPress avancé et sécurité, accessibilité RGAA, SEO et analytics. Tout "
            "le reste est utile mais peut attendre.",
            "Le découpage en sprints est venu ensuite, d’un constat simple : un module "
            "terminé sans livrable ne laisse aucune trace vérifiable. Chaque sprint "
            "doit produire quelque chose qui se montre — c’est ce qui alimente le "
            "portfolio en même temps que les compétences.",
        ],
        outil_titre="Le plan d’apprentissage par sprints",
        outil_intro="Six sprints, chacun adossé aux modules de formation du site et "
                    "conclu par un livrable publiable. Le sprint n’est terminé que "
                    "quand le livrable existe.",
        outil_html=tableau(
            ["Sprint", "Compétence visée", "Modules", "Livrable qui clôt le sprint"],
            [
                ["01", "HTML et CSS solides", "Modules 01 – 02",
                 "Page d’accueil d’un site municipal fictif, validée et accessible"],
                ["02", "Bases de JavaScript", "Module 03",
                 "Deux interactions utiles : filtre d’actualités et agenda déroulant"],
                ["03", "PHP et MySQL", "Modules 04 – 05",
                 "Formulaire de collecte d’événements enregistré en base"],
                ["04", "Structurer une application", "Module 06",
                 "Espace d’administration minimal pour publier une actualité"],
                ["05", "CMS municipal complet", "Modules 07 – 10",
                 "Tableau de bord, agenda, publications et fiches services"],
                ["06", "Accessibilité, SEO, sécurité", "Transverse",
                 "Audit RGAA et SEO d’un site existant, avec plan de correction"],
            ],
            "Plan d’apprentissage découpé en sprints, avec livrables",
        ),
        outil_apres=[
            "Deux règles tiennent le plan. <strong>Une seule compétence critique à la "
            "fois</strong> : mener deux sprints en parallèle revient à n’en finir "
            "aucun. Et <strong>rien n’est annoncé comme maîtrisé avant son "
            "livrable</strong> — sur un CV territorial, une compétence surévaluée se "
            "détecte en cinq minutes d’entretien.",
            "Les compétences territoriales — communication institutionnelle, support, "
            "réseaux — s’acquièrent en parallèle, par la lecture et l’observation, "
            "sans occuper de sprint dédié.",
        ],
    ),
    dict(
        slug="atomisation", numero="05", label="Se démarquer",
        titre="L’atomisation du positionnement",
        menu="AXES/atomisation.html",
        lead="La combinaison qui ne se copie pas : dix ans de terrain, l’œil "
             "graphique, le web et l’automatisation, au service d’une commune.",
        definition=[
            "« Atomiser » un positionnement, c’est le décomposer jusqu’à obtenir une "
            "formule que personne d’autre ne peut revendiquer à l’identique. Un "
            "développeur est remplaçable par un autre développeur ; une combinaison "
            "rare l’est beaucoup moins.",
            "La formule retenue : <strong>dix ans de terrain en collectivité + "
            "création graphique et vidéo + web et CMS + automatisation respectueuse "
            "des données</strong>. Chaque terme pris seul est banal ; l’ensemble est "
            "difficile à reconstituer.",
        ],
        blocs=[
            ("Ce que personne ne cumule", [
                "Comprendre un public sans jargon",
                "Produire soi-même les visuels",
                "Administrer et sécuriser le site",
                "Automatiser les tâches répétitives",
                "Parler le langage du service public",
            ]),
            ("Les cinq flux à proposer", [
                "Relais automatique sur les canaux citoyens",
                "Collecte et validation des événements",
                "Demandes de visuels et d’impression",
                "Veille et social listening local",
                "Synthèse mensuelle et revue de presse",
            ]),
            ("Le réflexe qui rassure", [
                "RGPD posé avant l’outil",
                "n8n auto-hébergé quand les données sont sensibles",
                "Make pour prototyper vite",
                "Souveraineté des données comme argument",
            ]),
        ],
        histoire=[
            "L’idée est née d’une frustration d’observateur : en regardant travailler "
            "des équipes de communication, les mêmes gestes reviennent chaque semaine. "
            "Copier une actualité vers trois plateformes, relancer une association "
            "pour une photo, recompiler des chiffres en fin de mois. Des heures "
            "dépensées sur des tâches qui n’exigent aucune décision.",
            "La première tentation a été de proposer de l’automatisation pour "
            "elle-même — cinq flux impressionnants, sans ancrage. Ça ne convainc "
            "personne : dans une mairie, une solution qui déplace des données "
            "citoyennes vers un service américain se heurte au premier réflexe du "
            "DPO.",
            "Le positionnement s’est solidifié le jour où le RGPD est passé devant "
            "l’outil. Proposer n8n auto-hébergé, sur les serveurs de la ville, avec "
            "les exécutions illimitées et la maîtrise des données — et réserver Make "
            "aux prototypes. Ce n’est plus une démonstration technique, c’est une "
            "réponse à une contrainte que la collectivité connaît déjà.",
        ],
        outil_titre="Tester et communiquer la formule",
        outil_intro="Un positionnement ne se décrète pas, il se vérifie. Quatre "
                    "épreuves successives, de la moins coûteuse à la plus engageante.",
        outil_html=tableau(
            ["Épreuve", "Comment", "Signal que ça fonctionne"],
            [
                ["Le test des trente secondes",
                 "Énoncer la formule à quelqu’un du secteur, sans préparation",
                 "L’interlocuteur reformule un besoin concret de son service"],
                ["Le test de la preuve",
                 "Montrer un flux réellement construit, pas un schéma",
                 "La question devient « combien de temps pour l’installer ? »"],
                ["Le test du RGPD",
                 "Annoncer l’hébergement local avant qu’on le demande",
                 "L’objection données ne vient pas — elle est déjà traitée"],
                ["Le test de la candidature",
                 "Placer la formule en tête de la lettre, pas en dernière ligne",
                 "Elle est citée pendant l’entretien"],
            ],
            "Protocole de validation du positionnement",
        ),
        outil_apres=[
            "Côté communication, le même message se décline sur trois supports : une "
            "phrase en tête du CV, une page de démonstration au portfolio avec un flux "
            "qui tourne vraiment, et un exemple chiffré en entretien — « cette "
            "republication vous prend deux heures par semaine, elle peut en prendre "
            "dix minutes ».",
            "Ce qu’il faut éviter : vendre l’automatisation comme une suppression de "
            "poste. Dans une collectivité, l’argument qui porte est le temps rendu "
            "aux agents pour ce qu’une machine ne fera pas — le contact avec les "
            "habitants.",
        ],
    ),
]

for i, axe in enumerate(AXES):
    precedent = AXES[i - 1] if i > 0 else None
    suivant = AXES[i + 1] if i < len(AXES) - 1 else None

    blocs = "\n".join(f"""                <article class="axe-list">
                    <h3>{titre}</h3>
                    <ul>
{chr(10).join(f"                        <li>{item}</li>" for item in items)}
                    </ul>
                </article>""" for titre, items in axe["blocs"])

    definition = "\n".join(
        f"                <p>{par}</p>" for par in axe["definition"])
    histoire = "\n".join(
        f"                <li><p>{par}</p></li>" for par in axe["histoire"])
    apres = "\n".join(
        f"            <p class=\"axe-note\">{par}</p>" for par in axe["outil_apres"])

    nav_prec = (f'<a class="lang-prev" href="{precedent["slug"]}.html">'
                f'<span>Axe {precedent["numero"]}</span>'
                f'<strong>{precedent["titre"]}</strong></a>'
                if precedent else '<span></span>')
    nav_suiv = (f'<a class="lang-next" href="{suivant["slug"]}.html">'
                f'<span>Axe {suivant["numero"]}</span>'
                f'<strong>{suivant["titre"]}</strong></a>'
                if suivant else '<span></span>')

    corps = f"""    <main id="contenu" class="lang-page axe-page">
        <nav class="breadcrumb" aria-label="Fil d’ariane">
            <a href="../index.html">Accueil</a>
            <span aria-hidden="true">/</span>
            <span aria-current="page">{axe['titre']}</span>
        </nav>

        <section class="section axe-hero">
            <p class="section-kicker">Axe {axe['numero']} — {axe['label']}</p>
            <div class="axe-hero-title">
                <span class="axe-hero-number" aria-hidden="true">{axe['numero']}</span>
                <h1>{axe['titre']}</h1>
            </div>
            <p class="lang-summary">{axe['lead']}</p>
        </section>

        <section class="section lang-block">
            <h2>La définition</h2>
            <div class="axe-definition">
{definition}
            </div>
            <div class="axe-lists">
{blocs}
            </div>
        </section>

        <section class="section lang-block">
            <h2>Comment il s’est construit</h2>
            <ol class="lang-history">
{histoire}
            </ol>
        </section>

        <section class="section lang-block">
            <h2>{axe['outil_titre']}</h2>
            <p class="axe-intro">{axe['outil_intro']}</p>
{axe['outil_html']}
{apres}
        </section>

        <nav class="lang-nav" aria-label="Autres axes">
            {nav_prec}
            {nav_suiv}
        </nav>
    </main>
"""

    html = page(
        titre=f"{axe['titre']} — Reconversion Pro",
        description=f"Axe {axe['numero']} du projet de reconversion : {axe['lead']}",
        corps=corps,
        feuille="axes.css",
        home="../",
        actif=axe["menu"],
    )
    with open(os.path.join(DOSSIER, f"{axe['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(html)

print("ok", len(AXES), "pages d'axes")
