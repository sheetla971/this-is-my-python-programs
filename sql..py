import sql.connector as con

from constant import HOST, DB_NAME, DB_USER, DB_PASS


class connection (object):
    def __init(self):
        self.con=con.connect(host=HOST,database=DB_NAME,user=DB_USER,passwd=DB_PASS)
        def get_cursor(self):
            return self.con.cursor()



