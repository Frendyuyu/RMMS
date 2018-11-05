from pyexcel_xlsx import get_data


def get_excel():
	data = get_data(r"data/exdb.xlsx")
	print("数据格式：")
	print(type(data))
	# print(data)

	# for sheet_n in data.keys():
	# 	print(sheet_n, ":", data[sheet_n])

	keys = data.keys()
	data_dict = data['IN']

	print(data_dict)


if __name__ == "__main__":
	print("这是一个测试模块：本模块测试读取EXCEL表 数据")
	print("回显：")
	get_excel()

# 文件结束

