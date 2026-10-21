# 🎫 TicketPy

Gestionnaire de tickets de support informatique en ligne de commande, écrit en Python.

TicketPy permet à un technicien de créer, suivre, fermer et analyser des tickets d'incidents (« l'imprimante ne répond plus », « pas de connexion wifi »…). Les tickets sont enregistrés automatiquement et sont conservés d'une utilisation à l'autre.

## ✨ Fonctionnalités

- **Créer un ticket** : nom du demandeur, description du problème et priorité (faible, moyenne, élevée), avec validation de la saisie
- **Afficher les tickets** : liste complète avec numéro, demandeur, priorité, statut et description
- **Fermer un ticket** : à partir de son numéro, avec gestion des erreurs (numéro inexistant, saisie invalide, ticket déjà fermé)
- **Statistiques** : nombre total de tickets, répartition ouverts / fermés et par priorité
- **Filtrer les tickets** : par statut (ouvert, fermé) ou par priorité
- **Sauvegarde automatique** : les tickets sont enregistrés dans un fichier `tickets.json` après chaque modification, puis rechargés au démarrage

## 🖥️ Aperçu

```
=== TicketPy - Support informatique ===
1. Créer un ticket
2. Afficher les tickets
3. Fermer un ticket
4. Statistiques
5. Filtrer les tickets
6. Quitter
Veuillez choisir une option (1-6) : 4
--- Statistiques ---
Total : 5 tickets
Ouverts : 3 | Fermés : 2
faible : 2 | moyenne : 1 | élevée : 2 |
```

## 🚀 Installation et lancement

**Prérequis :** Python 3 (aucune bibliothèque externe nécessaire)

1. Cloner le dépôt :
   ```
   git clone https://github.com/alexandrefelmy-dev/TicketPy.git
   cd TicketPy
   ```
2. Lancer le programme :
   ```
   python TicketPy.py
   ```

Le fichier `tickets.json` est créé automatiquement lors de la création du premier ticket.

## 🧠 Notions mises en pratique

Ce projet a été réalisé dans le cadre de mon apprentissage de Python. Il m'a permis de travailler :

- les boucles (`while`, `for`) et les conditions
- les structures de données : listes, dictionnaires et tuples
- les compréhensions de liste pour filtrer et compter
- la validation des saisies utilisateur
- la gestion des erreurs avec `try` / `except`
- le découpage du code en fonctions (paramètres et `return`)
- la lecture et l'écriture de fichiers JSON

## 🛣️ Évolutions prévues

- [x] Statistiques (nombre de tickets ouverts / fermés, répartition par priorité)
- [x] Filtrer les tickets par statut ou par priorité
- [x] Validation de la priorité saisie
- [ ] Date de création des tickets
- [ ] Passage en programmation orientée objet (classes)