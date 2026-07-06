from grovepi import *
from grove_rgb_lcd import *
import time 
import MySQLdb as sql

conexion = sql.connect(host='localhost',user='admin', passwd='1234',db='mds')
curs = conexion.cursor()

dht_sensor_port = 7 

