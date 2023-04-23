import csv
import json
import uuid

# Abrimos el archivo CSV de entrada y el archivo JSON de salida
with open('input.csv', 'r') as csv_file, open('output.json', 'w') as json_file:

    # Leemos el archivo CSV con csv.reader
    csv_reader = csv.reader(csv_file)

    # Saltamos la primera fila que contiene los títulos de las columnas
    next(csv_reader)

    # Procesamos cada línea del CSV
    for row in csv_reader:
        # Creamos un diccionario con los valores correspondientes
        data = {
            "id": str(uuid.uuid4()),
            "title": row[0],
            "content": row[1],
            "createdAt": 0,
            "$types": {"createdAt": "date"}
        }

        # Convertimos el diccionario a una cadena en formato JSON
        json_data = json.dumps(data)

        # Escribimos la cadena JSON en el archivo de salida
        json_file.write(json_data + ',\n')

