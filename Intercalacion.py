def intercalacion_archivos(archivo1, archivo2, archivo_salida):
  
    with open(archivo1, 'r') as f1, open(archivo2, 'r') as f2, open(archivo_salida, 'w') as salida:
        
        linea1 = f1.readline().strip()
        linea2 = f2.readline().strip()

        
        while linea1 or linea2:
            if linea1 and (not linea2 or int(linea1) < int(linea2)):
                
                salida.write(linea1 + '\n')
                linea1 = f1.readline().strip()  
            else:
               
                salida.write(linea2 + '\n')
                linea2 = f2.readline().strip()  


with open('archivo1.txt', 'w') as f:
    f.write('\n'.join(['1', '3', '5', '7', '9']))
with open('archivo2.txt', 'w') as f:
    f.write('\n'.join(['2', '4', '6', '8', '10']))


intercalacion_archivos('archivo1.txt', 'archivo2.txt', 'resultado_intercalacion.txt')
