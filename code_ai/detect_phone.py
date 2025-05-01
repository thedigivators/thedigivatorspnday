from ultralytics import YOLO
import cv2
import requests
from time import sleep, time
import paho.mqtt.client as mqtt
             
MQTT_TOPIC = "/nay/notifikasi"      
MQTT_BROKER = "localhost"
MQTT_PORT   = 1884
mqtt_client = mqtt.Client("MQTT QLIENT PUBLISHER")
mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
mqtt_client.loop_start()

# ESP32 URL
URL = "http://192.168.18.84"
AWB = True
video = cv2.VideoCapture(URL + ":81/stream")
# video = cv2.VideoCapture(0)

def set_resolution(url: str, index: int=1, verbose: bool=False):
    try:
        if verbose:
            resolutions = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)"
            print("available resolutions\n{}".format(resolutions))

        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")


def set_quality(url: str, value: int=1, verbose: bool=False):
    try:
        if value >= 10 and value <=63:
            requests.get(url + "/control?var=quality&val={}".format(value))
    except:
        print("SET_QUALITY: something went wrong")

def set_awb(url: str, awb: int=1):
    try:
        awb = not awb
        requests.get(url + "/control?var=awb&val={}".format(1 if awb else 0))
    except:
        print("SET_QUALITY: something went wrong")
    return awb

if __name__ == '__main__':
    set_resolution(URL, index=8)

model = YOLO('yolov8n.pt')
terdeteksi = 0
UBIDOTS_ENDPOINT = f"http://industrial.api.ubidots.com/api/v1.6/devices/esp32cam/"


while True:
    if video.isOpened():
        ret, frame = video.read()
        results = model.track(frame)
        frame_result = results[0].plot()


# Check if 'cell phone' is detected in the frame
        for r in results:
            boxes = r.boxes
        for box in boxes:
            class_id = int(box.cls[0])
            if class_id == 67:
                print("Kecurangan terdeteksi!")
                mqtt_client.publish(MQTT_TOPIC, "terdeteksi handphone, lampu dan buzzer dinyalakan!")
                terdeteksi += 1

                file_name = f"data/handphone_terdeteksi{terdeteksi}.jpg"
                cv2.imwrite(file_name, frame_result)


                file_path = f"D:\\STAGE 3 SIC\\data\\handphone_terdeteksi{terdeteksi}.jpg"
                files = {'photo' : open(file_path, 'rb')}
                telegram_api_url = 'https://api.telegram.org/bot7946877244:AAE8b7b83O25JJ8A4MrHBP8r-58pDZWdBIg/sendPhoto'
                params = {'chat_id': '-4651559197'}
                resp = requests.post(telegram_api_url, params=params, files=files)
                print(f"Status kirim Telegram: bukti gambar telah dikirim")
    

                data = {"Terdeteksi handphone" : terdeteksi}
                headers = {"Content-Type" : "application/json", "X-Auth-Token":"BBUS-L5TJHBNJc29LKKgDDXppr4d3jcyFbt"}
                response = requests.post(UBIDOTS_ENDPOINT, json=data, headers=headers)
                print(f"status pengiriman = {response.status_code}, {response.text}")
                
        cv2.imshow("Phone Detector", frame_result)
        key = cv2.waitKey(1)

        if key == ord('r'):
            idx = int(input("Select resolution index: "))
            set_resolution(URL, index=idx, verbose=True)

        elif key == ord('q'):
            val = int(input("Set quality (10 - 63): "))
            set_quality(URL, value=val)

        elif key == ord('a'):
            AWB = set_awb(URL, AWB)

        elif key == 27:
            break

text = f"Sesi pemantauan ujian telah selesai. Sistem mendeteksi sebanyak {terdeteksi} bukti yang perlu ditinjau lebih lanjut. Silakan akses hasil lengkap melalui tautan berikut: https://digivatorssipandai.streamlit.app/ sebagai bahan evaluasi dan tindak lanjut."
telegram_api_url = 'https://api.telegram.org/bot7946877244:AAE8b7b83O25JJ8A4MrHBP8r-58pDZWdBIg/sendMessage'
params = {'chat_id': '-4651559197',
          'text' : text}
resp = requests.post(telegram_api_url, params=params)
                     
cv2.destroyAllWindows()
video.release()

 
