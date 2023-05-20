import requests
import cv2
import numpy as np
import imutils

url = "http://100.79.42.1:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1270, height=768)
    cv2.imshow("Watch it", img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()