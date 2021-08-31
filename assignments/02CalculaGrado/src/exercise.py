def calcula_grado(x):
    if x>0.9 and x<=1:
        print ("A" )
    elif x<=0.9 and x>0.8:
        print ("B" )
    elif x<=0.8 and x>0.7:
        print ("C" )
    elif x<=0.7 and x>0.6:
        print ("D" )
    elif x<=0.6 and x>=0.0:
        print ("F" )
    else:
        print ("score incorrecto" ) 
def main():

    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))


if __name__=='__main__':
    main()
