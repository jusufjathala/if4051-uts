# main.py

import machine
from time import sleep
from umqtt.simple import MQTTClient


sleep(3)
led = machine.Pin(2, machine.Pin.OUT)

CLIENT_NAME = b'esp32'
BROKER_ADDR = b'72f4e7db90564580a07b5ccf36eaab25.s2.eu.hivemq.cloud'
USER_NAME = b'itb13519174'
USER_PASS = b'itB13519174'
mqttc = MQTTClient(CLIENT_NAME,
                   BROKER_ADDR,
                   port=0,
                   user=USER_NAME,
                   password=USER_PASS,
                   keepalive=60,
                   ssl=True,
                   ssl_params={'server_hostname':'72f4e7db90564580a07b5ccf36eaab25.s2.eu.hivemq.cloud'})
mqttc.connect()

topic_state = 'hivemq/state'
topic_command = 'hivemq/command'
message_received = ""
def callback_prod(topic, msg):
    global message_received
    if msg.decode() == 'on':
        led.value(1)
        message_received = "ON"
    elif msg.decode() == 'off':
        led.value(0)
        message_received = "OFF"
    else : #commmand check
        message_received = "CHECK_STATE"
        pass
        
# mqtt subscription
mqttc.set_callback(callback_prod)
mqttc.subscribe(topic_command)

while True:
    mqttc.check_msg()
    if (message_received):
        mqttc.publish( topic_state, str(led.value()).encode() )
        message_received = ""
    sleep(0.5)


