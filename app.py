from flask import Flask, render_template, request, g, session
#  数据模型
from models import *
# 配置文件
import config
from exts import db
# 操作函数
from functions import check_user
# 全局变量初始化
from inital import inital_admin

app = Flask(__name__)
app.config.from_object(config)
app.config['PORT'] = 80

# 传递一个APP 到db中初始化
db.init_app(app)


# 映射  一个article 表
# id
# title
# content
with app.app_context( ):
	db.create_all()
	inital_admin()


# 主页
@app.route("/")
def index():
	return render_template("index.html")


# 列表页
@app.route("/list/")
def list_html():
	# art_temp = Article.query.filter(Article.id > 0)

	# for temp  in art_temp:
	# 	print(temp.id)
	# 	print(temp.title)
	# 	print(temp.content)

	return render_template("list.html")


# 管理页
@app.route("/admin")
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


if __name__ == '__main__':
	app.run(port=80)

# TEST GIT
