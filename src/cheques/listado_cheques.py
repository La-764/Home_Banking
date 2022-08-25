import sys
import csv
from datetime import datetime

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
        print("Error: Existe más de un cheque con el mismo número de cheque para esta cuenta")


def filtrarPorDni():
    try:
        for i in range(0, len(documento)):
            if documento[i] == sys.argv[2]:
                chequesFiltrados.append(nroCheque[i])
                if sys.argv[3].upper() == "PANTALLA":
                    print("DNI: " + documento[i] + "\n Tipo:" +
                    tipo[i] + "\n Estado:" + estado[i])
                if sys.argv[3].upper() == "CSV":
                    crearCSV(sys.argv[2], i)
        errorPorNumeroDeCheque()
    except:
        raise


with open(sys.argv[1], 'r', encoding='utf-8') as f:
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
