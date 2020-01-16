import requests
from PIL import Image
from aip import AipOcr
from io import BytesIO


## 请求百度图片识别API
def recImg(image):
    APP_ID = '18282548'
    API_KEY = '9Mjlx7LmrjeX8ymHGF26DSyG'
    SECRET_KEY = 'keyUX36ZrBCSs1f1ssenrr4vcR1h3BsC'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    res = client.basicGeneral(image)
    if 'words_result' in res.keys():
        for item in res['words_result']:
            print(item['words'])
        else:
            print(res)
    return res


## 将img对象转换为buf
def toBuf(img):
    imgByteArr = BytesIO()
    img.save(imgByteArr, format="PNG")
    return imgByteArr.getvalue()


## 判断图片中是否存在机身联字样
def jude(res):
    result = False
    if 'words_result' in res.keys():
        for item in res['words_result']:
            word = item['words']
            if word.count("机身联") > 0:
                result = True
                break
    return result


if __name__ == '__main__':
    ## 读取网络图片
    content = requests.get(
        'http://yzyx-guangzhou20180315-1256259170.cos-website.ap-guangzhou.myqcloud.com/2019/12/03/18/14141027_1575367443257.jpg').content
    ## 打开成IMG对象
    img1 = Image.open(BytesIO(content))
    ## 图片旋转
    img2 = img1.rotate(90)
    img3 = img1.rotate(180)
    img4 = img1.rotate(270)
    imgList = [img1, img2, img3, img4]
    result = False
    ## 循环打开
    for newImg in imgList:
        # 转换为字节流
        imgBuf = toBuf(newImg)
        # 调用图片识别
        res = recImg(imgBuf)
        # 判断图中是否存在相同字样
        result = jude(res)
        if result:
            break
    print(result)
