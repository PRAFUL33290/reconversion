# Module 5 --- PHP : créer le premier back-office

> **Praful City CMS -- Parcours de formation**

## 🎯 Objectif

Dans ce module, tu vas découvrir **PHP**, le langage qui permettra de
donner vie au CMS. Grâce à PHP, les pages deviendront dynamiques, les
données seront récupérées depuis MySQL et les utilisateurs pourront se
connecter à un espace d'administration.

------------------------------------------------------------------------

# Compétences visées

À la fin de ce module, tu seras capable de :

-   Comprendre le rôle de PHP.
-   Installer un environnement de développement (PHP + serveur local).
-   Créer des pages PHP.
-   Utiliser les variables, conditions, boucles et fonctions.
-   Traiter un formulaire HTML.
-   Se connecter à une base MySQL avec PDO.
-   Créer un premier CRUD.
-   Comprendre les bases de la programmation orientée objet (POO).

------------------------------------------------------------------------

# Pourquoi PHP ?

PHP est exécuté **sur le serveur**.

Il permet notamment de :

-   afficher des données provenant de MySQL ;
-   gérer les connexions utilisateurs ;
-   enregistrer des formulaires ;
-   générer des pages dynamiques ;
-   sécuriser l'accès au back-office.

------------------------------------------------------------------------

# Les notions à apprendre

## Variables

-   `$nom`
-   `$email`
-   `$utilisateur`

## Structures de contrôle

-   `if`
-   `else`
-   `switch`
-   `foreach`
-   `while`

## Fonctions

Créer et réutiliser des fonctions.

## Tableaux

-   tableaux indexés ;
-   tableaux associatifs.

------------------------------------------------------------------------

# Se connecter à MySQL

Tu découvriras :

-   PDO ;
-   les requêtes préparées ;
-   la gestion des erreurs ;
-   les bonnes pratiques de sécurité.

------------------------------------------------------------------------

# Projet du module

Créer un mini back-office avec :

-   page de connexion ;
-   tableau de bord ;
-   liste des actualités ;
-   ajout d'une actualité ;
-   modification ;
-   suppression.

⚠️ L'objectif est de comprendre le fonctionnement en PHP natif avant de
passer à Symfony.

------------------------------------------------------------------------

# Exercices

## Exercice 1

Créer :

``` text
public/index.php
```

Afficher :

``` php
<?php
echo "Bonjour Ville de Nova !";
```

------------------------------------------------------------------------

## Exercice 2

Créer une variable contenant ton prénom et l'afficher.

------------------------------------------------------------------------

## Exercice 3

Créer une boucle qui affiche les jours de la semaine.

------------------------------------------------------------------------

## Exercice 4

Créer un formulaire HTML envoyé vers une page PHP.

Afficher les données reçues.

------------------------------------------------------------------------

## Exercice 5

Créer le fichier :

``` text
config/database.php
```

Y préparer la connexion PDO (nous la compléterons ensemble).

------------------------------------------------------------------------

# Arborescence

``` text
praful-city-cms/
├── config/
│   └── database.php
├── public/
│   ├── index.php
│   ├── login.php
│   └── dashboard.php
├── src/
├── templates/
└── database/
```

------------------------------------------------------------------------

# Les erreurs à éviter

-   Mélanger HTML et PHP sans organisation.
-   Utiliser `mysqli` au lieu de PDO pour les nouveaux projets.
-   Construire des requêtes SQL avec des chaînes de caractères.
-   Stocker les mots de passe en clair.
-   Faire confiance aux données envoyées par un formulaire.

------------------------------------------------------------------------

# Validation

Avant de passer au module Symfony, tu devras être capable de :

-   [ ] créer une page PHP ;
-   [ ] utiliser des variables et des fonctions ;
-   [ ] traiter un formulaire ;
-   [ ] comprendre PDO ;
-   [ ] afficher des données depuis MySQL.

------------------------------------------------------------------------

# Mission

Créer les fichiers :

``` text
public/index.php
public/login.php
config/database.php
```

Puis envoie-moi ton code.

Je vérifierai :

1.  la structure ;
2.  la lisibilité ;
3.  les bonnes pratiques ;
4.  la sécurité ;
5.  les pistes d'amélioration.

Nous construirons ensuite ensemble le premier véritable back-office de
**Praful City CMS**.
