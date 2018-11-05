from flask import Flask, render_template, request, g, session
from models import *
from exts import db
import config
from inital import inital_admin
from functions import check_user, clear_session, data_modify, checked, list_data

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
def list_html():
	s = list_data()			# 把函数返回值传给 s
	context = {'list_temp': s}			# 用字典方式传给模板页

	return render_template("dome.html", **context)


if __name__ == '__main__':
	app.run(port=80)


