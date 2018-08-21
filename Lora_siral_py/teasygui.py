import sys
import easygui as g

print("在哪里")

msg = "选择你喜欢的一种业余生活"
title = "兴趣检查"
choicess_list = ["看书","游泳","骑自行车","玩游戏"]
reply = g.choicebox(msg,title,choices=choicess_list)
flag = False
if reply == "看书":
	flag = True
else:
	g.msgbox("我们不提供该服务")

print("阻塞1")
#multpasswordbox() 跟 multenterbox() 使用相同的接口，
#但当它显示的时候，最后一个输入框显示为密码的形式（"*"）
#需要注意几点
#如果用户取消操作，则返回域中的列表的值或者None值
#如果用户输入的值比选项少的话，则返回列表中的值用空字符串填充用户为输入的选项

msg = "请输入用户名和密码"
title = "用户登录接口"
fieldNames = ["用户名","Email","密码"]
user_info = []
user_info = g.multpasswordbox(msg,title,fieldNames)
while True:
	if user_info == None:
		print("cancel")
		break
	errmsg=""
	for i in range(len(user_info)):
		option=user_info[i].strip()
		if option == "" and option[0] == "*":
			errmsg += "必填项"

	if errmsg == "":
		break
#注意 ccbox() 是返回整型的 1 或 0，不是布尔类型的 True 或 False。
	res = g.ccbox("亲爱的还玩吗？",choices=("重新输入！","退出登陆"))
	if res == 1:
		g.msgbox("您可以重新输入")
	else:
		g.msgbox("您已经退出登陆")

print("阻塞2")

print("您填写的资料如下:{0}".format(user_info))
#返回值为用户输入的字符串
#默认返回的值会自动去除首尾的空格
#如果需要保留首尾空格的话请设置参数 strip=False
title = "心里悄悄话"
msg = "您已登陆可以说心里话"
val = g.enterbox(msg=msg,title=title)

print("阻塞3")
if val == "秘密":
	val = textbox(msg='提点建议吧', title='建议', text='书写您的建议', codebox=0)
	g.msgbox("收到您的建议:{0}".format(val))

