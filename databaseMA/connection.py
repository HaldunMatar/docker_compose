import time
import mysql.connector
import sys
sys.path.append('../../OBJECT_DETECTION')

from setting import *

global ipDBsever 
ipDBsever='100.103.105.34'
# if not local :
#     #ipDBsever='100.98.164.136'
#     ipDBsever='100.74.149.25'
#     ipDBsever='100.98.164.136'
    

#     ipDBsever='100.103.105.34'
    
#     #ipDBsever='localhost' 
#     ipDBsever='100.103.105.34'
#     ipDBsever='100.74.149.25' 
#     ipDBsever='100.103.105.34' 
#     ipDBsever='100.94.180.13'   

try:
    
    print(' new strat ')
except Exception :
    print(Exception)

def get_connection():
    
    #host='172.17.0.2'
    host='host.docker.internal'
    database='MADB'
    password='Password123$'
    user='dba' 
   
    host_name= get_host_name()
    
   
    if 1==1:
        print('get_connection test' , ' hostname ',host_name )
        #if(not is_docker):
        # host='127.0.0.1'
        # database='MADB'
        # password='12345678'
        # user='root' 
        time.sleep(10)
        host='192.168.100.10'
        database='madb'
        password='Password123$'
        user='dba' 
        # time.sleep(10)
        
        return mysql.connector.connect(
                host=host,
                database=database,
                password=password,
                user=user                               
                )
        
                                     
