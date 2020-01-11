import json
import datetime

if __name__ == '__main__':
    # Load list of dictionnaries
    with open("ID.json", "r" ) as f :
        col_list = json.load(f)

    # Create new user
    col = {}
    col["name"] = input("Prénom : ")
    col["surname"] = input("Nom : ")
    col["entity"] = input("Entité : ")
    col["department"] = input("Département : ")
    col["id"] = input("Identifiant : ")
    col["pass"] = input("Mot de passe : ")
    col["country"] = input("Destination : ")
    col["datein"] = input(datetime.date)
    col["dateout"] = input(datetime.date)
    col["info"] = print("Ce correspondant séjourne à/en/au", col["country"], "du", col["datein"], "au", col["dateout"])

    # Add user to database
    col_list.append(col)

    # Dump updated database
    with open("ID.json","w") as f :
        json.dump(col_list, f)
