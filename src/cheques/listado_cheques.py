import csv
from datetime import datetime
from operator import length_hint
from pdb import line_prefix

archivo = input("Ingrese nombre del archivo csv: ")
filtrarDni = input("Ingrese DNI a filtrar: ")
salida=input("Ingrese pantalla si desea  imprimir por “pantalla” todos los valores que se tienen y  “csv” si desea exportar a un csv: ").upper()
chequesFiltrados = []
nro_cheque=[]
documento=[]
tipo=[]
estado=[]
dt = datetime.now()
ts = datetime.timestamp(dt)

def crearCSV(dni,linea):
    nombre_csv = str(dni)+"_"+str(ts)+".csv"

    NumeroCuenta=name_records[linea]['NumeroCuentaOrigen']
    valor=name_records[linea]['Valor']
    FechaOrigen=name_records[linea]['FechaOrigen']
    FechaPago=name_records[linea]['FechaPago']
    if documento[linea] == dni:

        csv = open(nombre_csv, "a")
        csv.write(documento[linea]+","+NumeroCuenta + "," + valor + "," + FechaOrigen + "," + FechaPago + "\n")
            
        csv.close()
    
def error():
    if len(chequesFiltrados) != len(set(chequesFiltrados)):
        print("Error: Existe más de un cheque con el mísmo número de cheque para esta cuenta")    

def filtrarPorDni():
    
    for i in range(0, len(documento)):
        if documento[i] == filtrarDni:
            chequesFiltrados.append(nro_cheque[i])
            if salida == "PANTALLA":
                print("DNI: " + documento[i] + "\n Tipo:" + tipo[i] + "\n Estado:" + estado[i])
            elif salida == "CSV":
                crearCSV(filtrarDni,i)
    error()

with open(archivo, 'r', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    name_records = list(csv_reader)
   
    
    for line in range(0,len(name_records)):
        nro_cheque.append(name_records[line]['NroCheque'])
        documento.append(name_records[line]['DNI'])
        tipo.append(name_records[line]['Tipo'])
        estado.append(name_records[line]['Estado'])
    
    filtrarPorDni()

    
        


