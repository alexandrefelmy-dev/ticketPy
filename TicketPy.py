import json

FICHIER = "tickets.json"

def menu():
    print("1. Créer un ticket\n2. Afficher les tickets\n3. Fermer un ticket\n4. Quitter")
    return input("Veuillez choisir une option (1-4) : ").strip()

def creer_ticket(compteur, tickets):
    nom = input("Nom du demandeur : ").strip()
    description = input("Description du problème : ").strip()
    priorite = input("Priorité (faible, moyenne, élevée) : ").strip()
    statut = "ouvert"
    ticket = {
        "id": compteur,
        "nom": nom,
        "description": description,
        "priorite": priorite,
        "statut": statut
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
            print(f"#{ticket['id']} | {ticket['nom']} | {ticket['priorite']} | {ticket['statut']}")
            print(f"    {ticket['description']}")

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
        print("Au revoir !")
        continuer = False

    else:
        print("Option invalide. Veuillez choisir une option valide (1-4).")