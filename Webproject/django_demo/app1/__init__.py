import pymysql
pymysql.version_info = (1, 4, 6, 'final', 0)  # 解决mysqlclient 1.3.13 or newer is required; you have 0.9.3.
pymysql.install_as_MySQLdb()
