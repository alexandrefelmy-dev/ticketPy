# 🎫 TicketPy

Gestionnaire de tickets de support informatique en ligne de commande, écrit en Python.

TicketPy permet à un technicien de créer, suivre et fermer des tickets d'incidents (« l'imprimante ne répond plus », « pas de connexion wifi »…). Les tickets sont enregistrés automatiquement et sont conservés d'une utilisation à l'autre.

## ✨ Fonctionnalités

- **Créer un ticket** : nom du demandeur, description du problème et priorité (faible, moyenne, élevée)
- **Afficher les tickets** : liste complète avec numéro, demandeur, priorité, statut et description
- **Fermer un ticket** : à partir de son numéro, avec gestion des erreurs (numéro inexistant, saisie invalide, ticket déjà fermé)
- **Sauvegarde automatique** : les tickets sont enregistrés dans un fichier `tickets.json` après chaque modification, puis rechargés au démarrage

## 🖥️ Aperçu

```
=== TicketPy - Support informatique ===
1. Créer un ticket
2. Afficher les tickets
3. Fermer un ticket
4. Quitter
Veuillez choisir une option (1-4) : 2
--- Liste des tickets (2) ---
#1 | Marie | élevée | fermé
    L'imprimante ne répond plus
#2 | Paul | faible | ouvert
    Pas de connexion wifi
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
- les structures de données : listes et dictionnaires
- la gestion des erreurs avec `try` / `except`
- le découpage du code en fonctions (paramètres et `return`)
- la lecture et l'écriture de fichiers JSON

## 🛣️ Évolutions prévues

- [ ] Statistiques (nombre de tickets ouverts / fermés, répartition par priorité)
- [ ] Filtrer les tickets par statut ou par priorité
- [ ] Validation de la priorité saisie
- [ ] Date de création des tickets
- [ ] Passage en programmation orientée objet (classes)
