# Module 7 --- Tableau de bord & Gestion des actualités

> **Praful City CMS -- Parcours de formation**

## 🎯 Objectif

Ce module marque le début du développement des **fonctionnalités
métier** du CMS.

Tu vas créer le premier module réellement utilisé par une mairie : **la
gestion des actualités**.

À la fin de ce module, tu disposeras d'un tableau de bord permettant de
consulter, créer, modifier et supprimer des actualités.

------------------------------------------------------------------------

# Compétences visées

-   Construire un tableau de bord d'administration.
-   Réaliser un CRUD complet.
-   Utiliser Doctrine avec Symfony.
-   Créer des formulaires Symfony.
-   Afficher les données dans Twig.
-   Gérer les messages de confirmation.
-   Sécuriser les actions d'administration.

------------------------------------------------------------------------

# Fonctionnalités du module

## Tableau de bord

Créer une page d'administration affichant :

-   nombre d'actualités ;
-   nombre d'événements ;
-   nombre de services ;
-   derniers contenus publiés ;
-   accès rapide aux modules.

------------------------------------------------------------------------

## Module Actualités

Chaque actualité comportera :

-   titre ;
-   slug ;
-   résumé ;
-   contenu ;
-   image principale ;
-   catégorie ;
-   auteur ;
-   statut (brouillon / publié) ;
-   date de publication.

------------------------------------------------------------------------

# CRUD

Tu développeras les opérations suivantes :

-   ✅ Créer une actualité
-   📖 Lire la liste des actualités
-   ✏️ Modifier une actualité
-   🗑️ Supprimer une actualité

------------------------------------------------------------------------

# Structure recommandée

``` text
src/
├── Controller/
│   └── PostController.php
├── Entity/
│   └── Post.php
├── Form/
│   └── PostType.php
├── Repository/
│   └── PostRepository.php

templates/
├── admin/
│   ├── dashboard.html.twig
│   └── posts/
│       ├── index.html.twig
│       ├── new.html.twig
│       ├── edit.html.twig
│       └── show.html.twig
```

------------------------------------------------------------------------

# Exercices

## Exercice 1

Créer l'entité `Post`.

## Exercice 2

Créer la migration et mettre à jour la base de données.

## Exercice 3

Créer `PostController`.

## Exercice 4

Créer le formulaire `PostType`.

## Exercice 5

Créer la liste des actualités.

## Exercice 6

Créer le formulaire d'ajout.

## Exercice 7

Créer la modification.

## Exercice 8

Créer la suppression avec protection CSRF.

------------------------------------------------------------------------

# Bonnes pratiques

-   Utiliser des routes explicites.
-   Valider les données.
-   Afficher des messages de succès.
-   Utiliser les requêtes préparées via Doctrine.
-   Éviter la duplication de code.

------------------------------------------------------------------------

# Validation

Avant de poursuivre tu devras être capable de :

-   [ ] créer une entité Doctrine ;
-   [ ] créer un CRUD Symfony ;
-   [ ] afficher une liste Twig ;
-   [ ] ajouter, modifier et supprimer une actualité ;
-   [ ] protéger les actions sensibles.

------------------------------------------------------------------------

# Mission

Créer le module **Actualités** complet.

À la fin, envoie-moi :

-   ton entité `Post` ;
-   ton contrôleur ;
-   ton formulaire ;
-   tes vues Twig.

Nous ferons une revue de code comme dans une équipe de développement
avant de passer au module **Agenda**.
