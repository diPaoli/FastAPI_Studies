from MySQLdb import _mysql

db = _mysql.connect(host="localhost",
            user="CursoFastAPI",
            password="senhaSenha.123",
            database="cursofastapi")


print(db)