from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def connection() :
    """
    Methode: connection
    Input: Aucun
    Output: Aucun
    Description: Methode threader lors de la connexion
    """
    while True : 
        try :
            message_connection = socket_client.recv(TAILLE).decode("utf8")
            #
            # Mettre code ici pour ce que le protocole doit faire
            # a la connexion au serveur
            #
            print(message_connection)
            recevoir()
        except OSError :
            break

def recevoir() :
    while True :
        try :
            message_recu = socket_client.recv(TAILLE).decode("utf8")
            #
            # Mettre code ici pour ce que le protocle doit faire
            # lorsqu'il recoit des donnes apres la connexion
            #
            print(message_recu)
        except OSError :
            break


def envoyer(message_envoye) :
    """
    Methode: envoyer
    Input: Un message
    Output: Aucun
    Description: Methode pour envoyer des donnees au serveur
    """
    if message_envoye != " " :
        socket_client.send(bytes(message_envoye,"utf8"))
    if message_envoye == "/quitter" :
        socket_client.send(bytes("client deconnecter","utf8"))
        quitter()

def quitter() :
    """
    Methode: quitter
    Input: Aucun
    Output: Aucun
    Description : Methode lorsqu'un client quitte l'application
    grace a la commande /quitter
    """
    socket_client.close()
    #
    # Mettre code pour le protocole lorsque un client se
    # deconnecte.
    #

###############

LISTE_COMMANDE = ["/quitter",]

HOTE = "127.0.0.1"  #Adresse du serveur qui est le loopback
PORT = 80   #A changer pour un adresse non utilise(A DETERMINE)
TAILLE = 1024   #La longueur possible d'un message lorsque recu(A DETERMINER)
ADD = (HOTE,PORT)   #L'adresse est un tuple de l'ip et du port

socket_client = socket(AF_INET, SOCK_STREAM)    #Creer le socket
socket_client.connect(ADD)  #Ouvre la connection

thread = Thread(target=connection)    #Creer un thread a partir de la fonciton connection
thread.start()                        #Ce thread ecoute en permanance sur le socket
#
#Code de lancement du GUI Tkinter
#