import csv
from operator import length_hint

archivo = input("Ingrese nombre del archivo csv: ")
filtrarDni = input("Ingrese DNI a filtrar: ")
salida=input("Ingrese pantalla si desea  imprimir por “pantalla” todos los valores que se tienen y  “csv” si desea exportar a un csv").upper()
chequesFiltrados = []
def crearCSV():
    with open('ITBA_test.txt', 'w', encoding='utf-8') as cheques:
        pass



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


def filtrarPorDni(filtrarDni):
    
    for i in range(0, lenght(documento)):
        if documento[i] == filtrarDni:
            if salida == "PANTALLA":
                print("DNI: " + documento[i] + "\n Tipo:" + tipo[i] + "\n Estado:" + estado[i])
            elif salida == "CSV":
                crearCSV()

