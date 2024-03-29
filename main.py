from pygal import Bar
from frequency import *


alphabet = list("abcdefghijklmnñopqrstuvwxyz")
code = {}

def reversed_alphabet():
    backwards = list(reversed(alphabet))

    for i in range(len(alphabet)):
        code[alphabet[i]] = backwards[i]



def frequency(text):
    text = list(text.lower())

    freq = {}
    for letter in alphabet:
        freq[letter] = 0

    total_letters = len(text)

    for letter in text:
        if letter in freq:
            freq[letter]+=1

    for letter in freq:
        freq[letter] = freq[letter]/total_letters *100

    return freq


def make_chart(text,language):
    chart = Bar()
    chart.title = 'Frequency analysis'
    chart.x_labels = text.keys()
    chart.add('Target message', text.values())
    chart.add('Language', language.values())

    chart.render_to_file("bar_chart.svg")


def atbash(text):
    text = text.lower()
    output = ""

    for letter in text:
        if letter in code:
            output += code[letter]

    return output


def get_text(filename):
    with open(filename) as f:
        text = f.read().replace('\n', '')

    return text


#Crea el menu
def menu():
    choice = ""

    while choice != "c" and choice != "f" and choice != "m":
        choice = input("Please enter c to encode/decode text, f to perform frequency analysis, or m to encrypt your own short message: ")

    if choice == "c":
        print("Running your message through the cypher... ")
        message = get_text("input.txt")
        code = atbash(message)
        print(code)

    elif choice == 'f':
        print('Analysing message…')
        message = get_text("input.txt")
        message_freq = frequency(message)

        language = input('Which language is your message in? \n1. English \n2. French \n3. Spanish\n Type: ')

        if language == '1':
            lang_freq = english  # Importa el diccionario en ingles
        elif language == '2':
            lang_freq = french
        elif language == '3':
            lang_freq = spanish

        make_chart(message_freq, lang_freq)

    elif choice == "m":
        message = input("What would you like to encode: ")
        code = atbash(message)
        print(code)


def main():
    reversed_alphabet()
    menu()

main()