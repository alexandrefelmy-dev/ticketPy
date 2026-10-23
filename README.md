# 🎫 TicketPy

Gestionnaire de tickets de support informatique en ligne de commande, écrit en Python.

TicketPy permet à un technicien de créer, suivre, fermer et analyser des tickets
d'incidents (« l'imprimante ne répond plus », « pas de connexion wifi »…). Les
tickets sont enregistrés automatiquement et sont conservés d'une utilisation à
l'autre.

## ✨ Fonctionnalités

- **Créer un ticket** : nom du demandeur, description du problème et priorité
  (faible, moyenne, élevée), avec validation de la saisie
- **Afficher les tickets** : liste complète avec numéro, demandeur, priorité,
  statut, date de création et description
- **Fermer un ticket** : à partir de son numéro, avec enregistrement de la date
  de fermeture et gestion des erreurs (numéro inexistant, saisie invalide,
  ticket déjà fermé)
- **Horodatage** : chaque ticket conserve sa date de création et, une fois
  fermé, sa date de fermeture (format `JJ/MM/AAAA HH:MM`)
- **Statistiques** : nombre total de tickets, répartition ouverts / fermés et
  par priorité
- **Filtrer les tickets** : par statut (ouvert, fermé) ou par priorité
- **Sauvegarde automatique** : les tickets sont enregistrés dans un fichier
  `tickets.json` après chaque modification, puis rechargés au démarrage

## 🖥️ Aperçu

```text
=== TicketPy - Support informatique ===
1. Créer un ticket
2. Afficher les tickets
3. Fermer un ticket
4. Statistiques
5. Filtrer les tickets
6. Quitter
Veuillez choisir une option (1-6) : 2
--- Liste des tickets (2) ---
#1 | Marie | élevée | fermé | 21/10/2026 09:14
    L'imprimante ne répond plus
    🔒 Fermé le 21/10/2026 10:02
#2 | Lucas | moyenne | ouvert | 22/10/2026 14:37
    Pas de connexion wifi
Veuillez choisir une option (1-6) : 4
--- Statistiques ---
Total : 2 tickets
Ouverts : 1 | Fermés : 1
faible : 0 | moyenne : 1 | élevée : 1 |
```

## 🚀 Installation et lancement

**Prérequis :** Python 3 (aucune bibliothèque externe nécessaire)

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/alexandrefelmy-dev/TicketPy.git
   cd TicketPy
   ```

2. Lancer le programme :

   ```bash
   python TicketPy.py
   ```

Le fichier `tickets.json` est créé automatiquement lors de la création du
premier ticket.

## 🗂️ Organisation du code

- **`Ticket`** : classe représentant un ticket (numéro, demandeur, description,
  priorité, statut, dates). Elle sait s'afficher (`afficher`), se fermer
  (`fermer`) et se convertir en dictionnaire pour la sauvegarde (`vers_dict`)
- **`depuis_dict`** : reconstruit un objet `Ticket` à partir des données JSON
- **Fonctions du menu** : `creer_ticket`, `afficher_tickets`, `fermer_ticket`,
  `afficher_statistiques`, `filtrer_tickets`
- **Persistance** : `sauvegarder_tickets` et `charger_tickets` gèrent le
  fichier `tickets.json`
- **`main`** : boucle principale qui affiche le menu et appelle la bonne action

## 🧠 Notions mises en pratique

Ce projet a été réalisé dans le cadre de mon apprentissage de Python. Il m'a
permis de travailler :

- les boucles (`while`, `for`) et les conditions
- les structures de données : listes, dictionnaires et tuples
- les compréhensions de liste pour filtrer et compter
- la validation des saisies utilisateur
- la gestion des erreurs avec `try` / `except`
- le découpage du code en fonctions (paramètres et `return`)
- la lecture et l'écriture de fichiers JSON
- la programmation orientée objet : classe, constructeur `__init__`,
  attributs et méthodes
- la sérialisation d'objets (conversion objet ↔ dictionnaire)
- la manipulation des dates avec le module `datetime`

## 🛣️ Évolutions

- [x] Statistiques (nombre de tickets ouverts / fermés, répartition par priorité)
- [x] Filtrer les tickets par statut ou par priorité
- [x] Validation de la priorité saisie
- [x] Date de création et de fermeture des tickets
- [x] Passage en programmation orientée objet (classe `Ticket`)

## ✅ Statut du projet

Projet terminé : toutes les fonctionnalités prévues sont implémentées.
