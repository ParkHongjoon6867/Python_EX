/* DB Connect test 20211006 */

import Oracle
import cx_Oracle as ora
from cx_Oracle import Error as oraErr
import pandas as pd

#데이터베이스 정보 입력해서 connection
def connDB(HOST, DB, PORT, USER, PASSWD):
    try:
        conn_str = USER + '/'+PASSWD + '@'+HOST + ':'+PORT + '/' +DB
        oraConn = ora.connect(conn_str)
    except oraErr as e :
        print("Error while connecting to {}".format(DB).format(e))
    return oraConn  

#데이터베이스 connection과 SQL문을 파라메터로 받아서 결과 반환
def fetchDB(sql_Select, oraCOnn):

oraCursor = oraConn.cursor()
oraResult = oraCursor.execute(sql_Select)
rows = oraCursor.getchall()

return(rows)

