# Module 4 --- MySQL : créer la base de données du CMS

> **Praful City CMS -- Parcours de formation**

## 🎯 Objectif

Dans ce module, tu vas apprendre à concevoir la base de données du futur
CMS. Toutes les informations (actualités, utilisateurs, événements,
associations...) seront stockées dans MySQL.

------------------------------------------------------------------------

# Compétences visées

À la fin de ce module, tu sauras :

-   Comprendre le rôle d'une base de données relationnelle.
-   Concevoir un schéma de données.
-   Créer une base MySQL.
-   Créer des tables.
-   Définir des clés primaires et étrangères.
-   Utiliser les requêtes SQL de base (CRUD).

------------------------------------------------------------------------

# Pourquoi MySQL ?

Une base de données permet de stocker durablement les informations :

-   utilisateurs ;
-   actualités ;
-   événements ;
-   pages ;
-   services municipaux ;
-   associations ;
-   documents.

Sans base de données, un CMS ne peut pas fonctionner.

------------------------------------------------------------------------

# Les notions à apprendre

## Tables

Une table représente un type de données.

Exemples :

-   users
-   posts
-   events
-   services
-   associations

## Colonnes

Chaque table contient des colonnes :

-   id
-   titre
-   contenu
-   date_creation
-   auteur

## Clés

-   Clé primaire (`PRIMARY KEY`)
-   Clé étrangère (`FOREIGN KEY`)

------------------------------------------------------------------------

# Les requêtes SQL essentielles

Tu apprendras à utiliser :

-   `CREATE DATABASE`
-   `CREATE TABLE`
-   `INSERT`
-   `SELECT`
-   `UPDATE`
-   `DELETE`

------------------------------------------------------------------------

# Projet du module

Créer la première base de données :

**praful_city_cms**

Puis créer les tables :

-   users
-   posts
-   categories
-   events
-   services

------------------------------------------------------------------------

# Exercices

### Exercice 1

Créer la base de données `praful_city_cms`.

### Exercice 2

Créer la table `users` avec :

-   id
-   nom
-   prenom
-   email
-   password
-   role
-   created_at

### Exercice 3

Créer la table `posts` avec :

-   id
-   title
-   slug
-   content
-   published_at
-   author_id

### Exercice 4

Ajouter quelques données de test avec `INSERT`.

### Exercice 5

Afficher les données avec `SELECT`.

------------------------------------------------------------------------

# Schéma simplifié

``` text
users
  │
  └──────┐
         │
posts ───┘

categories ── posts

events

services
```

------------------------------------------------------------------------

# Validation

-   [ ] Base créée
-   [ ] Tables créées
-   [ ] Relations comprises
-   [ ] Données insérées
-   [ ] Requêtes SELECT maîtrisées

------------------------------------------------------------------------

# Arborescence

``` text
praful-city-cms/
├── database/
│   ├── schema.sql
│   └── seed.sql
├── src/
├── public/
└── README.md
```

------------------------------------------------------------------------

# Mission

Créer le fichier `database/schema.sql` contenant les instructions SQL de
création de la base et des premières tables.

Ensuite, envoie-moi ton fichier. Je vérifierai la structure, les types
de données, les clés et je t'expliquerai les améliorations possibles
avant de passer au module PHP.
