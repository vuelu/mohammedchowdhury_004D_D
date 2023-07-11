import os 
import numpy as np
import pruebafun as fn
matriz=np.empty([10,4],type (int))
matriz2=np.empty([10,4],type (int))
op=0
ruts=[]
suma=0
dep=0
ganancias=[]
fn.llenar(matriz,matriz2)

while(True):
    os.system("cls")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    op=fn.valop(op)
    
    if(op==1):
        os.system("cls")
        tipo=fn.valiatipo(dep)
        dep=fn.validadep()
        cc=fn.disponible(matriz,dep)
        if(cc):
            print(" Departamento Disponible: ", tipo,dep)
            pagar=fn.comprardpto(matriz,tipo,dep,ruts)
            print(" Usted debera pagar un total de : UF,", pagar)
            input("<<Enter>> para continuar")
 
    if(op==2):
        os.system("cls")
        fn.mostrarDisponibles(matriz)
        os.system("pause")
    
    if(op==3):
        os.system("cls")
        fn.verlistado(ruts)
        os.system("pause")

    if(op==4):
        os.system("cls")
        fn.mostrargan(ganancias)
        if(suma==0):
            print("\t No se han vendido pasajes aún")
    
    if(op==5):
        os.system("cls")
        print("Adiooos!! ¡¡Que le vaya BIEEN!!")

    
