# Código de cores
limpar = '\033[m'
amarelo = '\033[33m'
amarelo_claro = '\033[93m'
roxo = '\033[35m'
ciano_claro = '\033[96m'

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
titulo('Twitter 10 Top Trends'.upper())

# Registro data, hora, minuto e segundo
date_today = datetime.now().strftime("%d-%m-%Y %Hh%Mm%Ss")

# Código de localização geográfico
BRAZIL_WOE_ID = 23424768

# Uso das chaves Twitter: "secrets"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACESS_TOKEN_SECRET)

# Solicitação API Twitter
api = tweepy.API(auth)

# Armazenamento Top Trends na variável
trends = api.trends_place(BRAZIL_WOE_ID)

# Nova Lista
Twitter_Top_Trends = []

# Contador
cont = 0

# Print dos Top Trends e armazenamento dos 10 Top Trends na Nova Lista
for c in trends[0]['trends']:
    print(f'{c}')
    cont += 1
    if cont <= 10:
        Twitter_Top_Trends.append(c)

# Eliminação de item dentro dos dicionario contidos na Nova Lista
for c in Twitter_Top_Trends:
    del c['promoted_content']

# Print dos 10 Top Trends na Nova Lista numerados
print()
print('='*100)
print(f'{amarelo}DATA DA EXTRAÇÃO: {amarelo_claro}{date_today}{limpar}')
for c, i in enumerate(Twitter_Top_Trends, start=1):
    print(f'{c}º=> {i}')
print('='*100)
print()

# Salva em arquivo texto a Nova Lista com registro único
arq = open(f'Twitter os 10 Top Trends {date_today}.txt', 'a+')
for c in Twitter_Top_Trends:
    arq.write(f'{c}')
    arq.write('\n')
arq.seek(0)
print(arq.read())
arq.close()
print('='*100)
