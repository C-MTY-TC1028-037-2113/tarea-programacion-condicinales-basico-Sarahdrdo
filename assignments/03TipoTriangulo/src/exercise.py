
def main():

    lado1 = int(input("Ingresa la medida del lado 1: "))
    lado2 = int(input("Ingresa la medida del lado 2: "))
    lado3 = int(input("Ingresa la medida del lado 3: "))
    
    
    if (lado1 <= 0):
        print('NO ES TRIANGULO')
        
    elif (lado2 <= 0):
        print('NO ES TRIANGULO')
    
    elif(lado3 <= 0):
        print('NO ES TRIANGULO')
        
    else:
        
        
        
        if (lado1 > lado2):
            
            if (lado2 == lado3):
                print ('ES UN TRIANGULO ISOSCELES')      
            elif (lado1 == lado3):
                print ('ES UN TRIANGULO ISOSCELES')
            elif (lado2 != lado3):
                print ('ES UN TRIANGULO ESCALENO')
    
    
        elif(lado1 < lado2):
        
            if (lado2 == lado3):
                print ('ES UN TRIANGULO ISOSCELES')  
            elif (lado1 == lado3):
                print ('ES UN TRIANGULO ISOSCELES')   
            elif (lado2 != lado3):
                print ('ES UN TRIANGULO ESCALENO')
           
        elif (lado1 == lado2):
            
            if (lado2 != lado3):
                print ('ES UN TRIANGULO ISOSCELES')
            elif(lado2 == lado3):
                print ('ES UN TRIANGULO EQUILATERO')
            

if __name__ == '__main__':
    main()