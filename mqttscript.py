import paho.mqtt.client as mqtt
import mysql.connector
from mysql.connector import Error

def save(x):
    parts = x.split(',')
    CapteurId, Timestamp, Valeur, Nom, Piece, Emplacement, Date = "", "", "", "", "", "", ""
    for part in parts:
        key, value = part.split('=')

        if key == "Id":
            CapteurId = value
        elif key == "piece":
            Piece = value
        elif key == "date":
            Date = value
        elif key == "time":
            Timestamp = value
        elif key == "temp":
            Valeur = value
        
        if Piece == 'sejour':
            Emplacement = 'Commode'
            Nom = 'Capteur1'
        else :
            Emplacement = 'Table'
            Nom = 'Capteur2'

    data1 = [CapteurId, Timestamp, Valeur]
    data2 = [Nom, Piece, Emplacement, Date]

    insert_data1("10.252.5.130", "temp_db", "Django", "Tototata6-", "donnees", data1)
    insert_data2("10.252.5.130", "temp_db", "Django", "Tototata6-", "capteur", data2)


def on_connect(client, userdata, flags, rc):
    client.subscribe(sub_topic)

def on_message(client, userdata, msg):
    message = msg.payload.decode('utf-8')
    save(message)

def insert_data1(host, database, user, password, table, data):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            query = f"""
            INSERT INTO {table} (CapteurId, Timestamp, Valeur) 
            VALUES (%s, %s, %s) 
            ON DUPLICATE KEY UPDATE 
                Timestamp = VALUES(Timestamp),
                Valeur = VALUES(Valeur)
            """
            cursor.execute(query, data)
            connection.commit()
            print(f"Data inserted or updated successfully into {table} table")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def insert_data2(host, database, user, password, table, data):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            query = f"""
            INSERT INTO {table} (Nom, Piece, Emplacement, Date) 
            VALUES (%s, %s, %s, %s) 
            ON DUPLICATE KEY UPDATE 
                Date = VALUES(Date),
                Piece = VALUES(Piece)
            """
            cursor.execute(query, data)
            connection.commit()
            print(f"Data inserted or updated successfully into {table} table")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


Broker = "test.mosquitto.org"
sub_topic = "IUT/Colmar2024/SAE2.04/Maison1"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(Broker, 1883, 60)
client.loop_forever()
