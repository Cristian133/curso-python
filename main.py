#!/usr/bin/env python3

import random

def presentation():

    print("***************************************************")
    print("*                                                 *")
    print("*         Comienza el Juego del ahorcado!         *")
    print("*                                                 *")
    print("***************************************************")

def random_word():
    len = input("\nIngresar el número de letras de la palabra\n que tratarás de deducir (6 - 9): ")
    path = "./diccionarios/0"+ len +".txt"

    with open(path, 'r') as file:
        word = file.readlines()

    return random.choice(word).strip()


def show(word, right_word):
    return ''.join([letter if letter in right_word else '_' for letter in word])

def start():
    presentation()
    word = random_word()
    right_word = set()
    remaining = 6
    wrong_word = set()

    while remaining > 0:

        print("\npalabra:", show(word, right_word))
        print(f"Letras incorrectas: {', '.join(wrong_word)}")
        print(f"Intentos restantes: {remaining}")

        letter = input("Adivina una letra: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Introducir una sola letra.")
            continue

        if letter in right_word or letter in wrong_word:
            print("Ya adivinate esa letra. Intentá con otra.")
            continue

        if letter in word:
            right_word.add(letter)
            print(f"La letra '{letter}' está en la palabra.")
        else:
            wrong_word.add(letter)
            remaining -= 1
            print(f"La letra '{letter}' no está en la palabra.")

        if set(word) == right_word:
            print(f"\n¡Felicitaciones!!! Adivinaste la palabra: {word}")
            break
    else:
        print(f"\nTe quedaste sin intentos. La palabra era: {word}")

if __name__ == '__main__':
    start()
