import pymssql
import numpy

"""
使用 pymssql 對資料庫進行連接 
"""
server = "wenrene.database.windows.net"
database= "free-sql-db-1116192" 
user = "dbeng" 
password = "Re2521026"
'''密碼洩漏問題'''


connect = pymssql.connect(server, user, password, database)
print("db登入成功")