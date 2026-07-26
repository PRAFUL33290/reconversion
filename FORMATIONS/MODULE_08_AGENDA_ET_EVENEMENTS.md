# Module 8 --- Agenda & Gestion des événements

> **Praful City CMS -- Parcours de formation**

## 🎯 Objectif

Dans ce module, tu vas développer le **module Agenda**, indispensable
sur les sites des collectivités.

À la fin de ce module, tu seras capable de créer un système complet de
gestion des événements municipaux.

------------------------------------------------------------------------

# Compétences visées

-   Créer une entité `Event`
-   Réaliser un CRUD complet avec Symfony
-   Gérer les dates et horaires
-   Afficher les événements dans Twig
-   Trier les événements à venir et passés
-   Préparer l'intégration d'un calendrier interactif

------------------------------------------------------------------------

# Fonctionnalités

Chaque événement contiendra :

-   Titre
-   Description
-   Date de début
-   Date de fin
-   Heure
-   Lieu
-   Catégorie
-   Organisateur
-   Image
-   Tarif (si nécessaire)
-   Lien d'inscription
-   Statut (Brouillon / Publié)

------------------------------------------------------------------------

# Structure recommandée

``` text
src/
├── Controller/
│   └── EventController.php
├── Entity/
│   └── Event.php
├── Form/
│   └── EventType.php
├── Repository/
│   └── EventRepository.php

templates/
└── admin/
    └── events/
        ├── index.html.twig
        ├── new.html.twig
        ├── edit.html.twig
        └── show.html.twig
```

------------------------------------------------------------------------

# Exercices

## Exercice 1

Créer l'entité `Event`.

## Exercice 2

Créer la migration Doctrine.

## Exercice 3

Créer `EventController`.

## Exercice 4

Créer `EventType`.

## Exercice 5

Afficher la liste des événements.

## Exercice 6

Ajouter un événement.

## Exercice 7

Modifier un événement.

## Exercice 8

Supprimer un événement avec protection CSRF.

------------------------------------------------------------------------

# Bonus

Préparer l'intégration de **FullCalendar** afin d'afficher les
événements dans une vue calendrier.

------------------------------------------------------------------------

# Bonnes pratiques

-   Vérifier que la date de fin est postérieure à la date de début.
-   Utiliser des routes explicites.
-   Valider les champs obligatoires.
-   Afficher des messages de succès et d'erreur.
-   Utiliser les composants Twig pour éviter les duplications.

------------------------------------------------------------------------

# Validation

Avant de poursuivre, tu devras être capable de :

-   [ ] créer une entité Doctrine `Event`
-   [ ] gérer un CRUD complet
-   [ ] afficher les événements dans Twig
-   [ ] trier les événements
-   [ ] comprendre comment intégrer un calendrier

------------------------------------------------------------------------

# Mission

Créer le module **Agenda** complet.

Lorsque tu auras terminé, envoie-moi :

-   `Event.php`
-   `EventController.php`
-   `EventType.php`
-   les vues Twig

Nous réaliserons une revue de code, puis nous passerons au module
**Publications & Documents**, utilisé pour gérer les bulletins
municipaux, comptes-rendus et documents officiels.
