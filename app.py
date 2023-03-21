from flask import Flask,render_template,request
import paho.mqtt.client as mqtt
import json
import logging
import time

app = Flask(__name__)

message_received = ""
state = ""
def on_connect(client,userdata,flags,rc):
    print("Connected with result code "+str(rc))
    client.subscribe("hivemq/test")

def on_message(client,userdata,msg):
    try:
        global message_received
        topic = msg.topic
        # print(topic)
        message_received = msg.payload.decode('utf-8')
        # print(message_received)
    except Exception as e:
        print("error",e)
        
        
client= mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("itb13519174","itB13519174")
client.loop_start()
client.connect("72f4e7db90564580a07b5ccf36eaab25.s2.eu.hivemq.cloud",8883,60)

@app.route('/', methods =["GET", "POST"])
def index():
    #client.loop_forever()
    if request.method == 'POST':
        global state 
        on_button = request.form.get("on_button")
        off_button = request.form.get("off_button")
        check_button = request.form.get("check_button")
        if on_button == 'TURN_ON':
            client.loop_start() #start the loop
            client.subscribe("hivemq/state")
            client.publish("hivemq/command", payload="on", qos=1)
            
            time.sleep(3) # wait
            
            if message_received == "1":
                state = "ON"
            elif message_received == "0":
                state = "OFF"
            else:
                state = "ERROR (Please CHECK_STATE)"
                pass
            
        elif  off_button == 'TURN_OFF':
            client.loop_start() #start the loop
            client.subscribe("hivemq/state")
            client.publish("hivemq/command", payload="off", qos=1)
            
            time.sleep(3) # wait
            
            if message_received == "1":
                state = "ON"
            elif message_received == "0":
                state = "OFF"
            else:
                state = "ERROR (Please CHECK_STATE)"
                pass
            
        elif check_button == 'CHECK_STATE' :
            client.loop_start() #start the loop
            client.subscribe("hivemq/state")
            client.publish("hivemq/command", payload="check", qos=1)
            
            time.sleep(3) # wait
            
            if message_received == "1":
                state = "ON"
            elif message_received == "0":
                state = "OFF"
            else:
                state = "ERROR (Please CHECK_STATE)"
                pass
            
        else :
            pass
        client.loop_stop()
        return render_template('index.html', state=state)
    
    client.loop_stop()
    return render_template('index.html')
