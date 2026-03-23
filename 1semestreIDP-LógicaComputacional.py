import time

def mostrarAcao(mensagem): #o parametro é a mensagem
    print(f"[AÇÃO]: {mensagem}") #Exiba a palavra "AÇÃO" seguido da mensagem digitada quando a func for chamada
    time.sleep(1) #Pequena pausa antes de exibir executar o print/escreva

#Estado inicial do robô
agua = 0
cafeAdicionado = 0
naTomada = False
ligado = False
noFiltro = False
lugar = "Quarto"

mostrarAcao("Ir para a cozinha...")
lugar = "Cozinha" #Altera o local do robo

mostrarAcao("Pegando um filtro de papel...") 
mostrarAcao("Abrindo o filtro...")
mostrarAcao("Colocando o filtro na cafeteira...")
noFiltro = True #Atualiza o estado do filtro 
mostrarAcao("Pegando o pó de café...")


mostrarAcao("Colocando a 1ª colher de café")
cafeAdicionado += 1 #Atualiza o estado de colheres de café no recipiente


mostrarAcao("Colocando a 2ª colher de café")
cafeAdicionado += 1 ###

mostrarAcao("Adicionando água...")
agua = 500  #Atualiza o estado da água

if naTomada == False: #Caso a cafeteira nao esteja conectada na tomada
    mostrarAcao("Conectando na tomada...") #Exiba a mensagem de que esta sendo conectada
    naTomada = True #Atualize o estado da tomada para verdadeiro

if noFiltro == True and agua > 0: #Caso as duas afirmações sejam verdadeira (filtro colocado e água)
    mostrarAcao("Ligando a cafeteira...")
    ligado = True
    mostrarAcao("Café sendo preparado...")
else:
    print("Erro: não é possível ligar a cafeteira.") #Caso alguma das condições acima seja falsa
    quit() #Encerre o programa
print("="*6,"O CAFÉ ESTÁ PRONTO","="*6)
