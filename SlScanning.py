import time #Biblioteca do tempo
from google import search #Biblioteca do Google

p = input('Escreva sua pesquisa: ')
t = input('Estime um tempo: ')

for resultado in search(p, stop=35): 
    print(resultado)
    time.sleep(30)

