# Código de cores
limpar = '\033[m'
amarelo_claro = '\033[93m'
roxo = '\033[35m'
ciano_claro = '\033[96m'
vermelho_claro = '\033[91m'

# Bibliotecas
from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACESS_TOKEN_SECRET
import tweepy
from datetime import datetime

# Título
def titulo(txt):
    """
    Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado
    """
    print(f'{ciano_claro}={limpar}' * (len(txt) + 4))
    print(f'{ciano_claro}= {roxo}{txt} {ciano_claro}={limpar}')
    print(f'{ciano_claro}={limpar}' * (len(txt) + 4))
    print()

# Chama função Título
titulo('Twitter 10 Top Trends'.upper().center(99))

# Registro data, hora, minuto e segundo
date_today = datetime.now().strftime("%Y-%m-%d %Hh%Mm%Ss")

# Código de localização geográfico
BRAZIL_WOE_ID = 23424768

# Uso das chaves Twitter: "secrets"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACESS_TOKEN_SECRET)

# Solicitação API Twitter
api = tweepy.API(auth)

# Armazenamento Top Trends na variável
try:
    trends = api.trends_place(BRAZIL_WOE_ID)
except:
    print(f'Erro:{vermelho_claro}tweepy.error.TweepError{limpar}')
    print()

# Nova Lista
Twitter_Top_Trends = []

# Contador
cont = 0

# Print dos Top Trends e armazenamento dos 10 Top Trends na Nova Lista
try:
    print(f'{amarelo_claro}Twitter Top Trends:{limpar}\n{trends}')
    for c in trends[0]['trends']:
        cont += 1
        if cont <= 10:
            Twitter_Top_Trends.append(c)
except NameError as erro:
    print(f'''{vermelho_claro}{erro}{limpar}
Favor verificar as {roxo}CHAVES{limpar} informadas em "{amarelo_claro}secrets{limpar}":
{roxo}CHAVES: {amarelo_claro}CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACESS_TOKEN_SECRET{limpar}''')
else:
    # Eliminação de item dentro dos dicionario contidos na Nova Lista
    for c in Twitter_Top_Trends:
        del c['promoted_content']

    # Print dos 10 Top Trends na Nova Lista numerados
    print()
    print(f'{ciano_claro}={limpar}'*104)
    print(f'{amarelo_claro}Data de extração Twitter os 10 Top Trends: {vermelho_claro}{date_today}{limpar}')
    for c, i in enumerate(Twitter_Top_Trends, start=1):
        print(f'{amarelo_claro}{c}º{vermelho_claro}=>{limpar} {i}')
    print(f'{ciano_claro}={limpar}'*104)
    print()

    # Salva em arquivo texto a Nova Lista com registro único
    arq = open(f'Twitter os 10 Top Trends {date_today}.txt', 'a+')
    for c in Twitter_Top_Trends:
        arq.write(f'{c}')
        arq.write('\n')
    arq.seek(0)
    arq.close()
