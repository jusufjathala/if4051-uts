
import esp
import uos, machine
import gc
import network

def connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('Test', 'wifipass1')
        while not sta_if.isconnected():
            pass # wait till connection
    print('Connection success, network config:', sta_if.ifconfig())

#esp.osdebug(None)
gc.collect()
connect()

