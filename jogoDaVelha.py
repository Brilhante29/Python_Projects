import random
class Game:
  usuario = int
  computador = int
  def game():
    usuario = int(input(
    """
    Escolha uma dentre as opções
    [1]Pedra
    [2]Papel
    [3]Tesoura
    """))
    computador = random.randint(1,3)

    if computador == 1:
      print("O computador escolheu: Pedra")
      if usuario == 1:
        print("Empate!")
      elif usuario == 2:
        print("Você venceu")
      elif usuario == 3:
        print("Você perdeu")
      else:
        print("Operação inválida")
    elif computador == 2:
      print('O computador escolheu: Papel')
      if usuario == 1:
        print("Você perdeu")
      elif usuario == 2:
         print("Empate!")
      elif usuario == 3:
         print("Você venceu")
      else:
         print("Operacao invalida")
    elif computador == 3:
      print('O computador escolheu: Tesoura')
      if usuario == 1:
        print("Você venceu")
      elif usuario == 2:
        print("Computador venceu")
      elif usuario == 3:
        print("Empate!")
      else:
        print("Operacao invalida")
    else:
      print("Operacao invalida")
  game()
 
