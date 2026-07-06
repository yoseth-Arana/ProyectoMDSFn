from grovepi import *
from grove_rgb_lcd import *
import time 
import MySQLdb as sql

conexion = sql.connect(host='localhost',user='admin', passwd='1234',db='mds')
curs = conexion.cursor()

dht_sensor_port = 7 

while True:
    try:
        [Temp, humed] = dht(dht_sensor_port, 0) 
        print("Temp =", Temp, "C\tHumidity =", humed, "%")

        temp = str(Temp)
        humed = str(humed)

        setRGB(0, 128, 64)  
        setRGB(0,255,0)
        setText("Temp: " + temp + "C     Humidity: " + humed + "%")
        
        curs.execute("insert into DatosH (temp, humed) values ("+ temp + ","+ humed +");")

    except sql.Error as e:
        print("Error:", e)
        
    curs.execute("select * from DatosH")
    for temp,humed in curs.fetchall():
        print(temp, humed)
        conexion.commit()
    #conexion.close()