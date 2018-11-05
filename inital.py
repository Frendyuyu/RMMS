from models import *


def inital_admin():
	"""
写表
# 		article1 = Article(title=title, content=content)
# 		db.session.add(article1)
# 		# 事务：
# 		db.session.commit()
# 		return "写入成功"
	:return:
	"""
	user_find = Users.query.filter(Users.name == "admin").first()
	# print("user find:".format(user_find))
	if user_find:
		# print("find")
		pass
	else:
		# print("none")
		administrators = Users(name="admin", password="5201314", department_id=1)
		db.session.add(administrators)
		db.session.commit()

	# .all()
	# user_find = Users.query.filter(Users.name == "admin").all()
	# print("finding:{}".format(user_find))
	# for i in user_find:
	# 	print(i.id)
	# 	print(i.name)
	# 	print(i.password)

	#  .first()
	# user_find = Users.query.filter(Users.name == "admin").first()
	# print("finding:{}".format(user_find))










