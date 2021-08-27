
def main(): 

    edad = int(input("Ingresa tu edad: "))

    if edad >= 18:
        ide = str(input("¿Tienes identificacion oficial? (s/n)"))
        
        if (ide == 's'):
            print('Trámite de licencia concedido')
            
        elif (ide == 'n'):
            print('No cumples requisitos')
        
        else:
             print('Respuesta incorrecta')
    
    
    
    elif(edad < 0):
        print('Respuesta incorrecta')
    
    
    else:
        print('No cumples con los requisitos') 
        
    

