#!/usr/bin/env python3

import cx_Oracle
import csv
#import sys

ver = '1.0.3'
db = 'register/Reg@12c_nas'

def send(message,systemid):
    try:
         con = cx_Oracle.connect(db)
         cursor = con.cursor()

         #cursor.execute("begin  ms_tools.ms_ins(p_msg_body =>'"+message+"', p_system_id =>"+systemid+",p_error =>"+p_error+ "); end ;")
         #cursor.execute("begin ms_tools.ms_ins(:1,:2,:3); end;", [message,systemid, p_error])

         outVal = cursor.var(str)
         cursor.callproc('ms_tools.ms_ins', [message,systemid, outVal])
         print(outVal.getvalue())
         con.commit()
         return outVal.getvalue()
    except cx_Oracle.DatabaseError as e:
         print("There is a problem with Oracle", e)

    finally:
         if cursor:
              cursor.close()
         if con:
              con.close()

def get_data(type,key,fname):
     con = cx_Oracle.connect(db)
     cursor = con.cursor()
     ref_cursor = con.cursor()
     cursor.callproc("garden.get_plot_data_cur", [type, key,7, ref_cursor])

     with open(fname, mode='w') as data_file:
          data_writer = csv.writer(data_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
          for row in ref_cursor:
              data_writer.writerow([row[0],row[1]])

def get_plot(fname):
     con = cx_Oracle.connect(db)
     cursor = con.cursor()
     ref_cursor = con.cursor()
     cursor.callproc("garden.get_plot_file_cur", [ref_cursor])

     with open(fname, mode='w') as data_file:
          data_writer = csv.writer(data_file, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
          for row in ref_cursor:
              data_writer.writerow([row[0],row[1]])
