#Utwórz zmienną przechowującą dowolny ciąg znaków.
#Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
#Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

magic = 'Abracadabra'

print('Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.')
magic_numb = len(magic)
if magic_numb > 5:
    print('Utworzony string jest dłuższy niż 5 znaków')
else:
    print('Utworzony string jest krótszy niż 5 znaków)')

magic = magic.lower()
print('Liczba wystąpień znaku "a" to' , end = ' ')
print(magic.count('a'),'.')
t = magic.count('a')

print()
print('Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.')

if t > 0:
    print(magic.replace('a', 'z'))
else:
    print('String nie zawiera znaku "a".')