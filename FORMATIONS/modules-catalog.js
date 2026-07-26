/* Source unique du parcours de formation.
   Consommée par navigation.js (accueil + modules 01/02) et par
   module-renderer.js (modules générés 03 à 10).
   « tagline » doit rester une phrase simple, compréhensible sans bagage
   technique : c'est ce que lit un visiteur qui découvre le métier. */
window.FORMATION_MODULES = [
    {
        number: "01",
        name: "HTML",
        file: "MODULE_01_HTML5.html",
        group: "Le site visible",
        tagline: "La structure de la page : titres, textes, images et liens."
    },
    {
        number: "02",
        name: "CSS",
        file: "MODULE_02_CSS3_PRAFUL_CITY_CMS.html",
        group: "Le site visible",
        tagline: "L’apparence : couleurs, polices, espacements et mise en page."
    },
    {
        number: "03",
        name: "JavaScript",
        file: "MODULE_03_JAVASCRIPT.html",
        group: "Le site visible",
        tagline: "Les interactions : menus, filtres et boutons qui réagissent."
    },
    {
        number: "04",
        name: "MySQL",
        file: "MODULE_04_MYSQL.html",
        group: "Les coulisses",
        tagline: "La base de données : là où sont rangées les infos du site."
    },
    {
        number: "05",
        name: "PHP",
        file: "MODULE_05_PHP.html",
        group: "Les coulisses",
        tagline: "Le code du serveur : il va chercher les données et fabrique la page."
    },
    {
        number: "06",
        name: "Symfony",
        file: "MODULE_06_SYMFONY.html",
        group: "Les coulisses",
        tagline: "Une boîte à outils PHP pour bâtir un site solide et durable."
    },
    {
        number: "07",
        name: "Tableau de bord",
        file: "MODULE_07_TABLEAU_DE_BORD_ET_ACTUALITES.html",
        group: "Le CMS municipal",
        tagline: "L’espace d’administration pour publier les actualités."
    },
    {
        number: "08",
        name: "Agenda",
        file: "MODULE_08_AGENDA_ET_EVENEMENTS.html",
        group: "Le CMS municipal",
        tagline: "Le calendrier des événements de la commune."
    },
    {
        number: "09",
        name: "Publications",
        file: "MODULE_09_PUBLICATIONS_ET_GESTION_DOCUMENTAIRE.html",
        group: "Le CMS municipal",
        tagline: "La mise en ligne des documents officiels et comptes rendus."
    },
    {
        number: "10",
        name: "Services municipaux",
        file: "MODULE_10_SERVICES_MUNICIPAUX.html",
        group: "Le CMS municipal",
        tagline: "Les fiches pratiques : horaires, démarches et contacts."
    }
];
