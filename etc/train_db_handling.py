# db操作
# ORMは使わずmysql-connector-pythonを利用する
# conda install -c https://conda.anaconda.org/anaconda mysql-connector-python
# 参考) http://qiita.com/zaburo/items/55347181be742b5109ea

import mysql.connector

# 接続
dbh = mysql.connector.connect(
    host='localhost',
    port='3306',
    db='net_keiba',
    user='root',
    password='root',
    charset='utf8'
)
stmt = dbh.cursor(buffered=True)

# 取得
sql = "select * from race_results order by id desc limit 10"
stmt.execute(sql)
rows = stmt.fetchall()
for row in rows:
    print(row)

# 挿入
# sql = "insert into race_results(race_definition_id, order_of_finish) values(200601010101, 1)"
# stmt.execute(sql)
# res = dbh.commit()

# # 更新
# sql = "update race_results set order_of_finish = 2 where id = 494701"
# stmt.execute(sql)
# res = dbh.commit()

# 削除
# sql = "delete from race_results where id = 494701"
# stmt.execute(sql)
# res = dbh.commit()

stmt.close()
dbh.close()
