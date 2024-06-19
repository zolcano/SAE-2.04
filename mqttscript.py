import csv
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

Broker = "test.mosquitto.org"
sub_topic = "IUT/Colmar2024/SAE2.04/Maison1"   

def csv_save(x):
    Id, Lieu, Date, Time, Temp = "", "", "", "", ""
    for i in range(12):
        Id += x[i+5]
    if x[24]=="c":
        Lieu = "chambre"
        for i in range(10):
            Date += x[i+38]
        for i in range(8):
            Time += x[i+54]
        for i in range(4):
            Temp += x[i+68]

        with open('chambre.csv', 'w', newline=None) as file:
            writer = csv.writer(file)
            writer.writerow(Id)
            writer.writerow(Lieu)
            writer.writerow(Date)
            writer.writerow(Time)
            writer.writerow(Temp)

    else:
        Lieu = "séjour"
        for i in range(10):
            Date += x[i+36]
        for i in range(8):
            Time += x[i+52]
        for i in range(4):
            Temp += x[i+66]
        with open('séjour.csv', 'w', newline=None) as file:
            writer = csv.writer(file)
            writer.writerow(Id)
            writer.writerow(Lieu)
            writer.writerow(Date)
            writer.writerow(Time)
            writer.writerow(Temp)
    print(Id, Lieu, Date, Time, Temp)

def on_connect(client, userdata, flags, rc):
    client.subscribe(sub_topic)

# when receiving a mqtt message do this;
def on_message(client, userdata, msg):
    message = str(msg.payload)
    csv_save(message)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(Broker, 1883, 60)
client.loop_forever()