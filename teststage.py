import requests
import json
from dateutil import parser

# Fonction qui retourne les états de tous les terrains présents   sur une réponse json donnée
    liste_terrains = []
    # Récupérer la liste des terrains présents sur la réponse json
    for dictionary in reponse_json['slots']:
        if parser.parse(dictionary['date']) == date:
               liste_terrains.append(dictionary['court'])
    # Supprimer les doublants
    liste_terrains = list(set(liste_terrains))
    print(liste_terrains)
    for x in liste_terrains:
        for domain_dict in reponse_json['slots']:
            if parser.parse(domain_dict['date']) == date and x == domain_dict['court']:
                if not domain_dict['present']:
                    print("le terrain n°", x, "est occupé le", domain_dict['date'],
                          "à {}h:{}".format(domain_dict['start'][0:2], domain_dict['start'][2:4]))
                else:
                    print("le terrain n°", x, "est libre le", domain_dict['date'],
                          "à {}h:{}".format(domain_dict['start'][0:2], domain_dict['start'][2:4]))
if __name__ == '__main__':
    # Demander à l'utilisateur la date voulue pour afficher les créneaux
    date_cal = parser.parse(input("Entrer une date voulue pour les créneaux : "))
    # Récupérer la réponse Json pour tennis
    data_json_tennis = requests.get(
        'https://www.eversports.de/widget/api/slot?facilityId=68673&sport=tennis&startDate={}'
        '&courts[]=55076&courts[]=55077&courts[]=55078&courts[]=55079&courts['
        ']=55080&courts[]=55081&courts[]=55082&courts[]=55083'.format(date_cal)).json()
    # Récupérer la réponse Json pour badminton
    data_json_badminton = requests.get(
        'https://www.eversports.de/widget/api/slot?facilityId=68673&sport=badminton&startDate='
        '{}27&courts[]=55092&courts[]=55093&courts[]=55094&courts[]=55095&courts[]=55096&courts['
        ']=55097&courts[]=55098&courts[]=55099'.format(date_cal)).json()
    # Récupérer la réponse Json pour squash
    data_json_squash = requests.get(
        'https://www.eversports.de/widget/api/slot?facilityId=68673&sport=squash&startDate={}'
        '&courts[]=55084&courts[]=55085&courts[]=55086&courts[]=55087&courts[]=55088&courts['
        ']=55089&courts[]=55090&courts[]=55091'.format(date_cal)).json()
    # Récupérer la réponse Json pour tischtennis
    data_json_tischtennis = requests.get(
        'https://www.eversports.de/widget/api/slot?facilityId=68673&sport=tischtennis&startDate'
        '={}&courts[]=55087&courts[]=55091'.format(date_cal)).json()
    print("\n---------------Réponses Json---------------\n")
    # json.dumps : convertir la réponse en format structuré et lisible
    print("\nRéponse Json pour les terrains de tennis :\n")
    print(json.dumps(data_json_tennis, indent=4, sort_keys=True))
    print("\nRéponse Json pour les terrains de badminton :\n")
    print(json.dumps(data_json_badminton, indent=4, sort_keys=True))
    print("\nRéponse Json pour les terrains de squash :\n")
    print(json.dumps(data_json_squash, indent=4, sort_keys=True))
    print("\nRéponse Json pour les terrains de tischtennis :\n")
    print(json.dumps(data_json_tischtennis, indent=4, sort_keys=True))
    print("\n------------Etat des terrains (occupé/libre)------------\n")
    print("\nEtat des terrains de tennis selon la réponse Json:\n")
    # Appel à la fonction pour afficher l'état des terrains
    etats_terrains_selon_reponse_json(data_json_tennis, date_cal)
    print("\nEtat des terrains de badminton selon la réponse Json:\n")
    etats_terrains_selon_reponse_json(data_json_badminton, date_cal)
    print("\nEtat des terrains de squash selon la réponse Json:\n")
    etats_terrains_selon_reponse_json(data_json_squash, date_cal)
    print("\nEtat des terrains de tischtennis selon la réponse Json:\n")
    etats_terrains_selon_reponse_json(data_json_tischtennis, date_cal)


