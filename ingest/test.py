#!/usr/bin/python

import os.path
import sys
import mysql.connector

cnx = mysql.connector.connect(user='jrwebster_dev', password='jrwebster_dev', database='tcp_ports', host='localhost');
cursor = cnx.cursor()

query = "SELECT count(*) from tcp_ports";

cursor.execute(query);
