import string

def criptografia(frase):
    
    caracter = ""
    a = list(string.ascii_lowercase)
    b = list(string.ascii_uppercase)
    for letra in frase:
        if letra in a:
            caracter = caracter + "@*&"
        elif letra in b:
            caracter = caracter + "#$!?"
    return caracter
            
print(criptografia(input("Digite o texto que será Criptografado ")))
