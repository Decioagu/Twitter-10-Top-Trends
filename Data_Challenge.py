# Bibliotecas
from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACESS_TOKEN_SECRET
import tweepy
from datetime import datetime

# Código de cores
limpar = '\033[m'
amarelo_claro = '\033[93m'
roxo = '\033[35m'
ciano_claro = '\033[96m'
vermelho_claro = '\033[91m'

# Função Título
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

# Chama "Função Título"
titulo('Twitter 10 Top Trends'.upper().center(100))

# Registro data, hora, minuto e segundo
date_today = datetime.now().strftime("%Y-%m-%d %Hh%Mm%Ss")

# Código de localização geográfico
BRAZIL_WOE_ID = 23424768

# Uso das chaves Twitter oculto em (Bibliotecas => "secrets")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACESS_TOKEN_SECRET)

# Solicitação API Twitter
api = tweepy.API(auth)

# Teste: Armazenamento ("BRAZIL_WOE_ID" => Top Trends) na variável "trends"
try:
    trends = api.trends_place(BRAZIL_WOE_ID)
# Identificado o erro
except:
    print(f'{amarelo_claro}Erro: {vermelho_claro}tweepy.error.TweepError{limpar}')
    print()
    print(f'''Favor verificar as {roxo}CHAVES{limpar} informadas em {amarelo_claro}(Bibliotecas => "secrets"){limpar}:
{roxo}CHAVES: {amarelo_claro}CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACESS_TOKEN_SECRET{limpar}''')
    print()
else:
    # Nova Lista
    Twitter_Top_Trends = []

    # Contador
    cont = 0

    # Print Twitter Top Trends, extraído de ("BRAZIL_WOE_ID" => Código de localização geográfico)
    print(f'{amarelo_claro}Twitter Top Trends:{limpar}\n{trends}')

    # Armazenamento dos 10 Top Trends na "Nova Lista"
    for c in trends[0]['trends']:
        cont += 1
        if cont <= 10:
            Twitter_Top_Trends.append(c)

    # Eliminação da chave "promoted_content" nos dicionários contidos na "Nova Lista"
    # Informação considerada desprezivo
    for c in Twitter_Top_Trends:
        del c['promoted_content']

    # Informa data e hora da extração
    print()
    print(f'{ciano_claro}={limpar}'*104)
    print(f'{amarelo_claro}Data de extração Twitter os 10 Top Trends: {vermelho_claro}{date_today}{limpar}')


    # Print dos 10 Top Trends na "Nova Lista" numerados de 1 até 10
    for c, i in enumerate(Twitter_Top_Trends, start=1):
        print(f'{amarelo_claro}{c}º{vermelho_claro}=>{limpar} {i}')
    print(f'{ciano_claro}={limpar}'*104)
    print()

    # Salva em arquivo texto a "Nova Lista" com registro único utilizando "date_today"
    arq = open(f'Twitter os 10 Top Trends {date_today}.txt', 'a+')
    for c in Twitter_Top_Trends:
        arq.write(f'{c}')
        arq.write('\n')
    arq.seek(0)
    arq.close()
