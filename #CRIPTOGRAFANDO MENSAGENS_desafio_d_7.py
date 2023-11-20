#CRIPTOGRAFANDO MENSAGENS
#LISTA DE ATIVIDADE 
#Desafio_1


#lista de letras para criptografar 
alfabeto = "defghijklmnopqrstuvwxyzabc"

#a chave secreta é 3 
chave = 7

letra=input("Por favor, entre com uma letra para criptografar: ")

#encontre a posição da letra em alfabeto

#exemplo: 'a' está na posição 0, 'e' está na posição 4, etc. 
posicao = alfabeto.find(letra)

#some a chave secreta para encontrar a posição da letra criptografada

#% 26 significa 'volte para e quando você chegar no 26 
novaPosicao=(posicao + chave) % 26

#a letra criptografada está no alfabeto na nova posição 
letraCriptografada = alfabeto[novaPosicao]
print("Sua letra criptografada é", letraCriptografada)