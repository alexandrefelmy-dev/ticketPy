import json
from datetime import datetime

FICHIER = "tickets.json"
PRIORITES = ("faible", "moyenne", "élevée")
STATUTS = ("ouvert", "fermé")

def menu():
    print("1. Créer un ticket\n2. Afficher les tickets\n3. Fermer un ticket\n4. Statistiques\n5. Filtrer les tickets\n6. Quitter")
    return input("Veuillez choisir une option (1-6) : ").strip()

def maintenant():
    temps = datetime.now()
    return temps.strftime("%d/%m/%Y %H:%M")

class Ticket:
    def __init__(self, ticket_id, nom, description, priorite):
        self.id = ticket_id
        self.nom = nom
        self.description = description
        self.priorite = priorite
        self.statut = "ouvert"
        self.date_creation = maintenant()
        self.date_fermeture = None

    def afficher(self) : 
        print(f"#{self.id} | {self.nom} | {self.priorite} | {self.statut} | {self.date_creation}")
        print(f"    {self.description}")
        if self.statut == "fermé":
            print(f"    🔒 Fermé le {self.date_fermeture}")

    def fermer(self):
        
        if self.statut == "fermé":
            print(f"Ticket #{self.id} déjà fermé")

        else : 
            self.statut = "fermé"
            self.date_fermeture = maintenant()
            print(f"🔒 Ticket #{self.id} fermé !")
            

        

def creer_ticket(compteur, tickets):
    nom = input("Nom du demandeur : ").strip()
    description = input("Description du problème : ").strip()

    priorite = input("Priorité (faible, moyenne, élevée) : ").strip().lower()
    while priorite not in PRIORITES :
        print("❌ Priorité invalide.")
        priorite = input("Choisissez parmi : faible, moyenne, élevée : ").strip().lower()

    statut = "ouvert"
    date_creation = maintenant()
    date_fermeture = None

    ticket = {
        "id": compteur,
        "nom": nom,
        "description": description,
        "priorite": priorite,
        "statut": statut,
        "date_creation": date_creation,
        "date_fermeture": date_fermeture
    }
    tickets.append(ticket)
    print(f"✅ Ticket #{compteur} créé !")
    return compteur + 1

def afficher_tickets(tickets):
    if not tickets:
        print("Aucun ticket disponible.")
    else:
        print(f"--- Liste des tickets ({len(tickets)}) ---")
        for ticket in tickets:
            print(f"#{ticket['id']} | {ticket['nom']} | {ticket['priorite']} | {ticket['statut']} | {ticket['date_creation']}")
            print(f"    {ticket['description']}")
            if ticket["statut"] == "fermé":
                print(f"    🔒 Fermé le {ticket['date_fermeture']}")

def fermer_ticket(tickets):
    try:
        ticket_id = int(input("Numéro du ticket à fermer : ").strip())
        trouve = False
        for ticket in tickets:
            if ticket["id"] == ticket_id: 
                trouve = True
                if ticket["statut"] == "fermé":
                    print(f"Ticket #{ticket_id} déjà fermé")

                else : 
                    ticket["statut"] = "fermé"
                    ticket["date_fermeture"] = maintenant()
                    print(f"🔒 Ticket #{ticket_id} fermé !")
                break

        if not trouve :
            print("Aucun ticket avec ce numéro")

    except ValueError:
        print("Veuillez entrer un nombre")

def sauvegarder_tickets(tickets):
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(tickets, f, ensure_ascii=False, indent=2)

def charger_tickets():
    try :
        with open(FICHIER, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def afficher_statistiques(tickets):
    print("--- Statistiques ---")
    if not len(tickets) : 
        print("Aucun ticket pour le moment.")
    else :
        print(f"Total : {len(tickets)} tickets")
        nb_tickets_ouvert = len([ticket for ticket in tickets if ticket["statut"] == "ouvert"])
        nb_tickets_ferme = len([ticket for ticket in tickets if ticket["statut"] == "fermé"])
        print(f"Ouverts : {nb_tickets_ouvert} | Fermés : {nb_tickets_ferme}")
        for priorite in PRIORITES:
            nb = len([ticket for ticket in tickets if ticket["priorite"] == priorite])
            print(f"{priorite} : {nb} | ", end="")
        print()

def filtrer_tickets(tickets):
    filtre = input("Filtrer par : 1. Statut  2. Priorité\nVotre choix : ").strip()

    if filtre == "1":
        statut_choisi = input("Statut (ouvert, fermé) : ").strip().lower()
        while statut_choisi not in STATUTS:
            print("❌ Statut invalide.")
            statut_choisi = input("Statut (ouvert, fermé) : ").strip().lower()
        resultat_statut = [ticket for ticket in tickets if ticket["statut"] == statut_choisi]
        afficher_tickets(resultat_statut)

    elif filtre == "2":
        priorite_choisie = input("Priorite (faible, moyenne, élevée) : ").strip().lower()
        while priorite_choisie not in PRIORITES:
            print("❌ Priorité invalide.")
            priorite_choisie = input("Priorité (faible, moyenne, élevée) : ").strip().lower()
        resultat_priorite = [ticket for ticket in tickets if ticket["priorite"] == priorite_choisie]
        afficher_tickets(resultat_priorite)

    else :
        print("veuillez choisir 1 ou 2")
        filtrer_tickets(tickets)

    


continuer = True
tickets = charger_tickets()
compteur = len(tickets) + 1

print("=== TicketPy - Support informatique ===")

while continuer:

    choix = menu()

    if choix == "1":
        compteur = creer_ticket(compteur, tickets)
        sauvegarder_tickets(tickets)
        
    elif choix == "2":
        afficher_tickets(tickets)
    
    elif choix == "3":
        fermer_ticket(tickets)
        sauvegarder_tickets(tickets)

    elif choix == "4":
        afficher_statistiques(tickets)

    elif choix == "5":
        filtrer_tickets(tickets)
        
    elif choix == "6":
        print("Au revoir !")
        continuer = False

    else:
        print("Option invalide. Veuillez choisir une option valide (1-6).")






