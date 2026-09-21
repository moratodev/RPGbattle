import armas
import personagens
from time import sleep
from random import randint

nome_jogador = str(input("Qual é o seu nome? ")).strip().title()
sleep(1)
print(f"Muito prazer {nome_jogador}, escolha uma classe para iniciar sua batalha!")
sleep(1)
print("""
1 - Kina  | Guerreiro
2 - Pally | Arqueiro
3 - Mage  | Mago \n""")

# Jogador escolhendo a classe.
while True:
    try:
        escolha_classe_jogador = int(input("Digite o número para a escolha da classe: "))
        if escolha_classe_jogador <= 0:
            print("Digite um valor maior que zero.")
            continue

        if escolha_classe_jogador > 3:
            print("Opção fora do parâmetro, números entre 1 e 3.")
            continue

    except ValueError:
        print("Digite uma opção válida.")
        continue

    else:
        if escolha_classe_jogador == 1:
            print(f"Perfeito, agora {nome_jogador} é da classe Kina")
            dragon_sword = armas.Espada("dragon sword", 28)
            jogador = personagens.Kina(nome_jogador, dragon_sword)
            print(jogador)
            break

        elif escolha_classe_jogador == 2:
            print(f"Perfeito, agora {nome_jogador} é da classe Pally")
            dragon_bow = armas.Arco("dragon bow", 30)
            jogador = personagens.Pally(nome_jogador, dragon_bow)
            print(jogador)
            break

        elif escolha_classe_jogador == 3:
            print(f"Perfeito, agora {nome_jogador} é da classe Mage")
            dragon_wand = armas.Cajado("dragon wand", 33)
            jogador = personagens.Mage(nome_jogador, dragon_wand)
            print(jogador)
            break

# Fazendo o adversário escolher a classe
print("Adversário escolhendo sua classe...")
sleep(2)

escolha_classe_adversario = randint(1, 3)
# Corrigido: Garante que o adversário não repita a classe do jogador sem entrar em loop infinito
while escolha_classe_adversario == escolha_classe_jogador:
    escolha_classe_adversario = randint(1, 3)

if escolha_classe_adversario == 1:
    print("O adversário agora é da classe Kina.")
    minotaur_sword = armas.Espada("minotaur sword", 28)
    adversario = personagens.Kina("Adversário", minotaur_sword)
    sleep(0.8)
    print(adversario)

elif escolha_classe_adversario == 2:
    print("O adversário agora é da classe Pally.")
    minotaur_bow = armas.Arco("minotaur bow", 30)
    adversario = personagens.Pally("Adversário", minotaur_bow)
    sleep(0.8)
    print(adversario)

elif escolha_classe_adversario == 3:
    print("O adversário agora é da classe Mage.")
    minotaur_wand = armas.Cajado("minotaur wand", 33)
    adversario = personagens.Mage("Adversário", minotaur_wand)
    sleep(0.8)
    print(adversario)

# Loop da Batalha
print("\n-=-=-=-=-= Prepare-se para a batalha! -=-=-=-=-=")
while True:
    print("""
    1 - Atacar
    2 - Ver status""")

    try:
        escolha_jogador = int(input("Digite sua opção: "))
    except ValueError:
        print("Opção inválida, digite um número.")
        continue

    if escolha_jogador == 1:
        jogador.atacar(adversario)
        # Verifica se o adversário foi derrotado após o ataque do jogador
        if not adversario.esta_vivo():
            print(f"\nBatalha encerrada! {jogador.obter_nome()} venceu!")
            break

    elif escolha_jogador == 2:
        print(jogador)
        print(adversario)
        continue # Não gasta o turno ao verificar o status

    else:
        print("Opção inválida!")
        continue

    # Vez do adversário
    print("\n----- Vez do Adversário -----")
    sleep(1)
    adversario.atacar(jogador)
    
    # Verifica se o jogador foi derrotado após o ataque do adversário
    if not jogador.esta_vivo():
        print(f"\nBatalha encerrada! {adversario.obter_nome()} venceu!")
        break