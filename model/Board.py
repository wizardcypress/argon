from Model import Model
from Post import Post

class Board(Model):

    def __init__(self, boardname = "Test"):
        # According to database/template/argo_fileheader.sql
        self.boardname = self.escape_string(boardname)
        self.table = "argo_fileheader_" + self.boardname

        try:
            self.connect()
        except:
            pass
        else:
            init_board_info()

    def __getattr__(self, name):
        try:
            return self.dict[name]
        except KeyError:
            return None

    def __setattr__(self, name, value):
        self.dict[name] = value

    def init_board_info(self):
        self.query("SELECT * FROM argo_boardheader where boardname='%s'" % self.boardname)

        row = self.fetchone()
        #todo:
        #will hold all attributes into self.dict

    def get_post(self, start, end=-1)
        if end == -1: end = self.get_total()
        if start > end: start = end
        self.query("SELECT * FROM %s limit %d,%d order by pid", self.table, start, end)
        rows = self.fetchall()
        res = [Post(row) for row in rows]
        return res

    def get_total(self):
        self.query("SELECT count(*) FROM %s" % self.table)
        row = self.fetchone()
        return row[0]

    # get the last limit posts
    def get_last(self, limit = 20):
        end = self.get_total()
        start = end - limit
        if start <= 0: start = 0
        return self.get_post(start, end)


    def add_post(self, post):
        # Assume post has been escaped string
        keys = map(str, post.dict.keys())
        values = map(str, post.dict.values())
        self.query("INSERT INTO %s(%s) VALUES(%s)" % self.table, ",".join(keys), ",".join(values))


    def del_post(self, start, end = -1):
        if end == -1: end = self.get_total()
        if start > end: start = end;
        start_pid = self.get_post(start).pid
        end_pid = self.get_post(end).pid
        self.query("DELETE FROM %s WHERE pid >= %d and pid <= %d" % self.table, start_pid, end_pid)

    def del_last(self, limit = 20):
        end = self.get_total()
        start = end - limit
        if start <= 0: start = 0
        self.del_post(start, end)

    def update_post(self, pid, post):
        # Assume post has been escaped string
        key_value = [ str(key)+'='+str(val) for key,val in post.dict.items() if key != 'pid' and key != 'filename']
        key_value.k
        self.query("UPDATE %s SET %s where pid = %s" % self.table, ",".join(key_value), post.pid )

    def close(self):
        self.closedb()


