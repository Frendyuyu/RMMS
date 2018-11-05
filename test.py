from flask import Flask, render_template, request, g, session, jsonify, json
from models import *
from exts import db
import config
from inital import inital_admin
from functions import check_user, clear_session, data_modify, checked, list_data, list_to_dict

app = Flask(__name__)
app.config.from_object(config)
app.config['PORT'] = 80

# 传递一个APP 到db中初始化
db.init_app(app)


# 映射  一个article 表
# id
# title
# content
with app.app_context():
	db.create_all()
	inital_admin()


# 主页
@app.route("/")
def index():
	# session['name'] = g.name
	# session['pwd'] = g.password
	# print("session :{}".format(session))
	# if session:
	# 	g.name = session['name']
	# 	g.password = session['pwd']
	# 	if checked():
	# 		return render_template("index.html")
	# 	else:
	# 		return render_template("login.html")
	# else:
		return render_template("index.html")


@app.route("/json/")
def json_html():
	data_dict = list_data()
	# print(type(data_dict))
	temp = list_to_dict(data_dict)
	print(type(temp))
	return jsonify(temp)


# 列表页
@app.route("/list/")
def list_html():
	data_dict = list_data()
	dict_data = {"data": data_dict}
	print(dict_data)
	dict_2 = {
		"admin": 1,
		"group": "003"
	}
	# k = json
	kk = json.dumps(dict_2)
	print("json:{}".format(kk))
	return render_template("list.html", **dict_data)


# 管理页
@app.route("/admin/<user>")
def admin_html():
	return render_template("admin.html")


# # 登陆页
# @app.route("/login")
# def add_html():
# 	if request.method == 'GET':
# 		return render_template("add.html")
# 	else:
# 		title = request.form.get('title')
# 		content = request.form.get('content')
# 		print("title:%s" % title)
# 		print("content: %s" % content)
# 		# 写表
# 		article1 = Article(title=title, content=content)
# 		db.session.add(article1)
# 		# 事务：
# 		db.session.commit()
# 		return "写入成功"


@app.route("/login/", methods=['GET', 'POST'])
def login_html():
	print("def Longin_html request.range：")
	print(request.range)

	if request.method == 'GET':
		g.state = session.get('name')
		return render_template("login.html")

	else:
		g.name = request.form.get('user')
		g.password = request.form.get('password')
		# 将用户传来的值进行 g 处理
		check_user()

		# return render_template("login.html")
		# return "登录成功：USER:{},   WD:{}".format(g.name)
		return render_template("login.html")


@app.route("/logout/")
def logout_html():
	clear_session()
	return render_template("login.html")


@app.route("/modify/", methods=['GET', 'POST'])
def modify_html():
	if request.method == 'GET':
		return render_template("modify.html")

	else:
		# print("session:{}".format(session['name']))
		try:
			if not session['name']:
				return render_template("login.html")
			else:
				g.name = session['name']
				g.password = request.form.get('password')
				g.content = request.form.get('content')
				# 将用户传来的值进行 g 处理
				data_modify()

			return render_template("modify.html")

		except KeyError:
			return render_template("login.html")


if __name__ == '__main__':
	app.run(port=80)


