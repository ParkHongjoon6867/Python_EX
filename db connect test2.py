import cx_Oracle

sql = " select sysdate as date_txt from dual"

#                           USER + '/'+PASSWD + '@'+HOST + ':'+PORT + '/' +DB
# conn = cx_Oracle.connect('python/python@localhost:1521/xe')
conn = cx_Oracle.connect('LocalDB/system@localhost:1521/xe')
cs = conn.cursor()
rs = cs.execure(sql)

print(" 항목 시간 : ", data_txt)

