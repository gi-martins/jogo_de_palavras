import random

from palavras_secretas import nivel_facil, nivel_medio, nivel_dificil


letras_validas = []

while True:   

    menu = input("Escolha sua dificuldade: 1(fácil); 2(médio); 3(díficil): ")

    if menu == "1":
        vidas = 15
        palavra_secreta = nivel_facil[random.randint(0, len(nivel_facil)-1)]
    elif menu == "2":
        vidas = 10 
        palavra_secreta = nivel_medio[random.randint(0, len(nivel_medio)-1)]       
    elif menu == "3":
        vidas = 5
        palavra_secreta = nivel_dificil[random.randint(0, len(nivel_dificil)-1)]
    else:
        print("Digite 1, 2 ou 3")
        continue
    
    break
 
while True:

    palavra_exibida = ""

    letra_chute = input("Digite uma letra: ")

    if len(letra_chute) > 1 or letra_chute.isspace() or not letra_chute.isalpha(): 
        print("Digite apenas uma letra válida")
        continue

    if letra_chute in palavra_secreta:
        letras_validas.append(letra_chute)
    else:
        vidas -= 1

    for letra in palavra_secreta:    
    
        if letra in letras_validas:
            palavra_exibida += letra
        
        else:
            palavra_exibida += "*"         

    print(palavra_exibida)

    if vidas <= 0:
        print("Você perdeu!")
        break

    if palavra_exibida == palavra_secreta:
        print("Palavra secreta está certa")
        break
