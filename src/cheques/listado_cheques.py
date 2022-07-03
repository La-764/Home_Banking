import csv
from datetime import datetime
from operator import length_hint

archivo = input("Ingrese nombre del archivo csv: ")
filtrarDni = input("Ingrese DNI a filtrar: ")
salida=input("Ingrese pantalla si desea  imprimir por “pantalla” todos los valores que se tienen y  “csv” si desea exportar a un csv").upper()
chequesFiltrados = []

def crearCSV(nombre_archivo, dni):
    nombre_csv = str(dni) + str(datetime.now())
    cheques = open(nombre_archivo, 'r')
    for linea in cheques:
        DNI = linea.rstrip("\n").split(",")
        if DNI == dni:
            NumeroCuenta, Valor, FechaOrigen, FechaPago = linea.rstrip("\n").split(",")
            csv = open(nombre_csv.csv, "w")
            csv.write(NumeroCuenta + "," + Valor + "," + FechaOrigen + "," + FechaPago + "\n")
            csv.close
    cheques.close()



with open(archivo, 'r', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    name_records = list(csv_reader)
    ## extrae datos
    for line in name_records:
        nro_cheque = (name_records[line]['NroCheque'])
        documento = (name_records[line]['DNI'])
        tipo = (name_records[line]['Tipo'])
        estado = (name_records[line]['Estado'])
    


print(name_records)
print()
print(name_records[0])
print()
print(name_records[0]['FechaPago'])


def filtrarPorDni():
    for i in range(0, len(documento)):
        if documento[i] == filtrarDni:
            if salida == "PANTALLA":
                print("DNI: " + documento[i] + "\n Tipo:" + tipo[i] + "\n Estado:" + estado[i])
            elif salida == "CSV":
                crearCSV(archivo, filtrarDni)

