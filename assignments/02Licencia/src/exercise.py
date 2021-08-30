
def main(): 

    edad = int(input("Ingresa tu edad: "))

    if edad >= 18:
        ide = str(input("¿Tienes identificación oficial? (s/n):"))
        
        if (ide == 's' or ide == 'S'):
            print('Trámite de licencia concedido')
            
        elif (ide == 'n' or ide == 'N'):
            print('No cumples requisitos')
        
        else:
             print('Respuesta incorrecta')
    
    elif(edad <= 0):
        print('Respuesta incorrecta')
    
    elif edad < 18:
        print('No cumples requisitos')        
if __name__ == '__main__':
    main()

