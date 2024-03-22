from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def accepter_connection() :
    """
    Methode: accepter_connection
    Input: aucun
    Output: aucun
    Description: Thread principal qui ecoute pour des connexions
    et creer des threads pour chaque client.
    """
    while True:
        client, adresse_client = SERVEUR.accept()   
        print(f'{client} : {adresse_client}')
        adresses[client] = adresse_client   #Garde en memoire l'adresse du client
        Thread(target=traiter_client, args=(client,)).start()    

def traiter_client(client) :
    """
    Methode: traiter_client
    Input: un socket client
    Output: Aucun
    Description: Methode qui traite un seul client.
    """
    #
    # Mettre code pour protocole lorsqu'un client se connecte
    # au serveur.
    #
    client.send(bytes("Vous etes connecter","utf8"))
    diffuser("Un client sait connecter")

    #Boucle infini pour ecouter le client
    while True:
        message_recu = client.recv(TAILLE)
        if message_recu != "/quit" :
            #
            # Mettre code pour protocole lorsque le serveur
            # recoit les donnees du client apres la connexion
            #
            print(message_recu)

        if message_recu == "/quit" :
            deconnection_client(client)
            break

def deconnection_client(client) :
    """
    Methode: decconection_client
    Input: un socket client
    Output: Aucun
    Description: Methode qui definit ce qui se passe lorsqu'un client
    quitte l'application en envoyant /quit.
    """
    #
    # Mettre code pour protocole lorsqu'un client quitte.
    #
    client.close()

def diffuser(message) :
    for socket in adresses :
        socket.send(bytes(f'diffuser : {message}',"utf8"))

#Informations
adresses = {}      #Dictionnaire des addresses
client = {}        # Est ce que notre protocoles nous permet de garder en mémoire les clients?

HOTE = "127.0.0.1"
PORT = 80
TAILLE = 1024
ADD = (HOTE, PORT)

#Creation socket serveur
SERVEUR = socket(AF_INET, SOCK_STREAM)
SERVEUR.bind(ADD)
SERVEUR.listen(5)
print("***Attente de connection...***")

#Thread principale
THREAD = Thread(target=accepter_connection)
THREAD.start()

#Maintient du serveur, pour arreter Ctr + c
try :
    while True:
        pass
except KeyboardInterrupt :
    print("Arret serveur")
    THREAD.join()   
    SERVEUR.close()