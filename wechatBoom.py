import itchat
import time
print('扫一下弹出来的二维码')
# 自动登录微信
itchat.auto_login(hotReload=True)
# 标记你要轰炸人的微信备注，是备注
boom_remark_name=input('输入你要轰炸的人的微信备注，按回车继续 ')
# 轰炸的内容
message=input('请输入你要轰炸的内容')
boom_obj=itchat.search_friends(remarkName=boom_remark_name)[0]['UserName']
while True:
    time.sleep(0.5)
    print('正在轰炸。。。。')
    itchat.send_msg(msg=message,toUserName=boom_obj)