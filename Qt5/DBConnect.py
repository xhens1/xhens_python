import pymysql

def select(search, where_1="", where_2=""):
    conn = pymysql.connect(host='SQL_IP', port=60002, user='아이디', password='비번', db='Qt5_test', charset='utf8')
    curs = conn.cursor()
    sql = "select * from " + search
    if where_1 != "":
        sql = sql + " where " + where_1 + " = '" + where_2 + "'"

    curs.execute(sql)

    rows = curs.fetchall()
    conn.close()

    return rows

def init_name():
    conn = pymysql.connect(host='SQL_IP', port=60002, user='아이디', password='비번', db='Qt5_test', charset='utf8')
    curs = conn.cursor()
    sql = "select name from attack;"
    curs.execute(sql)

    rows = curs.fetchall()
    conn.close()

    return rows

def search_combo(search):
    conn = pymysql.connect(host='SQL_IP', port=60002, user='아이디', password='비번', db='Qt5_test', charset='utf8')
    curs = conn.cursor()
    sql = "select explanation, target from attack where name = '" + search + "';"
    curs.execute(sql)

    rows = curs.fetchall()
    conn.close()

    return rows

def search_place(search):
    conn = pymysql.connect(host='SQL_IP', port=60002, user='아이디', password='비번', db='Qt5_test', charset='utf8')
    curs = conn.cursor()
    sql = "select target_name from target where No = " + search + ";"
    curs.execute(sql)

    rows = curs.fetchall()
    conn.close()

    return rows

def insert_place(insert):
    conn = pymysql.connect(host='SQL_IP', port=60002, user='아이디', password='비번', db='Qt5_test', charset='utf8')
    curs = conn.cursor()
    sql = "insert into target(target_name) values('" + insert + "');"

    curs.execute(sql)
    conn.commit()
    print(sql)
    conn.close()

def init_place():
    conn = pymysql.connect(host='SQL_IP', port=60002, user='아이디', password='비번', db='Qt5_test', charset='utf8')
    curs = conn.cursor()
    sql = "select No, target_name from target;"
    curs.execute(sql)

    rows = curs.fetchall()
    conn.close()

    return rows

def insert_explan(name, explanation, target):
    conn = pymysql.connect(host='SQL_IP', port=60002, user='아이디', password='비번', db='Qt5_test', charset='utf8')
    curs = conn.cursor()
    sql = "insert into attack(name, explanation, target) values('" + name + "', '" + explanation + "', '" + target + "');"

    curs.execute(sql)
    conn.commit()
    print(sql)
    conn.close()