#!/usr/bin/python
# coding=utf-8
"""
@Author: Zhao Fei
@Time: 4/17/2019 9:23 AM
@File: MySqlite3.py
"""

import sqlite3

# 连接数据库
db = sqlite3.connect('mydatabase.db')
cur = db.cursor()
table = 'mytable'

# 创建表
def create_table():
    try:
        cur.execute('''create table mytable (
            id int primary key not null check(id >= 0),
            column1 text default 'data default'
        );''')
        db.commit()
    except:
        print('table mytable already exists')


def alter_table():
    sql = 'alter table mytable add column column2 int default 0'
    cur.execute(sql)
    db.commit()

def drop_table():
    sql = 'drop table mytable;'
    cur.execute(sql)
    db.commit()


# 插入数据
def insert_data():
    # cur.execute('insert into mytable values (4, ?);', ('data41',))    可以
    # cur.execute('insert into mytable values (?, ?);', (4, 'data41'))  可以
    # cur.execute('insert into mytable values (?, "data51");', (5,))    可以
    # cur.execute('insert into mytable values (?, "data61");', [6])     可以
    # cur.execute('insert into mytable values (7, ?);', ['data71'])     可以
    id = 6
    data = "'data61'"
    # cur.execute('insert into mytable values (?, ?);', [id, data])     可以
    sql = 'insert into ' + table + ' values ( ' + str(id) + ', ' + data + ');'
    cur.execute(sql)
    cur.execute('insert into mytable (id) values (7);')
    cur.execute('insert into mytable (id) values (8);')
    cur.execute('insert into mytable (id) values (9);')
    cur.execute('insert into mytable (id) values (10);')
    cur.execute('insert into mytable (id) values (11);')

    db.commit()

# 查询数据
def select_data():
    result = cur.execute('select distinct * from mytable order by id limit 3 offset 1;')
    # print(cur.fetchone()) #游标位置变了

    print('id\tcolumn1')
    print('--\t-------')
    for row in result:
        print(str(row[0]) + '\t' + str(row[1]))
        # print(row[0])
    print('--------select over--------')


def delete_data():
    sql = 'delete from mytable where column1 like "data%";'
    cur.execute(sql)
    db.commit()


def update_data():
    sql = 'update mytable set column1="data111" where id = 7;'
    cur.execute(sql)
    db.commit()


def refer_tables():
    cur.execute('select name from sqlite_master where type="table";')
    print(cur.fetchall())


def create_view():
    cur.execute('create view myview as select id from mytable;')
    db.commit()

def select_view():
    cur.execute('select * from myview;')
    print(cur.fetchall())


def delete_view():
    cur.execute('drop view myview;')

if __name__ == '__main__':
    create_table()
    refer_tables()
    insert_data()
    select_data()
    update_data()
    select_data()
    create_view()
    select_view()
    delete_view()
    delete_data()
    select_data()
    drop_table()
    refer_tables()
    result = cur.execute("select strftime('%Y-%m-%d %H:%M:%S','now', 'localtime');")
    for row in result:
        print(row)
    db.close()
