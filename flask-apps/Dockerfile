# Le FROM est un élément obligatoire à faire figurer dans le Dockerfile
# On utilise en général une distribution Linux minimaliste (comme debian ou alpine)
# Il est possible de partir d'un conteneur complètement vide en utilisant "FROM scratch"
FROM ubuntu:14.04
FROM python:3

# Grâce au "RUN" vous pouvez exécuter de véritables commandes Shell à l'intérieur du conteneur
# au moment où il est buildé.
# La commande ci-dessous installe le paquet nginx et le paquet curl
RUN python3 -m pip install psycopg2
RUN python3 -m pip install Flask
#RUN python3 -m pip install requirements.txt 

COPY . /home/flask-app

WORKDIR /home/flask-app

# Par défaut, aucun port TCP ou UDP n'est ouvert
# La commande "EXPOSE" permet d'ouvrir les ports indiqués sur le conteneur
# Attention, cela n'empêche pas d'utiliser l'option --publish pour rediriger ces ports
# vers ceux de votre machine
#EXPOSE 5000

# Le dernier paramètre obligatoire CMD correspond à la commande à exécuter lorsque le conteneur
# démarre.
# Attention seule une commande CMD est autorisée et si vous en indiquez plusieurs, seule la dernière
# sera utilisée
CMD [ "python3", "app.py" ]