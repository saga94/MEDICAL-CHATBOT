
import mysql.connector
class DBConnection:
    @staticmethod
    def getConnection():
        database = mysql.connector.connect(host="localhost", user="root", passwd="SAIGANESH2004", db='Medicalbot',port= '3306')
        return database


if __name__=="__main__":
    print(DBConnection.getConnection())