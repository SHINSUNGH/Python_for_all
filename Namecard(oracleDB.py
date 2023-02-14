import cx_Oracle
try:
    conn = cx_Oracle.connect('SCOTT/TIGER@localhost:1521/xe')
    # conn = cx_Oracle.connect(user = 'SCOTT', password = 'TIGER', dsn = 'localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('select * from dept')
    print(cur.fetchall())
    sql = 'delete from dept where DEPTNO = :1'
    deptno = input('삭제할 부서코드 입력 : ')
    data = (deptno,)
    cur.execute(sql, data)
    conn.commit()
    conn.close()
except Exception as e:
    print(e)