def DefinaHoraAno():
    Flag = False
    while not Flag:
        try:
        
            minutosT = int(input("Digite a quantidade de horas\n"))
            
            ano = int(minutosT/(24*30.396473*12))
            minutosRest = minutosT%(24*30.396473*12)
            
            meses = int(minutosRest/720)
            minutosRest1 = minutosRest%720
            
            dias = int(minutosRest1/24)
            minutosRest2 = minutosRest1%24
            
            horas = int(minutosRest2%60)
            
            
            print ("Valor em {} anos {} meses {} dias e {} horas ".format(ano,meses,dias,horas))
            Flag = True
           
            
            
            print("____________________________________________________")
            print ("\n\n\n\n\n")
            return exit()
        
        
        except(ValueError):
            print("\n\n\nDigite apenas números\n\n\n\n\n\n")
            return exit()
DefinaHoraAno()      
