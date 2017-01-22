# top levelをパスに含める
import sys
sys.path.append('/Users/razokulover/src/github.com/image-processing-training-with-python/bijin_judgement')

# db周りの抽象化
import mysql.connector
from config import Config

class DB():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=Config.DATABASE_HOST,
            port=Config.DATABASE_PORT,
            db=Config.DATABASE,
            user=Config.DATABASE_USER,
            password=Config.DATABASE_PASS,
            charset=Config.DATABASE_CHARSET
        )
        # executeでcommitまでやる。デフォルトはoff。
        # https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-autocommit.html
        self.conn.autocommit = True

    def cursor(self):
        return self.conn.cursor(buffered=True)

    def close(self):
        return self.conn.close()
