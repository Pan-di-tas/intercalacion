def intercalacion_archivos(archivo1, archivo2, archivo_salida):
    """
    Realiza la intercalación de dos archivos ordenados y guarda el resultado en un tercer archivo.
    """
    with open(archivo1, 'r') as f1, open(archivo2, 'r') as f2, open(archivo_salida, 'w') as salida:
        # Leer la primera línea de cada archivo
        linea1 = f1.readline().strip()
        linea2 = f2.readline().strip()

        # Mientras haya datos en alguno de los archivos
        while linea1 or linea2:
            if linea1 and (not linea2 or int(linea1) < int(linea2)):
                # Si `linea1` es menor o `linea2` está vacía, escribir `linea1`
                salida.write(linea1 + '\n')
                linea1 = f1.readline().strip()  # Leer siguiente línea de archivo1
            else:
                # Si `linea2` es menor o `linea1` está vacía, escribir `linea2`
                salida.write(linea2 + '\n')
                linea2 = f2.readline().strip()  # Leer siguiente línea de archivo2

# Crear archivos de prueba (ya ordenados)
with open('archivo1.txt', 'w') as f:
    f.write('\n'.join(['1', '3', '5', '7', '9']))
with open('archivo2.txt', 'w') as f:
    f.write('\n'.join(['2', '4', '6', '8', '10']))

# Ejecutar la intercalación
intercalacion_archivos('archivo1.txt', 'archivo2.txt', 'resultado_intercalacion.txt')
