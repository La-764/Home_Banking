import csv
cheques=[]


def crearCSV():
    with open('ITBA_test.txt', 'w', encoding='utf-8') as cheques:
        pass



with open('ITBA_test.txt', 'r', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    name_records = list(csv_reader)
    ## extrae datos
    for line in name_records:
        nro_cheque = (name_records[line]['NroCheque'])
        documento = (name_records[line]['DNI'])
        tipo = (name_records[line]['Tipo'])
        estado = (name_records[line]['Estado'])

    salida=input("Ingrese pantalla si desea  imprimir por “pantalla” todos los valores que se tienen y  “csv” si desea exportar a un csv").upper()
    if salida == "PANTALLA":
            print("DNI: " + documento + "\n Tipo:" + tipo + "\n Estado:" + estado)
    elif salida == "CSV":
            crearCSV()


print(name_records)
print()
print(name_records[0])
print()
print(name_records[0]['FechaPago'])


for linea in f:
    ## hacer verificación de nro de cheque (ID) con dni
        DNI, Tipo, Estado = linea.rstrip("\n").split(",")
        salida=input("Ingrese pantalla si desea  imprimir por “pantalla” todos los valores que se tienen y  “csv” si desea exportar a un csv").upper()
        if salida == "PANTALLA":
            print("DNI: " + DNI + "\n Tipo:" + Tipo + "\n Estado:" + Estado)
        elif salida == "CSV":
            crearCSV()

