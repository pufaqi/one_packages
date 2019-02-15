#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:pufaqi
#loftybay@163.com
import connect_database
data="create table nmbs(id int,username int)"
#data="select * from user "
connect_database.sqlmysql(data)