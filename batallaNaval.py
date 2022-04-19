#armado de una batalla naval 
#armar una matriz de 10*10
column,row=10,10
tablero=[[0]*row for _ in range(column)]

tablero[0][1]="X"
tablero[0][2]="X"
tablero[0][3]="X"
tablero[5][5]="X"
tablero[6][5]="X"
tablero[7][5]="X"
tablero[8][5]="X"


print("JUEGO DE LA BATALLA NAVAL")
print("Usted cuenta con 4 vidas para este juego si no logra bombardear, debera indicar las coordenadas donde desee tirar la bomba \n recuerde que el tablero es de 10*10")

vida = 4
while vida != 0:
    try:
        coord1 = int(input("Ingrese la primer coordenadas a donde dirige la bomba: "))
        coord2 = int(input("Ingrese la segunda coordenadas a donde dirige la bomba: "))
    except:
        print ("Esto no es una coordenada, recorda que debe ser un numero del 0 al 10. No te desanimes, tu vida sigue intacta vuelve a intentarlo")
    else:
        if tablero[coord1][coord2]== "X":
            print( "ME DISTE!")
        else:
            vida= vida-1
            print(f"SEGUI INTENTANTO!! te quedan {vida} vidas")
            if vida == 0:
                print("FIN DEL JUEGO")

#print(barco_1)



    #for i in range( 0,10):
        #for j in range (0,10):
            #if i > 5 and i<=9 and j==1:
                #print(1, end = " ")
                #return(i,j)
            #elif i==3 and j<7:
                #print(1, end =" ")
                #return(i,j)
            #elif i ==9 and 3>=j<7:
                #print(1, end = " ")
                #return(i,j)
            #else : 
                #print("a", end=" ")
        #print("\n")
#print(batallaNaval)

#print("JUEGO DE LA BATALLA NAVAL")
#print("Usted cuenta con 4 vidas para este juego, debera indicar las coordenadas donde desee tirar la bomba \n recuerde que el tablero es de 10*10")

#vida = 0
#while vida < 4:
    #coord1 = int(input("Ingrese la primer coordenadas a donde dirige la bomba: "))
    #coord2 = int(input("Ingrese la segunda coordenadas a donde dirige la bomba: "))
    #bomba = [coord1,coord2]
    #vida= vida+1
    
    #barco1=batallaNaval(7,1)
    #if bomba == barco1:
        #print ("ME DISTE)")
    #else:
        #print("Segui intentando")