from flask import g

from models import Material


def list_data():
	g.data_list = Material.query.first()
	print(type(g.data_list))
	print("fun >> print g.data_list:".format(g.data_list))
	for i in g.data_list:
		print("fun >> g.data_list.mater_id:{}".format(i.mater_id))
		print("fun >> g.data_list.name:{}".format(i.name))
		print("fun >> g.data_list.mater_type:{}".format(i.mate_type))


if __name__ == "__main__":
	list_data()


