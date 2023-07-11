import os
import numpy as np

def llenar(matriz,matriz2):
    p=1
    for i in range (10):
        for j in range (4):
            matriz[i,j]=p
            matriz2[i,j]=p
            p+=1

def valop(op):
    op=0
    while(True):
        try:
            op=int(input("   Elija opción: "))
            if(op>=1 and op<=6):
                break
            else:
                print("Debe ingresar una opción entre 1 y 6")
        except ValueError:
            print("Debe ingresar un número entero")
    return op 


def mostrarDisponibles(matriz):
    os.system("cls")
    for i in range(10):
        print("\n") 
        for j in range(4):
            if(j==0 or j==1):
                print("\t",matriz[i,j], end=" ")
            else:
                print("\t",matriz[i,j], end=" ")
    print("\n\n")
            
def valiatipo(tip):
    os.system("cls")
    tip=""
    while(len(tip)<=0):
        print()
        print("Seleccione el tipo A/B/C/D")
        tip=input(" Elija un tipo: ").lower()
        if(tip!="a" and tip!="b" and tip!="c" and tip!="d"):
            print("Error, debe ingresar un tipo valido")
            tip=""
    return tip

def validadep():
    dep=0
    while(True):
        try:
            dep=int(input(" Ingrese número de dep entre 1 y 10: "))
            if(dep>=1 and dep<=10):
                break
            else:
                print("Error debe ingresar un dep entre 1 y 10")
        except ValueError:
            print("Debe ser un número entero")
    return dep 

def disponible(matriz,dep):
    for i in range(10):
        for j in range(4):
            if(dep==matriz[i,j]):
                return True
    return False

def comprardpto(matriz,tip,dep,ruts):
    if(tip=="a"):
        pago=3800
    if(tip=="b"):
        pago=3000
    if(tip=="c"):
        pago=2800
    if(tip=="d"):
        pago=3500
    for i in range(10):
        for j in range(4):
            if(dep==matriz[i,j]):
                while(True):
                    while(True):
                        try:
                            rut=int(input(" Ingrese su RUN "))
                            if(rut<99999999):
                                print(" Error, el run debe tener minimo 8 digitos ")
                            else:
                                break
                        except ValueError:
                            print("Debe ser numeros enteros")
                    if(len(ruts)>0):
                        sw=0
                        for y in range(len(ruts)):
                            if(rut==ruts[y]):
                                sw=1
                        if(sw==1):
                            print("El rut ya esta registrado ")
                        else:
                            ruts.append(rut)
                            break
                    else:
                        ruts.append(rut)
                        break           

    return pago
def verlistado(r):
    r.sort()
    print("Listado de pasajeros del avión ordenados de menor a mayor ")
    print("\t",r)

def mostrargan(matriz):
    suma=0
    for i in range(10):
        for j in range(4):
            if(matriz[i,j]!=0 and matriz[i,j]>40):
                suma+=matriz[i,j]
                    
                

