
class Model(object):

    def __init__(self, host = config.HOST, port = config.PORT, user=config.USER, passwd=config.PASSWD, db = config.DB ):
        self.host = host;
        self.port = port;
        self.db = db;

    def connect(self):
        try:
            self.conn = MySQLdb.connect(self.host, self.port, self.user, self.passwd, self.db)
            self.cursor = self.conn.cursor()
        except :
            ## will write to log later
            print "ERR: connect %s:%d %s:%s %s" % self.host, self.port, self.user, self.passwd, self.db

    def query(self, sql):
        try:
            self.curosr.execute(sql)
        except :
            pass

    def escape_string(self, rawsql):
        safe_sql = MySQLdb.escape_string(rawsql)
        return safe_sql

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def closedb(self):

        self.conn.close()

