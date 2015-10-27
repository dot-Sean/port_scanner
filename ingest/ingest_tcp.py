#!/usr/bin/python

import os.path
import sys
import mysql.connector

tcp_ingest = 'data/tcp_ports.txt';

print '\n\n';

# Check if files exist
if os.path.exists(tcp_ingest) == False:
	print 'The file containing your tcp ports, located here: ' + tcp_ingest + ' is missing.';
	print 'Please correct this, and re-run this script.';
	print 'System shutting down...';
	sys.exit(1);

# Files exist, let's start the ingest loop
with open(tcp_ingest) as input_file:
	for i, line in enumerate(input_file):
		temp = line.split(',');	
		connection = mysql.connector.connect(user='jwebster_dev', database='jwebster_dev');
		cursor = connection.cursor()
		row = ("INSERT INTO tcp_ports (protocol, port, description) VALUES (%s, %s, %s)");
		data = (temp[0], temp[1], temp[2]);
		cursor.execute(row, data);
		row_no = cursor.lastrowid;
		print line,
print "{0} line(s) printed".format(i+1);
