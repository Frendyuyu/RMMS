from exts import db


class Users(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	password = db.Column(db.String(16), nullable=False)
	department_id = db.Column(db.Integer, nullable=False)

	# def user_check_fun(self, name, password):
	# 	user_find_name = Users.query.filter(Users.name == name).first()
	# 	user_find_pwd = Users.query.filter(Users.password == password).first()
	#
	# 	# 获取 数据库查询结果
	# 	if user_find_name and user_find_pwd:
	# 		return True



class Material(db.Model):
	__tablename__ = "material"
	mater_id = db.Column(db.Integer, primary_key=True)
	mate_type = db.Column(db.String(20), nullable=False)
	name = db.Column(db.String(16), nullable=False)


class Materiall(db.Model):
	__tablename__ = "materiall"
	mater_id = db.Column(db.Integer, primary_key=True)
	mate_type = db.Column(db.Integer, nullable=False)
	name = db.Column(db.Integer, nullable=False)


class Inbound(db.Model):
	__tablename__ = "inbound"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	date_in = db.Column(db.String, nullable=False)
	coding = db.Column(db.String(10), nullable=True)
	po_no = db.Column(db.String(15), nullable=False)
	power = db.Column(db.String(8),  nullable=False)
	inn = db.Column(db.Integer, nullable=False)
	date_up = db.Column(db.String, nullable=True)

# class Inbound(db.Model):
# 	__tablename__ = "inbound"
# 	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# 	mater_id = db.Column(db.Integer, nullable=False)
# 	po_no =  db.Column(db.String(15), nullable=False)
# 	department_in = db.Column(db.String(15), nullable=False)
# 	department_out = db.Column(db.String(15), nullable=False)
#
#
# class Outbound(db.Model):
# 	__tablename__ = "outbound"
# 	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# 	mater_id = db.Column(db.Integer, nullable=False)
# 	po_no =  db.Column(db.String(15), nullable=False)
# 	department_in = db.Column(db.String(15), nullable=False)
# 	department_out = db.Column(db.String(15), nullable=False)
#
#
# class Department(db.Model):
# 	__tablename__ = "department"
# 	department_id = db.Column(db.String(15), primary_key=True, autoincrement=True)
# 	name = db.Column(db.String(16), nullable=False)
# 	groups = db.Column(db.String(50), nullable=False)
#
#

# class Group(db.Model):
# 	__tablename__ = "group"
# 	group_id = db.Column(db.String(15), primary_key=True, autoincrement=True)
# 	name = db.Column(db.String(16), nullable=False)


# class Order(db.Model):
# 	__tablename__ = "order"
# 	group_id = db.Column(db.String(15), primary_key=True, autoincrement=True)
# 	name = db.Column(db.String(16), nullable=False)
