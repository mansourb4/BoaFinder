import json

with open("ID.json", "r" ) as f :
    col_list = json.load(f)

def pays(pays_input, col_list) :
    output_user = []
    for user in col_list :
        if user["country"] == pays_input :
            output_user.append(user)
    print(output_user)
pays(input("Entrez un pays : "),col_list)

def nom(nom_input, col_list) :
    output_user = []
    for user in col_list :
        if user["surname"] == nom_input :
            output_user.append(user)
    print(output_user)
nom(input("Entrez un nom : "),col_list)

def departement(departement_input, col_list) :
    output_user = []
    for user in col_list :
        if user["department"] == departement_input :
            output_user.append(user)
    print(output_user)
departement(input("Entrez un département : "),col_list)
