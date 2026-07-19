
import random

palavra_secreta = random.choice(["javascript", 'python', 'java', 'ruby', 'typescript'])
letras_certas = []
letras_erradas = []
tentativas = 6

while tentativas > 0:
	palavra_formada = ""
	for letra in palavra_secreta:
		if letra in letras_certas:
			palavra_formada += letra
		else:
			palavra_formada += "_"

	print("Palavra:", palavra_formada)
	if len(letras_erradas) > 0:
		print("Letras erradas:", letras_erradas)
	else:
		print("Letras erradas:", "nenhuma")
	print("Tentativas restantes:", tentativas)

	if palavra_formada == palavra_secreta:
		print("Parabéns! Você ganhou!")
		break

	chute = input("Digite uma letra: ")
	chute = chute.lower()
	if len(chute) != 1:
		print("Digite apenas UMA letra válida.")
		continue

	if chute in letras_certas or chute in letras_erradas:
		print("Você já tentou essa letra. Tente outra.")
		continue

	if chute in palavra_secreta:
		letras_certas.append(chute)
	else:
		letras_erradas.append(chute)
		tentativas -= 1

print()

if tentativas == 0:
    print(f"Você perdeu! A palavra era '{palavra_secreta}'.")