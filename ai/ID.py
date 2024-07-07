import requests
import base64
import cv2 as cv

def ID(img):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"id_card_side": "front", "image": base64_image}
    access_token = '24.fdf2149555837edc56f2fd84bba0f1df.2592000.1722739222.282335-90548479'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    words_result2 = 'b'
    if response:
        data = response.json()
        words_result2 = data['words_result']['姓名']['words']

    return words_result2

