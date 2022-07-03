import csv
with open('ITBA_test.txt', 'r', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    name_records = list(csv_reader)

print(name_records)
print()
print(name_records[0])
print()
print(name_records[0]['FechaPago'])
