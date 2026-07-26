# Module 01 — Construire une page web avec HTML5

> Parcours Praful City CMS · Projet fil rouge : **Ville de Nova**

## Présentation du module

HTML est le langage qui permet d’organiser le contenu d’une page web. Il indique au navigateur ce qui est un titre, un paragraphe, une navigation, une image, une actualité ou encore un formulaire.

Dans ce premier module, tu vas construire la structure de la page d’accueil d’un site municipal fictif : **Ville de Nova**. Le design sera ajouté plus tard avec CSS.

### Objectif général

À la fin du module, tu sauras créer une page HTML5 :

- valide et correctement structurée ;
- compréhensible par les navigateurs et les moteurs de recherche ;
- accessible au clavier et aux technologies d’assistance ;
- organisée avec des balises sémantiques ;
- prête à recevoir une mise en forme CSS.

### Durée conseillée

Entre **4 et 6 heures**, réparties en plusieurs séances courtes.

### Prérequis

- Savoir créer un dossier et un fichier.
- Disposer d’un éditeur de code, par exemple Visual Studio Code.
- Savoir ouvrir un fichier HTML dans un navigateur.

---

## 1. Comprendre le rôle du HTML

HTML signifie **HyperText Markup Language**, ou langage de balisage hypertexte.

Une page web utilise généralement trois technologies complémentaires :

| Technologie | Rôle | Exemple |
|---|---|---|
| HTML | Structure et sens du contenu | Un titre, un article, un bouton |
| CSS | Apparence et mise en page | Couleurs, espacements, colonnes |
| JavaScript | Comportement et interactions | Menu mobile, filtre, formulaire |

HTML n’est pas un langage de programmation. Il utilise des **balises** pour décrire la nature des contenus.

```html
<h1>Bienvenue à Nova</h1>
<p>Retrouvez les actualités et les services de votre commune.</p>
```

Ici :

- `<h1>` indique le titre principal ;
- `<p>` indique un paragraphe ;
- `</h1>` et `</p>` ferment les éléments.

### À retenir

Une balise ne doit pas être choisie selon son apparence, mais selon le **sens** du contenu.

---

## 2. Préparer le projet

Crée l’arborescence suivante :

```text
ville-de-nova/
├── index.html
├── css/
├── js/
└── images/
```

Pour ce module, seul le fichier `index.html` sera utilisé.

### Ouvrir la page

1. Ouvre le dossier `ville-de-nova` dans ton éditeur.
2. Crée le fichier `index.html`.
3. Enregistre-le.
4. Ouvre ce fichier dans ton navigateur.
5. Actualise la page après chaque modification.

---

## 3. Écrire la structure minimale

Commence avec ce document :

```html
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Site officiel de la Ville de Nova : actualités, agenda et services municipaux.">
    <title>Ville de Nova — Site officiel</title>
</head>
<body>

</body>
</html>
```

### Explication ligne par ligne

`<!doctype html>`  
Indique que le document utilise la version moderne de HTML.

`<html lang="fr">`  
Contient toute la page et précise que son contenu est en français.

`<head>`  
Contient les informations destinées au navigateur et aux moteurs de recherche.

`<meta charset="utf-8">`  
Permet d’afficher correctement les accents et caractères spéciaux.

`<meta name="viewport">`  
Permet à la page de s’adapter correctement aux écrans mobiles.

`<meta name="description">`  
Résume le contenu de la page.

`<title>`  
Définit le texte affiché dans l’onglet du navigateur.

`<body>`  
Contient tout ce qui sera visible dans la page.

### Exercice 1 — Première page

1. Recopie la structure minimale.
2. Remplace le titre par `Ville de Nova — Accueil`.
3. Ajoute un paragraphe dans `<body>`.
4. Ouvre la page dans ton navigateur.

---

## 4. Hiérarchiser les titres et les textes

HTML propose six niveaux de titres, de `<h1>` à `<h6>`.

```html
<h1>Ville de Nova</h1>
<h2>Actualités</h2>
<h3>Ouverture de la médiathèque</h3>
```

Bonnes pratiques :

- utilise un seul `<h1>` pour le sujet principal de la page ;
- ne choisis pas un niveau pour obtenir une taille particulière ;
- conserve une hiérarchie logique ;
- utilise `<p>` pour les paragraphes, pas pour les titres.

```html
<p>
    La nouvelle médiathèque ouvrira ses portes samedi à partir de 10 h.
</p>
```

### Mettre certains mots en valeur

```html
<p>La mairie sera <strong>exceptionnellement fermée</strong> lundi.</p>
<p>Les inscriptions sont ouvertes <em>jusqu’au 15 septembre</em>.</p>
```

- `<strong>` indique une information importante ;
- `<em>` marque une insistance.

---

## 5. Utiliser les balises sémantiques

Les balises sémantiques décrivent le rôle des différentes zones.

```text
body
├── header
│   └── nav
├── main
│   ├── section
│   │   └── article
│   ├── section
│   └── section
└── footer
```

### Les principales balises

| Balise | Utilisation |
|---|---|
| `<header>` | En-tête d’une page ou d’un contenu |
| `<nav>` | Ensemble de liens de navigation |
| `<main>` | Contenu principal et unique de la page |
| `<section>` | Groupe de contenus partageant un même thème |
| `<article>` | Contenu autonome, comme une actualité |
| `<aside>` | Information complémentaire |
| `<footer>` | Pied de page ou informations de fin |

### Exemple

```html
<body>
    <header>
        <p>Ville de Nova</p>
        <nav aria-label="Navigation principale">
            <!-- Liens du menu -->
        </nav>
    </header>

    <main>
        <section>
            <h1>Bienvenue sur le site de la Ville de Nova</h1>
            <p>Actualités, démarches et vie locale.</p>
        </section>

        <section>
            <h2>Les dernières actualités</h2>
            <article>
                <h3>Ouverture de la médiathèque</h3>
                <p>Découvrez ce nouvel espace culturel.</p>
            </article>
        </section>
    </main>

    <footer>
        <p>© Ville de Nova</p>
    </footer>
</body>
```

### Exercice 2 — Le squelette municipal

Dans `index.html`, ajoute :

- un `<header>` ;
- une navigation ;
- un `<main>` ;
- une section d’introduction ;
- une section « Actualités » ;
- une section « Agenda » ;
- une section « Services » ;
- un `<footer>`.

Chaque section doit posséder un titre.

---

## 6. Créer une navigation avec des liens

Un lien est créé avec la balise `<a>`.

```html
<a href="contact.html">Contacter la mairie</a>
```

Pour créer un menu :

```html
<nav aria-label="Navigation principale">
    <ul>
        <li><a href="#actualites">Actualités</a></li>
        <li><a href="#agenda">Agenda</a></li>
        <li><a href="#services">Services</a></li>
    </ul>
</nav>
```

Les valeurs de `href` qui commencent par `#` ciblent un identifiant de la même page :

```html
<section id="actualites">
    <h2>Actualités</h2>
</section>
```

La valeur d’un `id` doit être unique.

### Types de liens utiles

```html
<a href="https://www.service-public.fr/">Service-Public.fr</a>
<a href="mailto:contact@nova.fr">Écrire à la mairie</a>
<a href="tel:+33500000000">Appeler la mairie</a>
```

Utilise des intitulés explicites. Évite les liens intitulés uniquement « Cliquez ici ».

---

## 7. Organiser le contenu avec des listes

### Liste non ordonnée

```html
<ul>
    <li>État civil</li>
    <li>Urbanisme</li>
    <li>Vie associative</li>
</ul>
```

### Liste ordonnée

```html
<ol>
    <li>Remplir le formulaire</li>
    <li>Ajouter les justificatifs</li>
    <li>Envoyer la demande</li>
</ol>
```

Utilise une liste lorsque plusieurs éléments appartiennent réellement à un même ensemble.

---

## 8. Ajouter une image accessible

```html
<img
    src="images/mediatheque-nova.jpg"
    alt="Façade vitrée de la médiathèque de Nova"
    width="800"
    height="450"
>
```

L’attribut `alt` décrit l’information portée par l’image.

- Image informative : écris une description concise et utile.
- Image décorative : utilise `alt=""`.
- Ne commence pas par « image de » : le lecteur d’écran annonce déjà qu’il s’agit d’une image.
- Indique si possible `width` et `height` pour stabiliser la mise en page.

### Associer une image à une légende

```html
<figure>
    <img
        src="images/parc-nova.jpg"
        alt="Promeneurs dans le parc municipal de Nova"
        width="800"
        height="450"
    >
    <figcaption>Le parc municipal au printemps.</figcaption>
</figure>
```

---

## 9. Structurer les actualités

Une actualité peut être représentée par un `<article>`, car elle forme un contenu autonome.

```html
<section id="actualites">
    <h2>Les dernières actualités</h2>

    <article>
        <p>Culture</p>
        <h3>La médiathèque ouvre ses portes</h3>
        <p>Un nouvel espace de lecture et de rencontre au cœur de Nova.</p>
        <a href="#">Lire l’actualité complète</a>
    </article>

    <article>
        <p>Environnement</p>
        <h3>Une journée pour nettoyer les berges</h3>
        <p>Habitants et associations se mobilisent samedi matin.</p>
        <a href="#">Lire l’actualité complète</a>
    </article>
</section>
```

### Exercice 3 — Trois actualités

Crée trois articles fictifs comprenant chacun :

- une catégorie ;
- un titre `<h3>` ;
- un résumé ;
- un lien dont le texte décrit clairement la destination.

Thèmes suggérés : culture, travaux et environnement.

---

## 10. Créer un formulaire simple

Un champ doit toujours posséder un libellé visible.

```html
<form action="#" method="post">
    <div>
        <label for="email">Adresse e-mail</label>
        <input
            type="email"
            id="email"
            name="email"
            autocomplete="email"
            required
        >
    </div>

    <div>
        <label for="message">Votre message</label>
        <textarea id="message" name="message" rows="5" required></textarea>
    </div>

    <button type="submit">Envoyer le message</button>
</form>
```

Points importants :

- `for="email"` correspond à `id="email"` ;
- `name` identifie la donnée envoyée ;
- `type="email"` demande une adresse électronique ;
- `required` indique que le champ est obligatoire ;
- le bouton possède un texte clair.

Le formulaire ne pourra pas envoyer réellement de message sans traitement côté serveur. Pour ce module, seule sa structure est demandée.

---

## 11. Les erreurs fréquentes

### Oublier de fermer ou imbriquer correctement les balises

Incorrect :

```html
<p>Bienvenue <strong>sur le site</p></strong>
```

Correct :

```html
<p>Bienvenue <strong>sur le site</strong></p>
```

### Utiliser `<br>` pour créer des espaces

Les espacements visuels seront gérés plus tard avec CSS. `<br>` sert uniquement à créer un retour à la ligne qui a du sens dans le contenu, par exemple dans une adresse.

### Utiliser trop de `<div>`

Une `<div>` est un conteneur sans signification particulière. Avant de l’utiliser, vérifie si `<header>`, `<nav>`, `<main>`, `<section>`, `<article>` ou `<footer>` serait plus précis.

### Mettre un bouton à la place d’un lien

- Un lien `<a>` permet de changer de page ou de section.
- Un bouton `<button>` déclenche une action.

### Écrire plusieurs `<h1>`

Pour ce projet, conserve un seul titre principal `<h1>` et utilise des `<h2>` pour les grandes sections.

---

## 12. Projet de validation — Accueil de la Ville de Nova

### Mission

Crée la première version complète de `index.html` pour le site municipal fictif **Ville de Nova**.

### Contenu obligatoire

#### En-tête

- Le nom « Ville de Nova ».
- Une navigation vers Actualités, Agenda et Services.

#### Introduction

- Un titre principal.
- Une phrase de présentation.
- Un lien vers la section Services.

#### Actualités

- Trois articles.
- Une hiérarchie de titres correcte.
- Au moins une image avec un texte alternatif pertinent.

#### Agenda

- Trois événements présentés sous forme de liste.
- Une date, un titre et un lieu pour chaque événement.
- Une date écrite avec la balise `<time>`.

Exemple :

```html
<time datetime="2026-09-12">12 septembre 2026</time>
```

#### Services municipaux

- Une liste d’au moins quatre services.
- Un lien explicite pour accéder à chaque service.

#### Contact

- Un petit formulaire comprenant un e-mail et un message.
- Des libellés correctement associés aux champs.

#### Pied de page

- Les coordonnées fictives de la mairie.
- Un lien vers les mentions légales.

### Contraintes

- Ne pas ajouter de CSS pour le moment.
- Utiliser un seul `<h1>`.
- Utiliser les balises sémantiques adaptées.
- Ne pas utiliser de texte « Lorem ipsum ».
- Indenter le code de manière régulière.
- Vérifier que tous les liens internes ciblent un `id` existant.

---

## 13. Grille d’auto-évaluation

Coche chaque point avant de considérer le module terminé.

### Structure

- [ ] Le document commence par `<!doctype html>`.
- [ ] La langue française est déclarée.
- [ ] Le codage UTF-8 et le viewport sont renseignés.
- [ ] Le titre de l’onglet est précis.
- [ ] Le contenu visible se trouve dans `<body>`.

### Sémantique

- [ ] La page contient `<header>`, `<nav>`, `<main>` et `<footer>`.
- [ ] Chaque grande section possède un titre.
- [ ] Les actualités utilisent `<article>`.
- [ ] Un seul `<h1>` est présent.
- [ ] Les niveaux de titres suivent un ordre logique.

### Accessibilité

- [ ] Toutes les images possèdent un attribut `alt`.
- [ ] Les textes des liens décrivent leur destination.
- [ ] Chaque champ de formulaire possède un `<label>`.
- [ ] La navigation possède un nom accessible.
- [ ] Le contenu reste compréhensible sans mise en forme.

### Qualité

- [ ] Les balises sont correctement fermées et imbriquées.
- [ ] L’indentation est régulière.
- [ ] Les identifiants sont uniques.
- [ ] Aucun `<br>` n’est utilisé pour créer des espacements.
- [ ] Aucun style n’est écrit directement dans le HTML.

---

## 14. Quiz de fin de module

1. Quel est le rôle principal de HTML ?
2. Quelle partie contient les informations non visibles destinées au navigateur ?
3. Pourquoi ajoute-t-on `lang="fr"` à la balise `<html>` ?
4. Quelle est la différence entre `<section>` et `<article>` ?
5. Combien de titres `<h1>` utiliseras-tu dans ce projet ?
6. À quoi sert l’attribut `alt` d’une image ?
7. Comment relier un `<label>` à un champ ?
8. Quelle différence existe entre un lien et un bouton ?
9. Pourquoi faut-il éviter de choisir une balise selon son apparence ?
10. Quelle balise permet de représenter une date de manière sémantique ?

<details>
<summary>Afficher les réponses</summary>

1. Structurer et donner du sens au contenu.
2. La partie `<head>`.
3. Pour indiquer la langue aux navigateurs, moteurs de recherche et technologies d’assistance.
4. Une section regroupe un thème ; un article constitue un contenu autonome.
5. Un seul.
6. À transmettre l’information de l’image lorsqu’elle n’est pas visible.
7. La valeur `for` du label doit correspondre à l’`id` du champ.
8. Le lien mène vers une destination ; le bouton déclenche une action.
9. Parce que HTML décrit le sens, tandis que CSS gère l’apparence.
10. `<time>`.

</details>

---

## 15. Validation du module

Le module est validé lorsque :

1. la page demandée est entièrement réalisée ;
2. la grille d’auto-évaluation est complétée ;
3. le code est lisible et sémantique ;
4. les erreurs relevées lors de la correction sont comprises et corrigées.

### Livrable

Envoie le fichier `index.html` du projet **Ville de Nova** pour correction.

La correction portera sur :

- la structure du document ;
- le choix des balises ;
- la hiérarchie des titres ;
- l’accessibilité de base ;
- la clarté et l’indentation du code.

Une fois ce module validé, la prochaine étape sera :

> **Module 02 — Mettre en forme la page avec CSS3**
