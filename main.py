import random

def desenhar_boneco(tentativas):
  partes = [
      """
        ______
       |      |
              |
              |
              |
              |
              |
      ============
      """,
      """
        ______
       |      |
     (   )    |
              |
              |
              |
              |
      ============
      """,
      """
        ______
       |      |
     (   )    |
       |      |
              |
              |
              |
      ============
      """,
      """
        ______
       |      |
     (   )    |
       |      |
       |      |
              |
              |
      ============
      """,
      """
        ______
       |      |
     (   )    |
      /|      |
       |      |
              |
              |
      ============
      """,
      """
        ______
       |      |
     (   )    |
      /|\\     |
       |      |
              |
              |
      ============
      """,
      """
        ______
       |      |
     (   )    |
      /|\\     |
       |      |
      /       |
              |
      ============
      """,
      """
        ______
       |      |
     (   )    |
      /|\\     |
       |      |
      / \\     |
              |
      ============
      """,
      """
        ______   
       |      |
     (X  )    |
      /|\\     |
       |      |
      / \\     |
              |
      ============
      """,
      """
        ______   
       |      |
     (X X)    |
      /|\\     |
       |      |
      / \\     |
              |
      ============
      """,
      """
        ______   
       |      |
     (X_X)    |
      /|\\     |
       |      |
      / \\     |
              |
      ============
      """
  ]
  print(partes[tentativas])
segredinhos = ['maçã', 'pera', 'laranja', 'banana', 
          'morango', 'abacaxi', 'melancia', 'limão', 'bergamota', 'pessêgo', 'mamão',
          'goiaba', 'abacate', 'acerola','cachorro', 'gato', 'papagaio', 'cavalo',
          'galinha', 'camelo', 'elefante', 'girafa', 'hipopótamo', 
          'pinguin', 'urso', 'macaco', 'arara', 'tartaruga'
          'cadeira', 'mesa', 'televisão', 'geladeira', 
          'fogão', 'armário', 'escrivaninha', 'cadeira de rodas', 'chuveiro'
           ]
continuar = ''
segredinho = random.choice(segredinhos)
letras_corretas = set()
letras_erradas = set()
tentativas = 0
while continuar != 'n':  
  while tentativas < 10:
    palavra_exibida = ' '.join([letra if letra in letras_corretas else '_' for letra in segredinho])
    print(f"\nPalavra: {palavra_exibida}")
    print(f"Tentativas: {tentativas}")
    print(f"Letras erradas: {', '.join(letras_erradas)}")
    tentativa = input("Manda uma letra aí: ").lower()
    if tentativa in letras_corretas or tentativa in letras_erradas:
        print("Você já tentou essa letra, mermão.")
        continue
    if tentativa in segredinho:
        letras_corretas.add(tentativa)
        if all(letra in letras_corretas for letra in segredinho):
          print(f"Mandou bem! Você adivinhou a palavra: {segredinho}")
          continuar = input("quer jogar denovo?s/n")
          if continuar == 's':
            continuar = 's'
            segredinho = random.choice(segredinhos)
            letras_corretas = set()
            letras_erradas = set()
            tentativas = 0
          else:
            break
    else:
      letras_erradas.add(tentativa)
      tentativas += 1
      desenhar_boneco(tentativas)
    if tentativas == 10:
      print(f"Que pena! Você perdeu! A palavra era: {segredinho}")
      continuar = input("quer jogar novamente? s/n ")
      if continuar == 's':
        continuar = 's'
        segredinho = random.choice(segredinhos)
        letras_corretas = set()
        letras_erradas = set()
        tentativas = 0
      else:
        break
