from pymysql import *
from pymysql import cursors

class DatabaseHelper():
    USER = 'root'
    PASSWORD = '..#Gunjan4122'
    HOST = 'localhost'
    database = 'inventory'

    @classmethod
    def execute_query(cls, query, parameters=None):
        conn = connect(host=cls.HOST, database=cls.database, user=cls.USER, password=cls.PASSWORD)
        cur = conn.cursor()
        if (parameters is None):
            cur.execute(query)
        else:
            cur.execute(query, parameters)
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def get_data(cls, query, parameters=None) -> dict:
        conn = connect(host=cls.HOST, database=cls.database, user=cls.USER, password=cls.PASSWORD)
        cur = conn.cursor(cursor=cursors.Cursor)
        if (parameters is None):
            cur.execute(query)
        else:
            cur.execute(query, parameters)
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result

    @classmethod
    def get_columns(cls, description):
        # column names are present as the first element of the collection,
        # hence extract the first element[0], create tuple & return it.
        return tuple(map(lambda x: x[0], description))

    @classmethod
    def get_all_data(cls, query, parameters=None):
        conn = connect(host=cls.HOST, database=cls.database, user=cls.USER, password=cls.PASSWORD)
        cur = conn.cursor()
        if (parameters is None):
            cur.execute(query)
        else:
            cur.execute(query, parameters)
        result = cur.fetchall()
        # get me the column names of the data
        headers = DatabaseHelper.get_columns(cur.description)
        cur.close()
        conn.close()
        # add the columns as the first row of my data
        return (headers,) + result

    @classmethod
    def get_data_combo(cls,query):
        conn = connect(host=cls.HOST, database=cls.database, user=cls.USER, password=cls.PASSWORD)
        cur = conn.cursor()
        cur.execute(query)
        result=cur.fetchall()
        cur.close()
        conn.close()
        return result
