# Module 10 --- Services municipaux & Fiches de services

> **Praful City CMS -- Parcours de formation**

## 🎯 Objectif

Dans ce module, tu vas créer le **module Services municipaux**, une
fonctionnalité essentielle de tout site de collectivité.

L'objectif est de permettre aux agents de créer et maintenir des fiches
de services claires, accessibles et faciles à mettre à jour.

------------------------------------------------------------------------

# Compétences visées

À la fin de ce module, tu seras capable de :

-   Concevoir une entité `Service`
-   Réaliser un CRUD complet avec Symfony
-   Associer un service à des démarches et des documents
-   Gérer les horaires, contacts et localisations
-   Construire une interface d'administration claire
-   Appliquer les bonnes pratiques d'accessibilité (RGAA)

------------------------------------------------------------------------

# Exemples de services

-   État civil
-   Urbanisme
-   CCAS
-   Jeunesse
-   Culture
-   Sports
-   Police municipale
-   Environnement
-   Bibliothèque
-   Petite enfance

------------------------------------------------------------------------

# Structure des données

Chaque service contiendra :

-   Nom
-   Slug
-   Description courte
-   Description détaillée
-   Adresse
-   Horaires
-   Téléphone
-   E-mail
-   Responsable
-   Catégorie
-   Image
-   Documents associés
-   Démarches associées
-   Coordonnées GPS
-   Statut (Publié / Brouillon)

------------------------------------------------------------------------

# Structure recommandée

``` text
src/
├── Controller/
│   └── ServiceController.php
├── Entity/
│   └── Service.php
├── Form/
│   └── ServiceType.php
├── Repository/
│   └── ServiceRepository.php

templates/
└── admin/
    └── services/
        ├── index.html.twig
        ├── new.html.twig
        ├── edit.html.twig
        ├── show.html.twig
        └── _form.html.twig
```

------------------------------------------------------------------------

# Fonctionnalités

## Administration

-   Ajouter un service
-   Modifier un service
-   Supprimer un service
-   Publier / Dépublier
-   Rechercher un service
-   Filtrer par catégorie

## Front-office

-   Liste des services
-   Fiche détaillée
-   Recherche
-   Filtre par catégorie
-   Carte de localisation (préparation)

------------------------------------------------------------------------

# Exercices

### Exercice 1

Créer l'entité `Service`.

### Exercice 2

Créer la migration Doctrine.

### Exercice 3

Créer `ServiceController`.

### Exercice 4

Créer `ServiceType`.

### Exercice 5

Créer les vues Twig.

### Exercice 6

Créer le CRUD complet.

### Exercice 7

Ajouter une recherche et un filtre par catégorie.

------------------------------------------------------------------------

# Bonnes pratiques

-   Utiliser des catégories cohérentes.
-   Afficher clairement les horaires.
-   Ajouter des liens vers les démarches.
-   Prévoir les champs pour le SEO.
-   Rendre les informations lisibles sur mobile.

------------------------------------------------------------------------

# Validation

Avant de passer au module suivant, tu devras être capable de :

-   [ ] créer une entité Doctrine `Service`
-   [ ] développer un CRUD complet
-   [ ] afficher une fiche de service
-   [ ] filtrer les services
-   [ ] respecter les bonnes pratiques d'accessibilité

------------------------------------------------------------------------

# Mission

Créer le module **Services municipaux** complet.

À la fin, envoie-moi :

-   `Service.php`
-   `ServiceController.php`
-   `ServiceType.php`
-   les vues Twig

Nous réaliserons une revue de code complète avant de passer au **Module
11 --- Annuaire des associations**, où nous développerons un annuaire
avec recherche, catégories et géolocalisation.
