#kode untuk menghidupkan buzzer dan led saat cellphone terdeteksi
from machine import Pin
from machine import PWM
import time
import network
from umqtt.simple import MQTTClient

led = Pin(19, Pin.OUT)
buzzer = PWM(Pin(4, Pin.OUT))
buzzer.init(freq=25, duty=0)

def hidupkan_buzzer():
    buzzer.init(freq=4186, duty=512)
    sleep(0.4)
    buzzer.duty(0)
    buzzer.deinit()

def hidupkan_lampu():
    led.on()
    sleep(0.4)
    led.off()


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Lahado", "AmbolaahRhss@**")

while not wlan.isconnected():
    print(".", ends="")
    
print("wifi is connected")


broker= "broker.emqx.io"
client_name = "projectdigivatorshsc191"
mqttc = MQTTClient (client_name, broker)

res = mqttc.connect()
print("Hasil koneksi MQTT:", res)

port = 1883
topic = "/nay/notifikasi"


def led_control (topic, msg):
    payload = msg.decode().strip()
    print("Pesan diterima dari topic:", topic, "dengan payload:", payload)
    if payload == "terdeteksi handphone, lampu dan buzzer dinyalakan!":
        hidupkan_lampu()
        hidupkan_buzzer()
    else:
        led.off()  

mqttc.set_callback(led_control)
mqttc.subscribe(topic)

        
while True:
    mqttc.check_msg()
    sleep(0.1)
    





