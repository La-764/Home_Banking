import csv
cheques=[]

with open('ITBA_test.txt', 'r', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    name_records = list(csv_reader)
    ## extrae datos
    documento=name_records[0]['DNI']

    salida=input("Ingrese pantalla si desea  imprimir por “pantalla” todos los valores que se tienen y  “csv” si desea exportar a un csv").upper()
    if salida == "PANTALLA":
            print("DNI: " + DNI + "\n Tipo:" + Tipo + "\n Estado:" + Estado)
    elif salida == "CSV":
            crearCSV()


print(name_records)
print()
print(name_records[0])
print()
print(name_records[0]['FechaPago'])


for linea in f:
        DNI, Tipo, Estado = linea.rstrip("\n").split(",")
        salida=input("Ingrese pantalla si desea  imprimir por “pantalla” todos los valores que se tienen y  “csv” si desea exportar a un csv").upper()
        if salida == "PANTALLA":
            print("DNI: " + DNI + "\n Tipo:" + Tipo + "\n Estado:" + Estado)
        elif salida == "CSV":
            crearCSV()

def crearCSV():
    with open('ITBA_test.txt', 'w', encoding='utf-8') as  cheques:
        pass
