#Caesar Cipher
#@Ermelindo Martinho

import pyperclip

#a string para ser encriptografado/descriptografado
message = 'Aqui tens a mesnagem.'

#a chave encriptada/descriptada
key = 13
#chama o programa para ser encriptografado/descriptografado
mode = 'encrypt'# define para encriptada ou descriptada

#possiveis symbolos que podem ser encriptado
LETTERS =  ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

#armazena a encriptação/descriptação do formulario da msg
translated = ''

#catalizar o string na msg
#message = message.upper()

#roda o codigo de encriptação/descriptação  em cada simbolo na msg de string
for symbol in message:
	if symbol in LETTERS:
        #irá encriptar(ou descriptar) o numero deste simbolo
		num = LETTERS.find(symbol)#vai ao numero do simbolo
		if mode ==  'encrypt':
			num = num + key
		elif mode == 'decrypt':
			num = num - key
        
        #lida com o wrap-around se o numero for maior que o cumprimento LETTER ou less do que zero
		if num >= len(LETTERS):
			num = num - len(LETTERS)
		elif num < 0:
			num = num + len(LETTERS)
       #adiciona simbolo de numeros encriptografado/descriptografado no final da tradução
		translated = translated + LETTERS[num]


	else:
         # adiciona o simbolo sem encriptografar/descriptografar
		translated = translated + symbol

#imprime a strig encriptografada/descriptografada
print(translated)

#copie a string encriptografada/descriptografada para a area de transferencia
pyperclip.copy(translated)
