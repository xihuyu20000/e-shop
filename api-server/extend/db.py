from typing import Optional

import pymysql
from DBUtils.PersistentDB import PersistentDB

POOL = PersistentDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    closeable=False,
    # 如果为False时， conn.close() 实际上被忽略，供下次使用，再线程关闭时，才会自动关闭链接。如果为True时， conn.close()则关闭链接，那么再次调用pool.connection时就会报错，因为已经真的关闭了连接（pool.steady_connection()可以获取一个新的链接）
    threadlocal=None,  # 本线程独享值得对象，用于保存链接对象，如果链接对象被重置
    host='127.0.0.1',
    port=3306,
    user='root',
    password='admin',
    database='scitools',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)


def fetchall(sql, data):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute(sql, data)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def fetchone(sql, data):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute(sql, data)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def page(tablename: str, queryParams = None):
    pagenum: int = int(queryParams['pageNo'] if 'pageNo' in queryParams.keys() else 1)
    pagesize: int = int(queryParams['pageSize'] if 'pageSize' in queryParams.keys() else 1)

    sql1 = 'SELECT count(*) AS count FROM ' + tablename + ' WHERE 1=1 '
    sql2 = 'SELECT * FROM ' + tablename + ' WHERE 1=1 '

    whereParam = ''
    for key, value in queryParams.items():
        if key and value:
            if key not in ('pageNo', 'pageSize'):
                whereParam += " AND {} LIKE '%{}%'".format(key, value)
        print('查询条件', key,":", value)

    if whereParam:
        sql1 += whereParam
        sql2 += whereParam
    sql2 += ' LIMIT ' + str((pagenum - 1) * pagesize) + ' , ' + str(pagesize)

    print('分页语句', sql2)
    conn = POOL.connection()
    cursor = conn.cursor()

    cursor.execute(sql1)
    result_count = cursor.fetchone()

    cursor.execute(sql2)
    result_all = cursor.fetchall()

    cursor.close()
    conn.close()
    return result_count['count'], result_all


def execute(sql, data):
    conn = POOL.connection()
    cursor = conn.cursor()
    result = cursor.execute(sql, data)
    conn.commit()
    print('执行增删改', sql, data, result)
    cursor.close()
    conn.close()
    return result