import sqlite3
dbname = "EDICT.sqlite3"


# データベースに接続するには，sqlite3.connect()メソッドを使用する->Connectionオブジェクトが作成される
conn = sqlite3.connect(dbname)

# itemsテーブルのカラム名取得
cur = conn.cursor()
select_sql = "pragma table_info(edict);"
for row in cur.execute(select_sql):
   print_txt = ""
   for i in range(len(row)):
       print_txt = f"{print_txt}{row[i]} | "
   print(print_txt)
cur.close()


# 1行ずつ読み込む(SQL文を実行するには，Cursorオブジェクトのexecute()メソッドを使用する．)
select_sql = "select * from edict"
cur = conn.cursor()
for row in cur.execute(select_sql):
   print_txt = ""
   for i in range(len(row)):
       print_txt = f"{print_txt}{row[i]} | "
   print(print_txt)
cur.close()