
from prefect import flow, task
import random
from kafka import KafkaProducer
import json
import time


# Définition d’une tâche Prefect pour générer des données de capteurs météo
@task
def generate_sensor_data():
    return {
        "timestamp": time.time(),  # Heure actuelle au format timestamp 
        "temperature": round(random.uniform(25, 40), 2),  # Température aléatoire entre 25°C et 40°C
        "humidity": round(random.uniform(40, 90), 2)  # Humidité aléatoire entre 
    }


# Définition d’une tâche Prefect pour envoyer les données générées à Kafka
@task
def send_to_kafka(data):
    # Création d’un producteur Kafka configuré pour se connecter au broker
    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',  # Adresse du serveur Kafka 
        value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Sérialisation des données en JSON
    )

    # Envoi des données dans le topic Kafka nommé 'agri-stream'
    producer.send('agri-stream', value=data)

    # Vider le buffer pour garantir que le message est bien envoyé immédiatement
    producer.flush()


# Définition du flow principal Prefect
@flow(name="Weather Kafka Flow")
def weather_stream():
    # Boucle pour envoyer 3 messages au total
    for _ in range(3):
        # Génération de données simulées de capteurs
        data = generate_sensor_data()
        print(data)

        # Envoi des données générées vers Kafka
        send_to_kafka(data)

        # Pause de 5 secondes pour simuler un intervalle entre les envois
        time.sleep(5)


# Point d’entrée du script : exécution du flow si le fichier est lancé directement
if __name__ == "__main__":
    weather_stream()
