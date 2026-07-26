# Module 6 --- Symfony : construire un CMS professionnel

> **Praful City CMS -- Parcours de formation**

## 🎯 Objectif

Dans ce module, tu vas découvrir **Symfony**, le framework PHP utilisé
dans de nombreux projets professionnels.

L'objectif est de transformer le mini back-office développé en PHP natif
en une application moderne, structurée et évolutive.

------------------------------------------------------------------------

# Pourquoi Symfony ?

Symfony apporte :

-   une architecture claire (MVC) ;
-   un système de routage ;
-   un moteur de templates (Twig) ;
-   un ORM (Doctrine) ;
-   une gestion avancée de la sécurité ;
-   des formulaires puissants ;
-   des commandes en ligne de commande ;
-   un écosystème professionnel.

------------------------------------------------------------------------

# Compétences visées

À la fin du module, tu sauras :

-   Installer Symfony.
-   Comprendre l'architecture MVC.
-   Créer des routes.
-   Créer des contrôleurs.
-   Utiliser Twig.
-   Créer des entités Doctrine.
-   Générer des migrations.
-   Créer des formulaires.
-   Mettre en place une authentification.
-   Organiser proprement un projet.

------------------------------------------------------------------------

# Architecture Symfony

``` text
src/
├── Controller/
├── Entity/
├── Form/
├── Repository/
├── Security/
└── Service/

templates/
config/
public/
migrations/
var/
vendor/
```

------------------------------------------------------------------------

# Les notions à apprendre

## Routing

Créer des URL propres :

-   /
-   /actualites
-   /agenda
-   /services

------------------------------------------------------------------------

## Contrôleurs

Chaque page est pilotée par un contrôleur.

Exemple :

-   HomeController
-   NewsController
-   EventController
-   ServiceController

------------------------------------------------------------------------

## Twig

Twig permet de séparer :

-   la logique (PHP)
-   l'affichage (HTML)

Tu apprendras :

-   les variables
-   les boucles
-   les conditions
-   l'héritage de templates
-   les composants réutilisables

------------------------------------------------------------------------

## Doctrine ORM

Créer des entités :

-   User
-   Post
-   Event
-   Service
-   Association

Puis :

-   migrations
-   relations
-   repository

------------------------------------------------------------------------

## Formulaires Symfony

Créer :

-   formulaire d'actualité
-   formulaire d'événement
-   formulaire de connexion

------------------------------------------------------------------------

## Sécurité

Découvrir :

-   authentification
-   rôles
-   contrôle d'accès
-   hashage des mots de passe
-   CSRF

------------------------------------------------------------------------

# Projet du module

Créer la première version du back-office Symfony avec :

-   page d'accueil
-   connexion
-   tableau de bord
-   liste des actualités
-   ajout d'une actualité

------------------------------------------------------------------------

# Exercices

## Exercice 1

Installer Symfony CLI.

## Exercice 2

Créer un nouveau projet Symfony.

## Exercice 3

Lancer le serveur local.

## Exercice 4

Créer un contrôleur `HomeController`.

## Exercice 5

Créer une vue Twig affichant :

> Bienvenue sur Praful City CMS

## Exercice 6

Créer l'entité `Post`.

## Exercice 7

Créer la première migration.

------------------------------------------------------------------------

# Validation

Avant de passer au module suivant, tu devras être capable de :

-   [ ] expliquer le modèle MVC ;
-   [ ] créer une route ;
-   [ ] créer un contrôleur ;
-   [ ] afficher une vue Twig ;
-   [ ] créer une entité Doctrine ;
-   [ ] lancer une migration.

------------------------------------------------------------------------

# Mission

Créer un nouveau projet Symfony et afficher une page d'accueil
fonctionnelle avec Twig.

Ensuite, envoie-moi :

-   l'arborescence du projet ;
-   ton contrôleur ;
-   ton template Twig.

Je vérifierai ton code, je t'expliquerai les bonnes pratiques et nous
construirons ensemble le véritable **Praful City CMS**.
