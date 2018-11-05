from exts import db


class Users(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	password = db.Column(db.String(16), nullable=False)
	department_id = db.Column(db.Integer, nullable=False)

#
# class Material(db.Model):
# 	__tablename__ = "material"
# 	mater_id = db.Column(db.Integer, primary_key=True)
# 	mate_type = db.Column(db.String(20), nullable=False)
# 	name = db.Column(db.String(16), nullable=False)
#
#
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
# class Department(db.Model):
# 	__tablename__ = "department"
# 	group_id = db.Column(db.String(15), primary_key=True, autoincrement=True)
# 	name = db.Column(db.String(16), nullable=False)
