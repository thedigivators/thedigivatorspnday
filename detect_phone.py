from ultralytics import YOLO
import cv2
import threading
import requests
from time import sleep, time

# ESP32 URL
URL = "http://192.168.18.84"
AWB = True
video = cv2.VideoCapture(URL + ":81/stream")

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

model = YOLO('yolov8m.pt')

while True:
    if video.isOpened():
        ret, frame = video.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)

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
                terdeteksi += 1
                file_name = f"data/handphone_terdeteksi{terdeteksi}.jpg"
                cv2.imwrite(file_name, frame_result)
                data = {"Terdeteksi handphone" : terdeteksi}
                headers = {"Content-Type" : "application/json", "X-Auth-Token":"BBUS-Ubq4m0YjEKtSfJDfVolqxOOs2gZfoz"}
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

cv2.destroyAllWindows()
video.release()

 
