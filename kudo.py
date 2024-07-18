"""
------------------------------------------
KUDO: Decoder Toolkit                    |
                                         |
Author: Veilwr4ith                       |
------------------------------------------
"""

kudo = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⣿⣷⠀⠀
⢀⠀⠤⠤⣤⣄⣀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⡧⠚⠀
⠀⠀⢀⣠⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀							   
⣠⣾⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀					         
⣿⠟⠋⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀						    
⠁⠀⢠⣿⠏⡇⣿⣿⣿⣿⡇⢿⣿⣿⣷⣽⣿⣿⢿⣟⣙⣳⣽⣿⢿⣿⣿⣿⠁⠀			    		      
⠀⠀⠸⡟⠀⡙⢼⣿⣿⣿⡷⣬⣾⢿⣿⣿⣿⣩⣽⠿⠋⠙⣫⣿⣿⣿⢿⡏⠀⠀				No matter how clever the code, there's always a way to break it.
⠀⠀⠀⠹⡀⠀⠀⢿⣯⡸⠀⢀⣸⡎⡷⠟⢿⠓⠂⠀⢐⡾⢿⢩⢛⡵⢿⡐⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠡⣳⡄⠈⠚⠀⠀⠀⠀⠑⠄⣀⣀⠠⡜⣋⡼⢲⠭⠁⠀⠀			
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠖⡂⠉⠉⠁⢀⡀⠔⠀⠀⢰⡩⢿⣈⠁⠀⠀⠀⠀					
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠠⢀⠀⠀⠀⣀⡤⠟⣰⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣬⣿⣿⣿⣾⣿⣿⣿⣷⣶⣤⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⣿⠿⠙⢻⢿⣿⣿⣿⣿⣿⣿⣿⣷⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡿⠐⡸⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 
"""

import base64
import base58
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import html
import idna
import quopri
import datetime
import urllib.parse

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Help Menu
help_menu = """
Available Algorithms:
1. Advanced Encryption Standard (AES)
2. ROT13
3. Rivest-Shamir-Adleman (RSA)
4. ASCII85
5. Base32
6. Base64
7. Caesar Cipher
8. Hexadecimal
9. HTML Entity
10. Morse Code
11. PunnyCode
12. Quoted Printable
13. Unicode
14. UNIX Datetime
15. URL
16. Vigenere Cipher
17. XOR
18. Brainfuck
19. Reversed Word
20. Affine Cipher
21. Base58
"""

"""Function for decrypting AES Encryption"""
def decrypt_aes(key, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv=ciphertext[:AES.block_size])
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    pad_length = plaintext[-1]
    plaintext = plaintext[:-pad_length]
    return plaintext.decode('utf-8')

"""Function for decoding ROT13 Algorithm"""
def rot13_decoder(text):
    decoded_text = ""
    for char in text:
        if 'A' <= char <= 'Z':
            decoded_text += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            decoded_text += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            decoded_text += char
    return decoded_text

"""Function for decrypting RSA Encryption"""
def decrypt_rsa(private_key, ciphertext_b64):
    private_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    ciphertext = base64.b64decode(ciphertext_b64)
    plaintext = cipher_rsa.decrypt(ciphertext)
    return plaintext.decode('utf-8')

"""Function for decoding ASCII58 Algorithm"""
def decode_ascii85(encoded_data):
    try:
        decoded_data = base64.a85decode(encoded_data.encode('ascii'))
        return decoded_data.decode('utf-8')
    except base64.binascii.Error:
        return "Error: Invalid ASCII85 encoded data"

"""Function for decoding Base32 Algorithm"""
def base32_decode(encoded_text):
    try:
        decoded_bytes = base64.b32decode(encoded_text)
        decoded_text = decoded_bytes.decode('utf-8')
        print(f"Decoded String: {decoded_text}")
    except:
        print("Decoding Failed.")

"""Function for decoding Base64 Algorithm"""
def base64_decode(encoded_text):
    try:
        decoded_bytes = base64.b64decode(encoded_text)
        decoded_text = decoded_bytes.decode('utf-8')
        print(f"Decoded String: {decoded_text}")
    except:
        print("Decoding Failed.")

"""Function for decoding Caesar Cipher"""
def caesar_decoder(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

"""Function for decoding Hexadecimal"""
def hex_to_plaintext(hex_string):
    try:
        hex_string = hex_string.replace(" ", "")
        byte_data = bytes.fromhex(hex_string)
        plaintext = byte_data.decode('utf-8')
        return plaintext
    except Exception as i:
        print("Error:", i)
        return None
    
"""Function for decoding HTML Entity"""
def html_entity_decoder(text):
    decoded_text = html.unescape(text)
    return decoded_text

"""Function for decoding Morse Code"""
def morse_decoder(text):
    words = text.split('/')
    decoded_message = []
    for word in words:
        letters = word.split()
        decoded_word = ''
        for letter in letters:
            decoded_word += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(letter)]
        decoded_message.append(decoded_word)
    return ' '.join(decoded_message)

"""Function for decoding Punnycode"""
def punnycode_decoder(text):
    try:
        decoded_text = idna.decode(text)
        return decoded_text
    except idna.IDNAError as e:
        print(f"Error: {e}")
        return None
    
"""Function for decoding Quoted Printable"""
def quoted_printable_decoder(text):
    try:
        decoded_text = quopri.decodestring(text).decode('utf-8')
        return decoded_text
    except Exception as fuck:
        print("Error: ", fuck)

"""Function for decoding Unicode"""
def unicode_decoder(text):
    try:
        decoded_text = text.encode('utf-8').decode('unicode-escape')
        return decoded_text
    except UnicodeDecodeError:
        return "Error: Unable to decode Unicode text"
    
"""Function for decoding UnixTime"""
def unix_time_decoder(timestamp):
    try:
        timestamp = int(timestamp)
        date_time = datetime.datetime.utcfromtimestamp(timestamp)
        return date_time.strftime('%Y-%m-%d %H:%M:%S UTC')
    except ValueError:
        return "Invalid Unix timestamp"
    
"""Function for decoding URL"""
def url_decoder():
    encoded_urls = input("Enter the encoded URL(s) separated by comma: ")
    urls = encoded_urls.split(',')
    
    decoded_urls = []
    for encoded_url in urls:
        try:
            decoded_url = urllib.parse.unquote(encoded_url)
            decoded_urls.append(decoded_url)
        except Exception as e:
            print(f"Error decoded URL '{encoded_url.strip()}': {e}")

"""Function for decoding Vigenere Cipher"""
def vigenere_decode(ciphertext, keyword):
    keyword = keyword.upper()
    plaintext = ""
    keyword_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted_char
            keyword_index += 1
        else:
            plaintext += char
    return plaintext

"""Function for decoding XOR"""
def xor_decode(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        plaintext += chr(ord(char) ^ key)
    return plaintext

"""Function for decoding Base58"""
def base58_decode(encoded_str):
    decoded_bytes = base58.b58decode(encoded_str)
    decoded_str = str(decoded_bytes, 'utf-8') if isinstance(decoded_bytes, bytes) else decoded_bytes
    return decoded_str

"""Function for decoding BrainFuck Code"""
def brainfuck_decode(code):
    code = list(filter(lambda x: x in ['+', '-', '<', '>', '[', ']', '.', ','], code))
    memory = [0] * 30000
    pointer = 0
    output = ""
    loop_stack = []
    loop_map = {}
    for idx, char in enumerate(code):
        if char =='[':
            loop_stack.append(idx)
        elif char == ']':
            if loop_stack:
                start = loop_stack.pop()
                loop_map[start] = idx
                loop_map[idx] = start
            else:
                raise ValueError("Mismatched brackets in Brainfuck code.")
    idx = 0
    while idx < len(code):
        command = code[idx]
        if command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif command == '>':
            pointer = (pointer + 1) % 30000
        elif command == '<':
            pointer = (pointer - 1) % 30000
        elif command == '[':
            if memory[pointer] == 0:
                idx = loop_map[idx]
        elif command == ']':
            if memory[pointer] != 0:
                idx = loop_map[idx]
        elif command == '.':
            output += chr(memory[pointer])
        elif command == ',':
            pass
        idx += 1
    return output

"""Function for decoding a reversed word"""
def decode_reverse(text):
    original_word = text[::-1]
    return original_word

"""2 Functions for affine cipher 'mod_inverse' and 'affine_decrypt'"""
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
        return None

def affine_decrypt(ciphertext, a, b):
    m = 26
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        raise ValueError("The key 'a' has no modular inverse, decryption is not possible.")
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            x = (a_inv * (y - b)) % m
            decrypted_char = chr(x + ord('A')) if char.isupper() else chr(x + ord('a'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

"""Main Menu Function"""
def menu():
    print(kudo)
    while True:
        try:
            prompt = input("~> ")
            if not prompt:
                continue
            elif prompt == '1':
                key = input("Enter the AES key (16, 24, or 32 bytes): ")
                key_encode = key.encode('utf-8')
                print("Length of key before encoding:", len(key))
                print("Length of key after encoding:", len(key_encode))
                ciphertext_b64 = input("Enter the encoded ciphertext: ")
                ciphertext = base64.b64decode(ciphertext_b64)
                try:
                    print("-" * 30)
                    plaintext = decrypt_aes(key_encode, ciphertext)
                    print("Decrypted plaintext:", plaintext)
                except Exception as e:
                    print("Error:", e)
            elif prompt == '2':
                encoded_text = input("Enter the ROT13 String: ")
                print('-' * 30)
                decoded_text = rot13_decoder(encoded_text)
                print(f"Decoded Text: {decoded_text}")
            elif prompt == '3':
                private_key_str = input("Enter the RSA private key: ")
                ciphertext_b64 = input("Enter the encoded ciphertext: ")
                try:
                    plaintext = decrypt_rsa(private_key_str, ciphertext_b64)
                    print("-" * 30)
                    print("Decrypted plaintext:", plaintext)
                except Exception as e:
                    print("Error:", e)
            elif prompt == '4':
                encoded_data = input("Enter the encoded data: ")
                decoded_data = decode_ascii85(encoded_data)
                print("-" * 30)
                print(f"Decoded String: {decoded_data}")
            elif prompt == '5':
                encoded_string = input("Enter the encoded data: ")
                print("-" * 30)
                base32_decode(encoded_string)
            elif prompt == '6':
                encoded_string = input("Enter the encoded data: ")
                print("-" * 30)
                base64_decode(encoded_string)
            elif prompt == '7':
                text = input("Enter the encoded string: ")
                shift = int(input("Enter the shift value: "))
                decrypted_text = caesar_decoder(text, shift)
                print("-" * 30)
                print(f"Decrypted text: {decrypted_text}")
            elif prompt == '8':
                hex_input = input("Enter the hexadecimal string: ")
                plaintext = hex_to_plaintext(hex_input)
                print("-" * 30)
                print("Plaintext:", plaintext)
            elif prompt == '9':
                html_entity = input("Enter the HTML Entity: ")
                decoded_entity = html_entity_decoder(html_entity)
                print("-" * 30)
                print("Decoded Entity: ", decoded_entity)
            elif prompt == '10':
                morse_code = input("Enter the Morse Code: ")
                decoded_message = morse_decoder(morse_code)
                print("-" * 30)
                print("Decoded Message:", decoded_message)
            elif prompt == '11':
                punnycode_text = input("Enter the Punnycode Text: ")
                decoded_text = punnycode_decoder(punnycode_text)
                print("-" * 30)
                print(f"Decoded Punnycode Text: {decoded_text}")
            elif prompt == '12':
                quoted_printable_text = input("Enter the QPT: ")
                decoded_text = quoted_printable_decoder(quoted_printable_text)
                print("-" * 30)
                print(f"Decoded Text: {decoded_text}")
            elif prompt == '13':
                unicode_text = input("Enter the Unicode Text: ")
                decoded_text = unicode_decoder(unicode_text)
                print("-" * 30)
                print("Decoded text:", decoded_text)
            elif prompt == '14':
                timestamp = input("Enter Unix timestamp: ")
                decoded_time = unix_time_decoder(timestamp)
                print("-" * 30)
                print("Decoded time:", decoded_time)
            elif prompt == '15':
                url_decoder()
            elif prompt == '16':
                ciphertext = input("Enter the ciphertext: ")
                keyword = input("Enter the keyword: ")
                decoded_text = vigenere_decode(ciphertext, keyword)
                print("-" * 30)
                print(f"Decoded String: {decoded_text}")
            elif prompt == '17':
                ciphertext = input("Enter the ciphertext: ")
                key = int(input("Enter the key (an integer): "))
                decoded_text = xor_decode(ciphertext, key)
                print("-" * 30)
                print(f"Decoded String: {decoded_text}")
            elif prompt == '18':
                brainfuck_code = input("Enter the brainfuck code: ")
                decoded_text = brainfuck_decode(brainfuck_code)
                print("-" * 30)
                print(f"Decoded text: {decoded_text}")
            elif prompt == '19':
                reversed_word = input("Enter the reversed word: ")
                original_word = decode_reverse(reversed_word)
                print("-" * 30)
                print(f"Decoded String: {original_word}")
            elif prompt == '20':
                ciphertext = input("Enter the ciphertext: ")
                a = int(input("Enter the key 'a' (must be coprime with 26): "))
                b = int(input("Enter the key 'b': "))
                try:
                    plaintext = affine_decrypt(ciphertext, a, b)
                    print(f"Decoded String: {plaintext}")
                except ValueError as e:
                    print(e)
            elif prompt == '21':
                ciphertext = input("Enter the ciphertext: ")
                decoded_text = base58_decode(ciphertext)
                print("-" * 30)
                print(f"Decoded String: {decoded_text}")
            elif prompt == 'h':
                print(help_menu)
            else:
                print("Invalid Option!")
        except KeyboardInterrupt:
            break
if __name__ == "__main__":
    menu()