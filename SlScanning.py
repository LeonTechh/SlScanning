import time
from google import search

p = input('Escreva sua pesquisa: ')
t = input('Estime um tempo: ')

for resultado in search(p, stop=35):
    print(resultado)
    time.sleep(30)

