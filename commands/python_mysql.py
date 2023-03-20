import os
from dotenv import load_dotenv
import mysql.connector


class mysql_db:
    def __init__(self):
        load_dotenv()
        self._conn  = mysql.connector.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER_NAME"),
            password=os.getenv("PASSWORD"),
        )
        try:
            if self._conn.is_connected():
                self._cursor = self._conn.cursor()
        except Error as e:
            print("Error while connecting to MySQL", e)
       

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


