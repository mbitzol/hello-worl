from collections import deque
cola = deque()
while True:
    
    
    print('1) Agregar documento a la cola de impresion')
    print('2) Imprimir')
    print('3) Salir')
    opcionmenu = input()

    if opcionmenu == '1':
        print('Se encontraron los siguientes archivos en la carpeta actual.')
        print('Ingrese el numero de archivo que desee agregar a la cola: ')
        print('[1] Archivo1.txt')
        print('[2] Archivo2.txt')
        print('[3] Archivo3.txt')
        print('[4] Cancelar')
        documento = input()
        if documento == '1':
            cola.append('Archivo1.txt')
        elif documento == '2':
            cola.append('Archivo2.txt')
        elif documento == '3':
            cola.append('Archivo3.txt')
        print(f'La cola de impresion es: {cola}')
        print('----------------------------------------------')
    elif opcionmenu == '2':
        archivoimpresion = cola.popleft()
        print(f'Se imprimio: {archivoimpresion}')
        print(f'La cola de impresion es: {cola}')
        print('----------------------------------------------')
        if len(cola) == 0:
            print('La cola esta vacia')
            print('----------------------------------------------')
    elif opcionmenu == '3':
        break
    else:
        print('----------------------------------------------')
        print('Digite una opcion')

