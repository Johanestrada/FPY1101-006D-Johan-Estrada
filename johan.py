'''Este codigo administra el stock de producctos de bodega'''

import os


dicc = {'1': ['Escoba : 5'],
        '2': ['Huevos : 25'],
        '3': ['Leche : 9']}


print('-----------------------------------------------\n------------Administrador de Stock-------------\n-----------------------------------------------')
#bienvenida del codigo
menup = [' 1. Ver stock de producctos\n','2. Añadir nuevo producto\n','3. Ajustar stock\n','4. Eliminar Producto\n','5. Salir\n']

while True:
    for indice, opcion in enumerate(menup):
        print(*menup)
        ans = input('¿Que quieres hacer?')
    if ans == '1':
        os.system('cls')
        for llave, clave in dicc.items():
          print(f'{llave[0], clave[0]}')
    else:
            ans == '2'
            nrepositorio=input('Ingrese el nombre del nuevo producto')
    else:
         ans =='3'
    aproducto = input('Ingrese el nombre del producto a ajustar')
    

