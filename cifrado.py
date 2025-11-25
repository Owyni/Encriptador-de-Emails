def cifrar_texto(texto):
    diccionario_cifrado = {
        'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c',
        'f': 'x', 'g': 'z', 'h': 'l', 'i': 'k', 'j': 'j',
        'k': 'h', 'l': 'g', 'm': 'f', 'n': 'd', 'o': 's',
        'p': 'a', 'q': 'p', 'r': 'o', 's': 'i', 't': 'u',
        'u': 'y', 'v': 't', 'w': 'r', 'x': 'e', 'y': 'w',
        'z': 'q', 'A': 'M', 'B': 'N', 'C': 'B', 'D': 'V', 
        'E': 'C', 'F': 'X', 'G': 'Z', 'H': 'L', 'I': 'K',
        'J': 'J', 'K': 'H', 'L': 'G', 'M': 'F', 'N': 'D',
        'O': 'S', 'P': 'A', 'Q': 'P', 'R': 'O', 'S': 'I',
        'T': 'U', 'U': 'Y', 'V': 'T', 'W': 'R', 'X': 'E',
        'Y': 'W', 'Z': 'Q', ' ': ' ', '\n': '\n'
    }

    texto_cifrado = ""

    for letra in texto:
        texto_cifrado += diccionario_cifrado.get(letra, letra)

    return texto_cifrado

def descifrar_texto(texto):
    diccionario_descifrado = {
        'm': 'a', 'n': 'b', 'b': 'c', 'v': 'd', 'c': 'e',
        'x': 'f', 'z': 'g', 'l': 'h', 'k': 'i', 'j': 'j',
        'h': 'k', 'g': 'l', 'f': 'm', 'd': 'n', 's': 'o',
        'a': 'p', 'p': 'q', 'o': 'r', 'i': 's', 'u': 't',
        'y': 'u', 't': 'v', 'r': 'w', 'e': 'x', 'w': 'y',
        'q': 'z', 'M': 'A', 'N': 'B', 'B': 'C', 'V': 'D',
        'C': 'E', 'X': 'F', 'Z': 'G', 'L': 'H', 'K': 'I',
        'J': 'J', 'H': 'K', 'G': 'L', 'F': 'M', 'D': 'N',
        'S': 'O', 'A': 'P', 'P': 'Q', 'O': 'R', 'I': 'S',
        'U': 'T', 'Y': 'U', 'V': 'V', 'W': 'W', 'E': 'X',
        'W': 'Y', 'Q': 'Z', ' ': ' ', '\n': '\n'
    }

    texto_descifrado = ""

    for letra in texto:
        texto_descifrado += diccionario_descifrado.get(letra, letra)

    return texto_descifrado