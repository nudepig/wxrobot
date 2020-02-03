import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import random
# def get_file_content(filePath):  # 读取文本
#     print(filePath, type(filePath))
#     with open(filePath, 'r') as fp:
#         return fp.read()
def face(msg):
    # 初始化字符串
    std = str(msg)
    stt = std.find(":")
    stu = std[stt+3:-6]
    # ste = get_file_content(msg) # "包长荣,董亚静;包良荣,王林香;李发宁,靳海燕;王秉安;魏耀鑫"
    # stt = ste.decode()
    # print(std)
    sty = (300-len(stu)*20)/2
    # 模板图片
    num = random.randint(1, 681)
    imageFile = "D:\Favorites\Links\pic_aqa\i%s.jpg" % num  # "F:\\family\\请柬模板.JPG"
    # 新文件保存路径
    file_save_dir = "D:\Favorites\Links\samples"

    # 初始化参数
    x = sty  # 横坐标（左右）
    y = 260  # 纵坐标（上下）
    word_size = 20  # 文字大小
    word_css = "C:\Windows\Fonts\msyh.ttf"  # 字体文件   行楷
    # STXINGKA.TTF华文行楷   simkai.ttf 楷体  SIMLI.TTF隶书  minijianhuangcao.ttf  迷你狂草    kongxincaoti.ttf空心草

    # 设置字体，如果没有，也可以不设置
    font = ImageFont.truetype(word_css, word_size)

    # 分割得到数组
    im1 = Image.open(imageFile)  # 打开图片
    im = im1.resize((300, 300))
    # box = (0, 0, 300, 300)  ##确定拷贝区域大小
    # im = im2.crop(box)  ##将im表示的图片对象拷贝到region中，大小为box
    draw = ImageDraw.Draw(im)
    print(font.getsize(stu))
    draw.text((x, y), stu, (0, 0, 0), font=font)  # 设置位置坐标 文字 颜色 字体

    # 定义文件名 数字需要用str强转
    new_filename = file_save_dir + ".jpg"
    im.save(new_filename)
    del draw  # 删除画笔
    im.close()  # 关闭图片
    return new_filename