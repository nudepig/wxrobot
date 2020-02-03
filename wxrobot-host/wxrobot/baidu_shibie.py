# from aip import AipOcr  # 如果已安装pip，执行pip install baidu-aip即可
# import os
# """ 你的 APPID AK SK """
# APP_ID = '16802142'
# API_KEY = 'FcIxTPz25FZOSjOfgTKfAWIn'
# SECRET_KEY = 'GKIvG4tFqqyzisDCY81ASkMihg3LHrwx'
#
# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# """ 读取图片 """
# def get_file_content(filePath):          # 读取图片
#     with open(filePath, 'rb') as fp:
#         return fp.read()
#
# def image_identify(picture):
#     image = get_file_content(picture)
#     # print(image)
#     # time_one = time.time()
#     result = client.basicAccurate(image)  # 获取百度识别的结果
#     # time_two = time.time()
#     # print(time_two - time_one)
#     # if time_two - time_one > 6:
#     # else:
#     if os.path.exists('result.txt'):
#         os.remove('result.txt')
#     for result_words in list(result['words_result']):    # 提取返回结果
#         with open('result.txt', 'a+', encoding='utf-8') as file:
#             file.write(result_words['words'] + '\n')
#     with open('result.txt', 'r', encoding='utf-8') as file:
#         result_input = file.read()
#         return result_input    # 返回识别的文字结果，文字分行
#
# picture = r'f43a9ae3508254911d9b551d3b0a2d5.png'
# image_identify(picture)

# encoding:utf-8
# 旧版api


import requests
import base64
import os

'''
通用文字识别（高精度版）
'''

def image_identify(picture):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=v6ChGHmbOGNu5yyP1bchGYmF&client_secret=RSLGkQm44tYEti0m7dfg2GGgAibFKkZ2'
    access_token = requests.get(host)
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open(picture, 'rb')
    img = base64.b64encode(f.read())
    access_token = access_token.json()
    access_token = access_token['access_token']
    params = {"image": img}
    # access_token = '[调用鉴权接口获取的token]'
    request_url = '{}?access_token={}'.format(request_url, access_token)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    response = response.json()
    if os.path.exists('result.txt'):
            os.remove('result.txt')
    for result_words in list(response['words_result']):    # 提取返回结果
        with open('result.txt', 'a+', encoding='utf-8') as file:
            file.write(result_words['words'] + '\n')
    with open('result.txt', 'r', encoding='utf-8') as file:
        result_input = file.read()
        return result_input
