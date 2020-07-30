import pymysql
from datetime import datetime

def search(nombre,temp):
    name = nombre
    fech = datetime.now()
    db = pymysql.connect(host='localhost', user='root', passwd='sistemas', db='delfin2020')
    cursor = db.cursor()
    id = cursor.execute("SELECT id_empleado FROM empleados WHERE nombre = %s;", (name,))
    cursor.execute("SELECT * FROM chicho WHERE id_empleados = %s;", (id,))
    if cursor.fetchone():
        # Significa que es salida
        update_exit(id,fech)
        cursor.close()
        return 0
    else:
        #Significa que es entrada
        #Boolean Temp
        insert_information(id,fech,temp)
        return 1

def update_exit(id,fech):
    db = pymysql.connect(host='localhost', user='root', passwd='sistemas', db='delfin2020')
    cursor = db.cursor()
    fechaE = cursor.execute("SELECT HoraE FROM chicho WHERE id_empleado = %s;", (id,))
    fE = fechaE.split(' ')[0]
    fS = fech.split(' ')[0]
    if fE.equals(fS):
        cursor.execute("UPDATE chicho SET HoraS = %s WHERE id_empleado = %s;", (fech,id))
        cursor.close()
        db.commit()


def insert_information(id,date,temp):
    db = pymysql.connect(host='localhost', user='root', passwd='sistemas', db='delfin2020')
    cursor = db.cursor()
    cursor.execute("INSERT INTO chicho (id, id_empleado, HoraE, Temp) VALUES (%s, %s, %s, %s)", (0, id, date, temp))
    cursor.close()
    db.commit()

