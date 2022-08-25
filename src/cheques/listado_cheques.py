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
numeroCuenta = []
valor = []
fechaOrigen = []
fechaPago = []
dt = datetime.now()
ts = datetime.timestamp(dt)


def crearCSV(dni, linea):
    nombreCSV = str(dni)+"_"+str(ts)+".csv"

    NumeroCuenta = numeroCuenta[linea]
    Valor = valor[linea]
    FechaOrigen = fechaOrigen[linea]
    FechaPago = fechaPago[linea]

    csv = open(nombreCSV, "a")
    csv.write(documento[linea]+","+NumeroCuenta + "," +
              Valor + "," + FechaOrigen + "," + FechaPago + "\n")

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

    for item in csvReader:
        nroCheque.append(item['NroCheque'])
        documento.append(item['DNI'])
        tipo.append(item['Tipo'])
        estado.append(item['Estado'])
        numeroCuenta.append(item['NumeroCuentaOrigen'])
        valor.append(item['Valor'])
        fechaOrigen.append(item['FechaOrigen'])
        fechaPago.append(item['FechaPago'])

    filtrarPorDni()
