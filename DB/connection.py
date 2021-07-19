import pyodbc as pyodbc

class Connection:

    DB_NAME = "tasks-app"
    SERVER = "."

    dsn = r"DRIVER={ODBC Driver 17 for SQL Server};SERVER="+SERVER+";DATABASE="+DB_NAME+";Trusted_Connection=yes;"

    def Connect(self):
        try:
            conn = pyodbc.connect(self.dsn,autocommit=True)
            return conn
        except Exception as e:
            return f"Error when trying to connect to DB {e}"

    def Select(self,sp):
        conn = self.Connect()
        cursor = conn.cursor()

        try:
            if len(sp) > 1:
                DB_Data = cursor.execute(sp[0],sp[1:])
            else:
                DB_Data = cursor.execute(sp[0])

            return list(DB_Data)
        except Exception as e:
            return f"Error {e}"

    def DML(self,dml):
        conn = self.Connect()
        cursor = conn.cursor()

        try:
            r = cursor.execute(dml[0],dml[1:]).rowcount
            if r > 0:
                return True
        except:
            return False