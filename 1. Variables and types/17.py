# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro lub w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

print('KANTOR ONLINE - NISKIE CENY')

exchange_euro = 4.19
exchange_dolar = 3.90

a = input("Proszę o podanie kwoty która zostanie wykorzystana w docelowym miejscu: ")
print("Dziękuję. Wprowadzona kwota wynosi:", a, 'PLN')

money_holiday = float(a)

currency_what = input('Z jakiej waluty skorzystasz w docelowym miejscu? WPISZ EURO LUB DOLAR: ')
if currency_what != 'DOLAR':
    calculation_euro = money_holiday / exchange_euro
    print('Kwota po przeliczeniu wynosi', round(calculation_euro), '€')
else:
    calculation_dolary = money_holiday / exchange_dolar
    print('Kwota po przeliczeniu wynosi', round(calculation_dolary), '$')

print('Życzymy miłej podróży')