from flask import g, session
from sqlalchemy import text
from models import Users, Material, Inbound
from exts import db
from pyexcel_xlsx import get_data


def init_fun():
	g.find_text = text("id > 0")
	g.state = None
	g.user_messages = None
	g.pwd_messages = None


def checked():
	# list = ["None", "None", "None"]

	# 初始化全局中转变量
	init_fun()

	user_find_name = Users.query.filter(Users.name == g.name).first()
	user_find_pwd = Users.query.filter(Users.password == g.password).first()
	# 获取 数据库查询结果

	if user_find_name and user_find_pwd:
		return True

	else:
		if not user_find_name:
			# 给出错误信息
			g.user_messages = u" 用户不存在"
		if not user_find_pwd:
			# 给出错误信息
			g.pwd_messages = u" 密码不正确"

		return False


def check_user_bk():
	# 定义全局 错误信息为空
	g.state = None
	g.user_messages = None
	g.pwd_messages = None

	user_find_name = Users.query.filter(Users.name == g.name).first()
	user_find_pwd = Users.query.filter(Users.password == g.password).first()
	# print(user_find_name)
	# print(user_find_pwd)
	# g.messages = None
	if user_find_name and user_find_pwd:
		# session.permanent = True
		session['name'] = g.name
		session['pwd'] = g.password
		g.state = u"登录成功!"
		g.messages = u"{}，你输入用户名及客码正确".format(g.name)
	else:
		if not user_find_name:
			g.user_messages = u" 用户不存在"
		if not user_find_pwd:
			g.pwd_messages = u" 密码不正确"

	print("user:{},pwd:{}".format(user_find_name, user_find_pwd))


def check_user():
	if checked():
		session['name'] = g.name
		session['pwd'] = g.password
		g.state = u"登录成功!"
		g.messages = u"{}，你输入用户名及客码正确".format(g.name)


def clear_session():
	g.name = None
	g.state = u"退出成功!"
	g.messages = u"已按你的要求清除用户名本地记录"
	session.clear()


def data_modify():
	# print("Name:{},PWD:{},Content:{}".format(g.name, g.password, g.content))
	# print("{}:{}:{}".format(len(g.name), len(g.password), len(g.content)))
	if len(g.password) == 0 or len(g.content) == 0:
		if len(g.password) == 0:
			g.pwd_messages = u"原密码不能为空"
			print("PWD None")
		if len(g.content) == 0:
			g.pwd_new_messages = u"新密码不能为空"
			print("NEW PWD None")
	else:
		print("ELSE None")
		if checked():
			new_pwd = Users.query.filter(Users.name == g.name).first()
			# print(new_pwd)
			new_pwd.password = g.content
			db.session.commit()
			g.state = u"密码修改 成功!"
			g.messages = u"已按你的要求修改新密码为:{},请你牢记本密".format(g.content)


def list_data():
	init_fun()
	# # write_data()
	# temp_data = {}
	# temp_list = []

	data_list = Inbound.query.all()
	print(type(data_list))

	# print("fun >> print g.data_list:".format(data_list))

	# for i in data_list:
	# 	# 	temp_data.update(mater_id=i.mater_id, name=i.name, mate_type=i.mate_type)
	# 	# 	# print(temp_data)
	# 	#
	# 	# 	temp_list.append(temp_data)

	return data_list

	# for i in new_data:
	# 	print("Data : {}".format(i))0-
	# 	print("Data : {}".format(i.name))

def list_to_dict(data):
	print("cheng aeft:".format(data))
	if data:
		data = {}
		kk = 1
		for i in data:
			data = {kk: {"id": i.id}, }
			kk = kk + 1
	else:
		return {}
	return data


def write_data():
	w1 = Material(mate_type="46546546", name="546465")
	w2 = Material(mate_type="afdsafd", name="rwerw")
	w3 = Material(mate_type="46sdfsdf546546", name="5sdf46465")
	w4 = Material(mate_type="4654646", name="54665")
	w5 = Material(mate_type="afdsfd", name="rwrw")
	w6 = Material(mate_type="46sdfsdf54546", name="5sdf6465")
	db.session.add(w1)
	db.session.commit()

	db.session.add(w2)
	db.session.commit()

	db.session.add(w3)
	db.session.commit()

	db.session.add(w4)
	db.session.commit()

	db.session.add(w5)
	db.session.commit()

	db.session.add(w6)
	db.session.commit()


def get_excel():
	data = get_data(r"data\db1.xlsx")
	# print("数据格式：")
	# print(type(data))
	# print(data)

	# for sheet_n in data.keys():
	# 	print(sheet_n, ":", data[sheet_n])

	# keys = data.keys()
	# print(keys)

	data_list = data['in']
	# print(data_list)

	return data_list


def write_data_list(list_item):

	# w1 = Material(mate_type="46546546", name="546465")
	# db.session.add(w1)
	# db.session.commit()
	for i in list_item:
		print(i)
		for ii in i:
			print(ii)

		break
		# ii = tuple(i)
		# k = Inbound(i)
		# Inbound()
		# print(type(k))
		# db.session.add(k)
		# db.session.commit()
	# i = [43390, '', 'SL-180905002-2000', 8, 11200]
	# ii = (43390, '', 'SL-180905002-2000', 8, 11200)

	# print(type(i))
	# print(type(ii))
	# iii = tuple(i)
	# print(iii)


if __name__ == "__main__":
	pass

# 文件结束