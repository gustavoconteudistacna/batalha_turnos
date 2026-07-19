import random
vida_player = 100
vida_npc = 100
defesa_player = 100
defesa_npc = 100
dano = 25
rounds = 1

while vida_player > 0 and vida_npc > 0:
    print(f'{"-" * 10} ROUND {rounds} {"-" * 10}')
    print(f"Player -> Vida: {vida_player} | Defesa: {defesa_player}")
    print(f"NPC    -> Vida: {vida_npc} | Defesa: {defesa_npc}")
    print()
    player_acao = int(input("1 - Atacar | 2 - Defender | Escolha: "))
    while player_acao != 1 and player_acao != 2:
        player_acao = int(input("Digite apenas 1 ou 2: "))
    npc_acao = random.choice(["atacar", "defender"])
    print()
    if player_acao == 1:
        print("Player escolheu ATACAR")
    else:
        print("Player escolheu DEFENDER")

    if npc_acao == "atacar":
        print("NPC escolheu ATACAR")
    else:
        print("NPC escolheu DEFENDER")

    print()

    if player_acao == 1 and npc_acao == "atacar":
        print("Ambos atacaram!")

        vida_player = vida_player - dano
        vida_npc = vida_npc - dano

    elif player_acao == 2 and npc_acao == "defender":

        print("Os dois defenderam. Nada aconteceu.")

    elif player_acao == 1 and npc_acao == "defender":

        if defesa_npc > 0:

            defesa_npc = defesa_npc - dano

            if defesa_npc < 0:
                defesa_npc = 0

            print("O NPC bloqueou o ataque!")
            print(f"A defesa do NPC caiu para {defesa_npc}")

        else:
            vida_npc -= dano
            print("O escudo do NPC foi quebrado!")
            print("O ataque atingiu diretamente a vida.")

    elif player_acao == 2 and npc_acao == "atacar":
        if defesa_player > 0:
            defesa_player = defesa_player - dano
            if defesa_player < 0:
                defesa_player = 0
            print("O Player bloqueou o ataque!")
            print(f"A defesa do Player caiu para {defesa_player}")

        else:

            vida_player = vida_player - dano

            print("O escudo do Player foi quebrado!")
            print("O ataque atingiu diretamente a vida.")

    rounds = rounds + 1

print("=" * 35)

if vida_player <= 0 and vida_npc <= 0:
    print("Empate!")
elif vida_player <= 0:
    print("NPC venceu!")
else:
    print("Player venceu!")