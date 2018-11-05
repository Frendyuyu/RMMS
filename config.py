import os
from datetime import timedelta

# FLASK CONFIG
# HOST = "127.0.0.1"
# PORT = 80
# SERVER_NAME = "{}:{}".format(HOST, PORT)
# DEBUG = True

# session 对像 密钥
SECRET_KEY = os.urandom(25)  # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # 设置session的保存时间。

# DATABASE CONFIG
DRIVECT = "mysql"
# DRIVER = "pymysql"
DRIVER = "mysqlconnector"
USERNAME = "root"
PASSWORD = "5201314"
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = "3306"
DATABASE = "test"
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DRIVECT, DRIVER, USERNAME, PASSWORD, MYSQL_HOST, MYSQL_PORT, DATABASE, )
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_NATIVE_UNICODE = 'utf8mb4'
# VARIABLE_VALUE = 'utf8mb4'


if __name__ == "__main__":
	# mysql + pymysql: // < username >: < password >@< host > / < dbname > [? < options >]
	print("Host name :{}/br DEF:{}".format(SERVER_NAME, "127.0.0.1:5000"))
	print("Connter DataBase Text:{} /br DEF:{}".format(SQLALCHEMY_DATABASE_URI, "mysql + pymysql: // < username >: < password >@< host > / < dbname > [? < options >]"))
