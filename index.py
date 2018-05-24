nome = str(input("Ola, qual e o seu nome? "))
print("Que nome bonito! ", nome)

while True:
	quest = input("Faca uma pergunta  ")

	if quest == "Qual o seu nome?":
		print("Meu nome e Ana! haha, e eu sei o seu tambem, ", nome)
	else:
		print("Nao tenho essa pergunta no meu banco de dados! Leia  o arquivo : perguntas.txt que previamente deveria vir no seu download!")