import cv2
import numpy as np
import requests

url = r'http://192.168.8.103:8000/uploads/default.jpg'
resp = requests.get(url, stream=True).raw
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)


print(image)

