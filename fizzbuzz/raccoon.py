# Hello :) C'est Const de la Nightoo !
# Voila, ce bout de code ne sert strictement a rien !
# Enfin, il te permet de poser des questions a mister raccoon (mais il est un peut bete)
# J'espere que tu aimera discuter avec lui (Il attend qu'on lui réponde maintenant! :p)

import random
from flask import Blueprint, Flask, request, jsonify, make_response

raccoon_api = Blueprint('raccoon_api', __name__)


@raccoon_api.route('/raccoon', methods=['GET'])
def get_raccoon():
    return "Coucou! C'est raccoon! J'aime fouiller les poubelles :) Tu peux me poser des questions:" \
        "<ul>" \
            "<li>/raccoon/onmangequand</li>" \
            "<li>/raccoon/estcequeraccoonafaim</li>" \
            "<li>/raccoon/cestquandquonboit</li>" \
            "<li>/raccoon/onsortou</li>" \
            "<li>/raccoon/quiafaitcacadanslabruyere</li>" \
            "<li>/raccoon/ditmoicestquoilemeilleursonaumonde</li>" \
            "<li>/raccoon/quiatoutvomit</li>" \
            "<li>/raccoon/tuecoutesquoi</li>" \
        "</ul>" \

@raccoon_api.route('/raccoon/onmangequand', methods=['GET'])
def get_onmangequand():
    return "Quand j'ai faim! Sinon apres, il y a trop de nourriture dans mon ventre :o"

@raccoon_api.route('/raccoon/estcequeraccoonafaim', methods=['GET'])
def get_estcequeraccoonafaim():
    return "OUI! Toujours !"

@raccoon_api.route('/raccoon/cestquandquonboit', methods=['GET'])
def get_cestquandquonboit():
    return "Quand tu veux :) (tant que c'est pas de l'evian)"

@raccoon_api.route('/raccoon/onsortou', methods=['GET'])
def get_onsortou():
    mystery = random.randrange(0, 7)
    if(mystery == 0):
        return "Au Black Dog (ya dla musique de sauvage)"
    elif(mystery == 1):
        return "Tant'ya dla biere, j'men calice mon chum!"
    elif(mystery == 2):
        return "Au Feelgood, y sont fort laid labas"
    elif(mystery == 3):
        return "Au Ptit Garage, ya dla biere et des punks"
    elif(mystery == 4):
        return "Chez nous autres labas! Ya biere en masse"
    elif(mystery == 5):
        return "Beh jsais po.. Mais viens on jase"
    elif(mystery == 6):
        return "Au foufoune electrique (bon, ca fait, mais t'es tu game?)"
    return "Olala! C'est quoi cette merde?"

@raccoon_api.route('/raccoon/quiafaitcacadanslabruyere', methods=['GET'])
def get_quiafaitcacadanslabruyere():
    return "Alors la... Personne ne le sait !!!"

@raccoon_api.route('/raccoon/ditmoicestquoilemeilleursonaumonde', methods=['GET'])
def get_ditmoicestquoilemeilleursonaumonde():
    return "https://www.youtube.com/watch?v=4A6u2EAs2dc"

@raccoon_api.route('/raccoon/quiatoutvomit', methods=['GET'])
def get_quiatoutvomit():
    mystery= random.randrange(0, 5)
    if(mystery== 0):
        return "C'est Charles!"
    elif(mystery == 1):
        return "J'sais po mon chum..."
    elif(mystery == 2):
        return "Bey boy... C'est po moi !"
    elif(mystery == 3):
        return "C'est moieeee ! Hehe *hic*"
    elif(mystery == 4):
        return "C'est lui labas! Oui, lui labas derriere le fut de biere!"
    return "Ah.. Apparemment on saura jamais :p"

@raccoon_api.route('/raccoon/tuecoutesquoi', methods=['GET'])
def get_tuecoutesquoi():
    mystery= random.randrange(0, 5)
    if(mystery== 0):
        return "Plein de trucs debiles! (par example, la fameuse \"Toune De L'Ete!\" de Joel Martel, un grand homme)"
    elif(mystery == 1):
        return "D'la KPop ! YayayaalalalaaRatataaaaa"
    elif(mystery == 2):
        return "Des breakdowns de metalcore !!! Bouuuuum paff tadadaaaaam tchiiiiii! BIIIM"
    elif(mystery == 3):
        return "D'la pop! Yayay! Les fleuuuureees sooont jauuuuennnnneuuuh!"
    if(mystery== 4):
        return "Tant qu'on peut mettre les mains devant et descendre des rideaux, ca me va!"
    return "Justin Bieber et Tokio Hotel <3"
