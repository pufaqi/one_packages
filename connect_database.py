#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:pufaqi
#loftybay@163.com
import pymysql
def sqlmysql(data):
    db = pymysql.connect("ip","root","pufaqi999,.QAZ","pytest")
    cursor = db.cursor ()
    sql = """
        %s
    """
    try:
        cursor.execute(sql%data)
        db.commit()
    except:
        db.rollback()
    db.close
