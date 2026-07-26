# Module 9 --- Publications & Gestion documentaire

> **Praful City CMS -- Parcours de formation**

## 🎯 Objectif

Dans ce module, tu vas développer le système de **gestion documentaire**
du CMS.

Les collectivités publient quotidiennement des documents officiels :
bulletins municipaux, comptes-rendus, délibérations, guides pratiques,
formulaires PDF et rapports. Tu vas apprendre à créer un module
permettant de les administrer facilement.

------------------------------------------------------------------------

# Compétences visées

À la fin de ce module, tu seras capable de :

-   Créer une entité `Publication`
-   Gérer les fichiers PDF
-   Réaliser un CRUD complet avec Symfony
-   Organiser les documents par catégories et par année
-   Afficher les documents dans Twig
-   Sécuriser les téléversements

------------------------------------------------------------------------

# Fonctionnalités

Chaque publication comportera :

-   Titre
-   Slug
-   Description
-   Catégorie
-   Année
-   Type de document
-   Fichier PDF
-   Image de couverture (optionnelle)
-   Auteur
-   Statut (Brouillon / Publié)
-   Date de publication

------------------------------------------------------------------------

# Types de documents

-   Bulletin municipal
-   Compte-rendu
-   Délibération
-   Rapport
-   Guide pratique
-   Formulaire administratif
-   Document budgétaire

------------------------------------------------------------------------

# Structure recommandée

``` text
src/
├── Controller/
│   └── PublicationController.php
├── Entity/
│   └── Publication.php
├── Form/
│   └── PublicationType.php
├── Repository/
│   └── PublicationRepository.php

templates/
└── admin/
    └── publications/
        ├── index.html.twig
        ├── new.html.twig
        ├── edit.html.twig
        ├── show.html.twig
        └── _form.html.twig
```

------------------------------------------------------------------------

# Exercices

## Exercice 1

Créer l'entité `Publication`.

## Exercice 2

Créer la migration Doctrine.

## Exercice 3

Créer `PublicationController`.

## Exercice 4

Créer `PublicationType`.

## Exercice 5

Créer la liste des publications.

## Exercice 6

Ajouter une publication avec un fichier PDF.

## Exercice 7

Modifier une publication.

## Exercice 8

Supprimer une publication avec protection CSRF.

------------------------------------------------------------------------

# Gestion des fichiers

Le dossier recommandé :

``` text
public/
└── uploads/
    └── publications/
```

Bonnes pratiques :

-   Accepter uniquement les PDF.
-   Limiter la taille des fichiers.
-   Renommer automatiquement les fichiers.
-   Éviter les doublons.
-   Supprimer le fichier lors de la suppression de la publication.

------------------------------------------------------------------------

# Bonus

Ajouter :

-   recherche par mot-clé ;
-   filtres par catégorie ;
-   filtres par année ;
-   tri par date de publication.

------------------------------------------------------------------------

# Validation

Avant de poursuivre, tu devras être capable de :

-   [ ] créer l'entité `Publication`
-   [ ] téléverser un PDF
-   [ ] afficher les documents
-   [ ] filtrer les publications
-   [ ] supprimer un document en toute sécurité

------------------------------------------------------------------------

# Mission

Créer le module **Publications** complet.

Lorsque tu auras terminé, envoie-moi :

-   `Publication.php`
-   `PublicationController.php`
-   `PublicationType.php`
-   les vues Twig

Nous réaliserons une revue de code complète avant de passer au **Module
10 --- Services municipaux**, qui introduira les fiches de services, les
contacts et les démarches associées.
