#kode untuk menghidupkan buzzer dan led saat cellphone terdeteksi
from machine import Pin
from machine import PWM
from time import sleep
import network
from umqtt.simple import MQTTClient

red_led = Pin(5, Pin.OUT)
green_led = Pin(23, Pin.OUT)
buzzer = PWM(Pin(19, Pin.OUT))
buzzer.init(freq=25, duty=0)

def hidupkan_buzzer():
    buzzer.init(freq=1000, duty=1023)
    sleep(0.4)
    buzzer.duty(0)
    buzzer.deinit()

def hidupkan_lampu():
    green_led.off()
    red_led.on()
    sleep(0.4)
    red_led.off()
    green_led.on()
    print("buzzer on")


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Lahado", "AmbolaahRhss@**")

while not wlan.isconnected():
    print(".", ends="")
    red_led.on()
    
print("wifi is connected")

def led_control (topic, msg):
    payload = msg.decode().strip()
    print("Pesan diterima dari topic:", topic, "dengan payload:", payload)
    
    if payload == "terdeteksi kecurangan, lampu dan buzzer dinyalakan!":
        hidupkan_lampu()
        hidupkan_buzzer()
    else:
        red_led.off()
        
port = 1884
topic = "/nay/notifikasi"
broker= "192.168.18.185"
client_name = "projectdigivatorshsc191"
mqttc = MQTTClient(client_id=client_name, server = broker, port=port)

mqttc.connect()
mqttc.set_callback(led_control)
mqttc.subscribe(topic)

print("mqtt berhasil connect")

        
while True:
    mqttc.check_msg()
    sleep(0.1)
    
