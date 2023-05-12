palavra = "Python"
letras_usuario = []
chances = 7
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=' ')
        else:
            print('_', end= " ")
    print("")
    tentativa = input("escolha uma letra, ")
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False



    if chances == 0 or ganhou:
         break

if ganhou:
    print(f"Parabéns a pallavra era: {palavra}")
else:
    print(f"Lost a palavra era: {palavra}")