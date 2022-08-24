import csv
from datetime import datetime
from operator import length_hint
from pdb import line_prefix

archivo = input("Ingrese nombre del archivo csv: ")
filtrarDni = input("Ingrese DNI a filtrar: ")
salida = input("Ingrese pantalla si desea  imprimir por “pantalla” todos los valores que se tienen y  “csv” si desea exportar a un csv: ").upper()
chequesFiltrados = []
nroCheque = []
documento = []
tipo = []
estado = []
dt = datetime.now()
ts = datetime.timestamp(dt)


def crearCSV(dni, linea):
    nombreCSV = str(dni)+"_"+str(ts)+".csv"

    NumeroCuenta = nameRecords[linea]['NumeroCuentaOrigen']
    valor = nameRecords[linea]['Valor']
    FechaOrigen = nameRecords[linea]['FechaOrigen']
    FechaPago = nameRecords[linea]['FechaPago']

    csv = open(nombreCSV, "a")
    csv.write(documento[linea]+","+NumeroCuenta + "," +
              valor + "," + FechaOrigen + "," + FechaPago + "\n")

    csv.close()


def errorPorNumeroDeCheque():
    if len(chequesFiltrados) != len(set(chequesFiltrados)):
        print(
            "Error: Existe más de un cheque con el mísmo número de cheque para esta cuenta")


def filtrarPorDni():
    try:
        for i in range(0, len(documento)):
            if documento[i] == filtrarDni:
                chequesFiltrados.append(nroCheque[i])
                if salida == "PANTALLA":
                    print("DNI: " + documento[i] + "\n Tipo:" +
                    tipo[i] + "\n Estado:" + estado[i])
                if salida == "CSV":
                    crearCSV(filtrarDni, i)
        errorPorNumeroDeCheque()
    except:
        raise


with open(archivo, 'r', encoding='utf-8') as f:
    csvReader = csv.DictReader(f)
    nameRecords = list(csvReader)

    for line in range(0, len(nameRecords)):
        nroCheque.append(nameRecords[line]['NroCheque'])
        documento.append(nameRecords[line]['DNI'])
        tipo.append(nameRecords[line]['Tipo'])
        estado.append(nameRecords[line]['Estado'])

    filtrarPorDni()
