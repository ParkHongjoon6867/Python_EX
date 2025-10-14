import logging
import sys
import pymysql

#host = "mysql.hostname.com"
host = "localhost"
port = "3306"
database = "phjtestdb"
username = "root"
password = "phjoon6867~"


def main():

    try:
    #DB Connection 생성
        conn = pymysql.connect(host, user=username, passwd=password, db=database, use_unicode=True, charset='utf8')
        cursor = conn.cursor()

    except:
        logging.error("")
        sys.exit(1)

	
    # cursor.execute("show tables")
    #print(cursor.fetchall())

    query = "insert into phj0001 (a) value ('1');"
    
    cursor.execute(query)
    conn.commit()
    
    conn.close()
    
if __name__ == '__main__':
	main()