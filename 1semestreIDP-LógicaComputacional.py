# Adicionei mais Refinamento, Verificações, Loop e Tratamento de erro
import time

def mostrarAcao(mensagem):
    print(f"[AÇÃO]: {mensagem}")
    time.sleep(1)

# Estado inicial
agua = 0
cafeAdicionado = 0
naTomada = False
ligado = False
noFiltro = False
lugar = "Quarto"

# Ir para cozinha
mostrarAcao("Ir para a cozinha...")
lugar = "Cozinha"

# Localizar e pegar filtro
mostrarAcao("Localizando filtro de café...")
mostrarAcao("Pegando um filtro de papel...")
mostrarAcao("Abrindo o filtro...")
mostrarAcao("Colocando o filtro na cafeteira...")
noFiltro = True

# Verificar filtro refinamento + decisão
#Enquanto o filtro não estiver posicionado, este codigo vai rodar infinitamente
while noFiltro == False:
    mostrarAcao("Filtro mal posicionado! Ajustando...")
    noFiltro = True

mostrarAcao("Filtro OK!")

# Localizar café
mostrarAcao("Localizando o pó de café...")
mostrarAcao("Abrindo o recipiente de café...")

# Adicionar café
mostrarAcao("Colocando a 1ª colher de café")
cafeAdicionado += 1

mostrarAcao("Colocando a 2ª colher de café")
cafeAdicionado += 1

mostrarAcao("Fechando o recipiente de café...")
# Verificar café suficiente
#Caso o cafe adicionado seja menor que 2, ele irá dizer que tem café insuficiente
if cafeAdicionado < 2:
    print("Erro: café insuficiente!")
    quit()

# Adicionar água
mostrarAcao("Localizando garrafa d'água...")
mostrarAcao("Abrindo tampa da garrafa  d'água...")
mostrarAcao("Adicionando água...")
agua = 500

# Verificar água
#Caso a agua adicionada seja menor que 2, ele irá dizer que tem água insuficiente
if agua <= 0:
    print("Erro: sem água!")
    quit()

# Conectar na tomada
#Caso a cafeteira nao esteja na tomada, ele vai conectar ela.
if not naTomada:
    mostrarAcao("Conectando na tomada...")
    naTomada = True

# Ligar cafeteira
#Se o filtro estiver no lugar e tiver água, ele vai ligar a cafeteira
if noFiltro and agua > 0:
    mostrarAcao("Ligando a cafeteira...")
    ligado = True
    mostrarAcao("Café sendo preparado...")
else: #Caso contrario ele vai cancelar o programa
    print("Erro: não é possível ligar a cafeteira.")
    quit()
mostrarAcao("AGUARDE...")
mostrarAcao("Retirando a jarra de café...")
mostrarAcao("Servindo o café em uma xícara...")
print("="*6,"CAFÉ PRONTO","="*6)
