import os
import time

#Variables
opc1=0
opc2=0
sectores = ['Centro', 'Colina', 'Industrias','Santiago','San Joaquín']
nombre=''
direccion=''
comuna=''
cant_5kg=0
cant_15kg=0
cant_45kg=0
Pedidos = []

#Funciones

def guardarPedidos(nombre,direccion,comuna,cant_5kg,cant_15kg,cant_45kg):
    registrar = [nombre,direccion,comuna,cant_5kg,cant_15kg,cant_45kg]
    Pedidos.append(registrar)
    os.system('cls')
    print('---------------------')
    print('Pedido Registrado')
    print('---------------------')
    time.sleep(2)

def listar():
    for pedido in Pedidos:
                print(f'Nombre: {pedido[0]}, direc.: {pedido[1]}, comuna: {pedido[2]}, cant. Cil. 5kg: {pedido[3]}, cant. Cil. 15kg: {pedido[4]}, cant. Cil. 45kg: {pedido[5]}')

def errorIngreso():
    os.system('cls')
    print('---------------------')
    print('La opcion ingresada no es valida')
    print('---------------------')
    time.sleep(2)

def listarSectores():
    index = 1
    for sector in sectores:
        print(f'[{index}] {sector}')
        index +=1
    try:
        indexSector = int(input('--->>> '))
    except:
            errorIngreso()
    comuna = sectores[indexSector-1]
    return comuna

def ingresarDatos():
    print('---------------------')
    print('Ingrese los datos del pedido: ')
    nombre=input('Ingrese el nombre del cliente: ')
    direccion=input('Ingrese la dirección del cliente: ')
    print('Selecciones su sector: ')
    comuna = listarSectores()
    menu2=True
    cant_5kg=0
    cant_15kg=0
    cant_45kg=0
    while menu2:        
        print('---------------------')
        print('Seleccione una opcion: ')
        print(f'[1]	Cilindro de 5 kilo\t [Cantidad: {cant_5kg}]')
        print(f'[2]	Cilindro de 15 kilo\t [Cantidad: {cant_15kg}]')
        print(f'[3]	Cilindro de 45 kilo\t [Cantidad: {cant_45kg}]')
        print('[4]	Guardar')
        print('---------------------')
        try:
            opc2=int(input('-->>> '))
        except:
            errorIngreso()
        
        if opc2 < 1 or opc2 > 4:
            errorIngreso()
        else:
            if opc2 == 1:
                try:
                    cant_5kg=int(input('Ingrese el numero de cilindros que necesita:  '))
                except:
                    errorIngreso()
            elif opc2 == 2:
                try:
                    cant_15kg=int(input('Ingrese el numero de cilindros que necesita:  '))
                except:
                    errorIngreso()
            elif opc2 == 3:
                try:
                    cant_45kg=int(input('Ingrese el numero de cilindros que necesita:  '))
                except:
                    errorIngreso()
            elif opc2 == 4:
                os.system('cls')
                print('---------------------')
                print('Datos guardados!!!')
                print('---------------------')
                time.sleep(2)
                menu2 = False
    return(nombre,direccion,comuna,cant_5kg,cant_15kg,cant_45kg)

def imprimir(comuna):
    with open('Hoja de Ruta.txt','w', encoding='utf-8') as ruta:
        for pedido in Pedidos:
            if comuna == pedido[2]:
                linea = f'Nombre: {pedido[0]}, direc.: {pedido[1]}, comuna: {pedido[2]}, cant. Cil. 5kg: {pedido[3]}, cant. Cil. 15kg: {pedido[4]}, cant. Cil. 45kg: {pedido[5]}'
                ruta.write(linea + '\n')
    os.system('cls')
    print('---------------------')
    print('Archivo creado')
    print('---------------------')
    time.sleep(2)

def main():
    menu1=True
    while menu1:
        print('---------------------')
        print('Seleccione una opcion: ')
        print('[1]	Registrar pedido')
        print('[2]	Listar los todos los pedidos')
        print('[3]	Imprimir hoja de ruta')
        print('[4]	Salir del programa')
        print('---------------------')

        try:
            opc1=int(input('-->>> '))
        except:
            errorIngreso()
        
        if opc1 < 1 or opc1 > 4:
            errorIngreso()
        else:
            if opc1 == 1:
                nombre,direccion,comuna,cant_5kg,cant_15kg,cant_45kg=ingresarDatos()
                guardarPedidos(nombre,direccion,comuna,cant_5kg,cant_15kg,cant_45kg)            
            elif opc1 == 2:
                listar()
            elif opc1 == 3:
                print('---------------------')
                print('Seleccione el sector para imprimir la hoja de ruta: ')
                comuna = listarSectores()
                imprimir(comuna)
            elif opc1 == 4:
                os.system('cls')
                print('---------------------')
                print('Hasta Luego!!!!')
                print('---------------------')
                menu1 = False
                time.sleep(2)

main()