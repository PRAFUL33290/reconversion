# Praful City CMS — Cahier de projet et parcours d’apprentissage

## 1. Objectif du projet

Créer progressivement un **CMS pour collectivités** inspiré des besoins réels d’un site municipal.

Ce projet servira à apprendre et pratiquer :

- HTML5
- CSS3
- JavaScript
- PHP 8
- MySQL
- Symfony
- Git et GitHub
- Accessibilité RGAA
- RGPD
- SEO
- Sécurité web
- Déploiement et maintenance

Le résultat final devra permettre de présenter un projet concret dans un portfolio pour viser un poste de :

- webmaster en mairie ;
- chargé de communication numérique ;
- gestionnaire de site institutionnel ;
- intégrateur ou développeur web junior ;
- assistant communication et numérique.

---

## 2. Nom du projet

**Praful City CMS**

Nom du site de démonstration :

> Ville de Nova

Ce nom peut être remplacé plus tard.

---

## 3. Principe pédagogique

Le site sera développé étape par étape.

Pour chaque étape :

1. comprendre la notion ;
2. voir un exemple simple ;
3. reproduire l’exemple ;
4. réaliser un exercice ;
5. intégrer la fonctionnalité au CMS ;
6. faire relire et corriger le code ;
7. valider avant de passer au module suivant.

Le code doit rester compréhensible.  
Aucune fonctionnalité ne doit être ajoutée sans explication.

---

# 4. Stack technique principale

## Front-end

- HTML5
- CSS3
- JavaScript natif
- Twig avec Symfony

## Back-end

- PHP 8
- Symfony
- Doctrine ORM

## Base de données

- MySQL

## Outils complémentaires

- Git
- GitHub
- Composer
- Symfony CLI
- VS Code
- phpMyAdmin ou Adminer
- Leaflet
- OpenStreetMap
- FullCalendar
- TinyMCE ou CKEditor
- Chart.js
- PHPMailer ou Symfony Mailer
- Brevo pour les e-mails et alertes SMS

---

# 5. Ordre d’apprentissage

## Bloc 1 — HTML

Objectifs :

- comprendre la structure d’une page ;
- utiliser les balises sémantiques ;
- créer une navigation ;
- structurer un contenu municipal ;
- créer des formulaires accessibles ;
- intégrer des images, vidéos et documents.

Livrables :

- page d’accueil ;
- page actualités ;
- fiche service municipal ;
- fiche association ;
- page contact.

---

## Bloc 2 — CSS

Objectifs :

- maîtriser les sélecteurs ;
- utiliser Flexbox ;
- utiliser CSS Grid ;
- créer une interface responsive ;
- utiliser des variables CSS ;
- gérer les états hover, focus et active ;
- créer une charte graphique cohérente.

Livrables :

- en-tête responsive ;
- grille d’actualités ;
- cartes de services ;
- tableau de bord ;
- formulaires ;
- pied de page institutionnel.

---

## Bloc 3 — JavaScript

Objectifs :

- comprendre les variables ;
- utiliser les conditions et boucles ;
- créer des fonctions ;
- manipuler le DOM ;
- écouter des événements ;
- charger des données JSON ;
- utiliser Fetch API ;
- créer des filtres dynamiques.

Livrables :

- menu mobile ;
- filtres d’actualités ;
- recherche instantanée ;
- carte interactive ;
- calendrier ;
- alertes et confirmations.

---

## Bloc 4 — MySQL

Objectifs :

- comprendre une base de données ;
- créer des tables ;
- utiliser les clés primaires et étrangères ;
- écrire des requêtes SQL ;
- comprendre les relations ;
- organiser les données du CMS.

Tables principales :

- users
- roles
- pages
- posts
- categories
- events
- publications
- services
- associations
- equipments
- elected_members
- council_reports
- procedures
- procedure_submissions
- sms_subscribers
- media
- settings

---

## Bloc 5 — PHP

Objectifs :

- comprendre les variables et tableaux ;
- traiter les formulaires ;
- utiliser les sessions ;
- se connecter à MySQL ;
- créer un CRUD ;
- sécuriser les entrées ;
- gérer les fichiers ;
- comprendre la programmation orientée objet.

Mini-projet :

Créer un petit back-office en PHP natif avant Symfony.

Fonctionnalités :

- connexion ;
- déconnexion ;
- liste des actualités ;
- ajout ;
- modification ;
- suppression ;
- publication.

---

## Bloc 6 — Symfony

Objectifs :

- comprendre MVC ;
- créer des routes ;
- créer des contrôleurs ;
- utiliser Twig ;
- utiliser Doctrine ;
- créer des entités ;
- utiliser les migrations ;
- créer des formulaires ;
- gérer les utilisateurs ;
- sécuriser les accès ;
- créer des services ;
- créer une API.

---

# 6. Fonctionnalités finales du CMS

## 6.1 Tableau de bord

Afficher :

- nombre d’actualités ;
- nombre d’événements ;
- nombre de publications ;
- nombre d’associations ;
- nombre de démarches reçues ;
- derniers contenus modifiés ;
- statistiques ;
- raccourcis de création.

---

## 6.2 Authentification et utilisateurs

Rôles envisagés :

- Administrateur
- Communication
- Rédacteur
- Agent
- Élu

Fonctionnalités :

- connexion ;
- déconnexion ;
- mot de passe sécurisé ;
- permissions ;
- profils ;
- historique des actions.

---

## 6.3 Gestion des pages

Fonctionnalités :

- créer une page ;
- modifier une page ;
- supprimer une page ;
- enregistrer en brouillon ;
- publier ;
- programmer ;
- définir un titre SEO ;
- définir une méta-description ;
- choisir une image ;
- organiser le menu.

---

## 6.4 Actualités

Champs :

- titre ;
- slug ;
- résumé ;
- contenu ;
- image principale ;
- catégorie ;
- auteur ;
- statut ;
- date de publication ;
- mise en avant ;
- SEO.

---

## 6.5 Agenda

Champs :

- titre ;
- description ;
- date de début ;
- date de fin ;
- heure ;
- lieu ;
- tarif ;
- lien d’inscription ;
- organisateur ;
- image ;
- catégorie.

Fonctionnalités :

- vue calendrier ;
- filtres ;
- export iCal ;
- événements passés ;
- événements à venir.

---

## 6.6 Publications

Exemples :

- magazine municipal ;
- guide pratique ;
- délibération ;
- compte-rendu ;
- document budgétaire ;
- dossier de concertation.

Fonctionnalités :

- dépôt de PDF ;
- classement ;
- catégories ;
- recherche ;
- année ;
- téléchargement ;
- archivage.

---

## 6.7 Grands projets

Champs :

- titre ;
- résumé ;
- description ;
- état d’avancement ;
- date ;
- budget ;
- galerie ;
- documents ;
- localisation ;
- contact.

---

## 6.8 Marchés publics

Champs :

- référence ;
- intitulé ;
- description ;
- date d’ouverture ;
- date limite ;
- statut ;
- documents ;
- lien externe ;
- contact.

Attention :

Le CMS ne remplacera pas forcément une plateforme officielle de marchés publics.  
Il pourra servir à informer et rediriger vers la plateforme réglementaire.

---

## 6.9 Services municipaux

Exemples :

- État civil
- Urbanisme
- Enfance
- Jeunesse
- Culture
- Sports
- CCAS
- Police municipale

Champs :

- nom ;
- description ;
- horaires ;
- téléphone ;
- e-mail ;
- adresse ;
- responsable ;
- démarches associées ;
- documents ;
- carte.

---

## 6.10 Annuaire des associations

Champs :

- nom ;
- catégorie ;
- description ;
- logo ;
- adresse ;
- téléphone ;
- e-mail ;
- site internet ;
- réseaux sociaux ;
- horaires ;
- responsable ;
- coordonnées géographiques.

Fonctionnalités :

- recherche ;
- filtre ;
- classement alphabétique ;
- carte ;
- formulaire de mise à jour.

---

## 6.11 Carte interactive des équipements

Technologies :

- Leaflet
- OpenStreetMap

Équipements :

- mairie ;
- écoles ;
- médiathèque ;
- salles municipales ;
- équipements sportifs ;
- parcs ;
- parkings ;
- services publics.

Fonctionnalités :

- marqueurs ;
- catégories ;
- filtres ;
- fiches ;
- itinéraire ;
- géolocalisation.

---

## 6.12 Organigramme des élus

Champs :

- nom ;
- prénom ;
- fonction ;
- délégation ;
- photo ;
- biographie ;
- e-mail ;
- ordre d’affichage.

Organisation :

- maire ;
- adjoints ;
- conseillers délégués ;
- conseillers municipaux.

---

## 6.13 Comptes-rendus des conseils municipaux

Champs :

- date ;
- titre ;
- ordre du jour ;
- procès-verbal ;
- délibérations ;
- vidéos ;
- documents téléchargeables.

Fonctionnalités :

- classement par année ;
- moteur de recherche ;
- filtres ;
- téléchargement ;
- archivage.

---

## 6.14 Démarches en ligne

Exemples :

- demande d’acte ;
- réservation de salle ;
- signalement de voirie ;
- demande de rendez-vous ;
- demande de contact ;
- inscription à un événement ;
- dépôt de dossier.

Fonctionnalités :

- formulaires ;
- pièces jointes ;
- accusé de réception ;
- numéro de dossier ;
- statut ;
- suivi ;
- notification e-mail ;
- export ;
- suppression selon durée de conservation.

Statuts :

- Reçue
- En cours
- En attente
- Traitée
- Refusée
- Clôturée

---

## 6.15 Alertes SMS

Fonctionnalités :

- inscription ;
- confirmation ;
- désinscription ;
- listes thématiques ;
- envoi ciblé ;
- historique ;
- consentement RGPD.

Catégories possibles :

- urgences ;
- travaux ;
- événements ;
- météo ;
- circulation ;
- écoles.

---

## 6.16 Médiathèque

Fonctionnalités :

- ajout de fichiers ;
- images ;
- PDF ;
- vidéos ;
- recherche ;
- dossiers ;
- texte alternatif ;
- compression ;
- redimensionnement ;
- contrôle des formats ;
- suppression sécurisée.

---

## 6.17 Moteur de recherche

Recherche dans :

- pages ;
- actualités ;
- événements ;
- associations ;
- services ;
- publications ;
- comptes-rendus.

Fonctionnalités :

- recherche globale ;
- filtres ;
- suggestions ;
- surlignage ;
- tri par pertinence.

---

## 6.18 Statistiques

Indicateurs :

- contenus publiés ;
- démarches reçues ;
- documents téléchargés ;
- recherches effectuées ;
- pages les plus consultées ;
- abonnés SMS ;
- événements à venir.

---

# 7. Architecture prévue avec Symfony

```text
praful-city-cms/
├── assets/
│   ├── controllers/
│   ├── images/
│   ├── scripts/
│   └── styles/
├── config/
├── migrations/
├── public/
│   ├── uploads/
│   └── index.php
├── src/
│   ├── Controller/
│   ├── Entity/
│   ├── Form/
│   ├── Repository/
│   ├── Security/
│   └── Service/
├── templates/
│   ├── admin/
│   ├── front/
│   ├── components/
│   └── base.html.twig
├── tests/
├── translations/
├── .env
├── composer.json
└── README.md
```

---

# 8. Première version minimale

La première version ne contiendra que :

- page d’accueil ;
- actualités ;
- agenda ;
- services municipaux ;
- connexion administrateur ;
- tableau de bord ;
- CRUD actualités ;
- CRUD événements ;
- CRUD services.

Objectif :

Obtenir rapidement un CMS fonctionnel avant d’ajouter les modules avancés.

---

# 9. Découpage en versions

## Version 0.1

- maquette HTML ;
- page d’accueil ;
- navigation ;
- actualités statiques ;
- agenda statique.

## Version 0.2

- base MySQL ;
- PHP natif ;
- connexion ;
- CRUD actualités.

## Version 0.3

- installation Symfony ;
- entités ;
- Doctrine ;
- Twig ;
- formulaires.

## Version 0.4

- utilisateurs ;
- rôles ;
- sécurité ;
- dashboard.

## Version 0.5

- actualités ;
- agenda ;
- pages ;
- services ;
- médias.

## Version 0.6

- associations ;
- publications ;
- conseils municipaux ;
- organigramme.

## Version 0.7

- carte interactive ;
- recherche ;
- démarches en ligne.

## Version 0.8

- SMS ;
- statistiques ;
- notifications.

## Version 0.9

- RGAA ;
- RGPD ;
- SEO ;
- sécurité ;
- performances.

## Version 1.0

- tests ;
- documentation ;
- déploiement ;
- démonstration ;
- portfolio.

---

# 10. Règles de développement

- Utiliser un code lisible.
- Nommer clairement les variables.
- Commenter uniquement lorsque cela aide à comprendre.
- Ne jamais stocker un mot de passe en clair.
- Utiliser les protections CSRF.
- Valider toutes les données.
- Échapper les sorties HTML.
- Vérifier les fichiers envoyés.
- Utiliser Git à chaque étape importante.
- Faire un commit par fonctionnalité.
- Tester sur mobile.
- Respecter les niveaux de titres.
- Ajouter des labels aux formulaires.
- Prévoir la navigation clavier.
- Ajouter des textes alternatifs aux images.
- Séparer le contenu, le style et la logique.

---

# 11. Convention Git

Branches :

```text
main
develop
feature/nom-fonctionnalite
fix/nom-correction
```

Exemples de commits :

```text
feat: ajoute le module actualités
feat: crée le formulaire événement
fix: corrige le menu mobile
style: améliore le tableau de bord
docs: complète le guide d’installation
refactor: simplifie le contrôleur des pages
```

---

# 12. Sécurité à apprendre

- injection SQL ;
- XSS ;
- CSRF ;
- validation serveur ;
- contrôle des droits ;
- hachage des mots de passe ;
- upload sécurisé ;
- limitation des tentatives ;
- journaux ;
- sauvegardes ;
- mises à jour ;
- variables d’environnement.

---

# 13. Accessibilité RGAA

À appliquer dès le début :

- HTML sémantique ;
- titres hiérarchisés ;
- contrastes suffisants ;
- focus visible ;
- formulaires labellisés ;
- navigation clavier ;
- textes alternatifs ;
- messages d’erreur clairs ;
- contenu compréhensible ;
- liens explicites ;
- pas d’information transmise uniquement par la couleur.

---

# 14. RGPD

Prévoir :

- consentement ;
- finalité ;
- minimisation des données ;
- durée de conservation ;
- droit de suppression ;
- mentions d’information ;
- sécurité ;
- politique de confidentialité ;
- journalisation limitée ;
- gestion des abonnements SMS ;
- suppression automatique des anciens dossiers.

---

# 15. SEO

Prévoir :

- balise title ;
- méta-description ;
- URL propre ;
- titres H1 à H6 ;
- sitemap ;
- robots.txt ;
- canonical ;
- Open Graph ;
- données structurées ;
- images optimisées ;
- performances ;
- maillage interne.

---

# 16. Déploiement

À apprendre :

- hébergement PHP ;
- base MySQL ;
- nom de domaine ;
- HTTPS ;
- variables d’environnement ;
- installation Composer ;
- migrations ;
- cache ;
- permissions ;
- sauvegardes ;
- restauration ;
- maintenance.

---

# 17. Portfolio final

Le portfolio devra présenter :

- le contexte ;
- le besoin ;
- la cible ;
- la maquette ;
- les technologies ;
- l’architecture ;
- les principales fonctionnalités ;
- les difficultés rencontrées ;
- les solutions ;
- les règles RGAA ;
- les règles RGPD ;
- les tests ;
- les captures ;
- une vidéo de démonstration ;
- le dépôt GitHub ;
- une démo en ligne.

---

# 18. Première mission

## Mission 1 — Créer la base du site

Créer les fichiers :

```text
index.html
actualites.html
agenda.html
services.html
contact.html
css/style.css
js/app.js
images/
```

## Contenu attendu

La page d’accueil doit contenir :

- un en-tête ;
- un logo texte ;
- un menu ;
- une bannière principale ;
- trois accès rapides ;
- trois actualités ;
- trois événements ;
- une section services ;
- un appel à l’action ;
- un pied de page.

## Compétences travaillées

- structure HTML ;
- balises sémantiques ;
- liens ;
- images ;
- listes ;
- sections ;
- classes CSS ;
- organisation des fichiers.

---

# 19. Fonctionnement avec le tuteur

Pour chaque séance, utiliser cette structure :

```text
Cours du jour :
Objectif :
Notions :
Exemple :
Exercice :
Mission projet :
Erreurs rencontrées :
Corrections :
Ce que j’ai appris :
Prochaine étape :
```

Lorsque je demande de l’aide, le tuteur doit :

1. expliquer simplement ;
2. éviter de donner toute la solution immédiatement ;
3. proposer un indice ;
4. corriger mon code ;
5. expliquer mes erreurs ;
6. me faire refaire l’exercice ;
7. valider lorsque la notion est comprise.

---

# 20. Commande de démarrage

Message à envoyer au tuteur :

> Nous commençons Praful City CMS. Lance la Mission 1. Explique-moi d’abord la structure HTML d’une page municipale, puis donne-moi un exercice progressif. Ne me donne pas tout le code immédiatement : guide-moi comme un formateur.

---

## Statut du projet

```text
Projet : Praful City CMS
Niveau : Débutant progressif
Étape actuelle : Mission 1
Statut : À commencer
```
