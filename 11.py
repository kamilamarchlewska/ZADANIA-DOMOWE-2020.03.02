#Utwórz listę, która zawiera składniki na ulubione danie.
#Wyświetl komunikaty co należy pokolei dodać.
#Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

list = ['jajka', 'mąkę', 'mleko', 'roztopione masło', '1/2 śmietany 30%', 'cukier puder']

print('Wrzuć do miski następujące składniki:')

for l in list:
    print('➤', l)

print('''
Zmiksuj składniki do gładkiej masy
Rozgrzej patelnię
Usmaż naleśniki
Gotowe :)''')