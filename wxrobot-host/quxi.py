
import time
from wxpy import *
bot = Bot()

my_friend = bot.friends().search(u'小山')[0]


time_str1 = '2019-8-6 23:52:00'
timeArray1 = time.strptime(time_str1, "%Y-%m-%d %H:%M:%S")
timeStamp1 = int(time.mktime(timeArray1))
print(timeStamp1)
if time.time() == 1565106720:
    print(time.time())
    my_friend.send('Hello, WeChat!')







# 堵塞进程，直到结束消息监听 (例如，机器人被登出时)
# embed() 互交模式阻塞，电脑休眠或关闭互交窗口则退出程序
bot.join()