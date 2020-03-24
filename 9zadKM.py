# Oblicz z pomocą pythona zapotrzebowanie kaloryczne:
# dla 25-letniej kobiety o wzroście 1.7m i wadze 63kg, która uprawia sport kilka razy w tygodniu
# 10 x masa ciała + 6.25 x wzrost w cm – 5 x wiek + S

print('Kalkulator zapotrzebowania kalorycznego')
op = "TAK"
while op == "TAK":

    plec = input('Jesteś kobietą (K) czy mężczyzną (M)? Wpisz odpowiednią literę: ')

    if plec == 'M':
        masaM = float(input('Proszę o podanie swojej wagi w kg: '))
        wzrostM = float(input('Proszę o podanie swojego wzrostu w cm: '))
        wiekM = float(input('Proszę o podanie swojego wieku: '))
        PPMM = (10 * masaM) + (6.25 * wzrostM) - (wiekM + 5)

        print('Proszę o określenie swojego trybu życia:')
        print('( 1 ) Praca siedząca, brak dodatkowej aktywności fizycznej.')
        print('( 2 ) Praca niefizyczna, mało aktywny tryb życia.')
        print('( 3 ) Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu.')
        print('( 4 ) Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu.')
        print('( 5 ) Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu.')

        opm = "M.TAK"
        while opm == "M.TAK":
            numer = input('Proszę o podanie numeru wybranej aktywności: ')

            if numer == '1':
                print('Twoje zapotrzebowanie kaloryczne to:', PPMM * 1.2 , 'kcal')
                break
            elif numer == '2':
                print('Twoje zapotrzebowanie kaloryczne to:', PPMM * 1.4, 'kcal')
                break
            elif numer == '3':
                print('Twoje zapotrzebowanie kaloryczne to:', PPMM * 1.6, 'kcal')
                break
            elif numer == '4':
                print('Twoje zapotrzebowanie kaloryczne to:', PPMM * 1.8, 'kcal')
                break
            elif numer == '5':
                print('Twoje zapotrzebowanie kaloryczne to:', PPMM * 2.0, 'kcal')
                break

            else:
                print('Podano nieprawidłową wartość.')
                opm = input("Czy chcesz ponownie wprowadzić hasło? (M.TAK/M.NIE)? ")

    elif plec == 'K':
        masaK = float(input('Proszę o podanie swojej wagi w kg: '))
        wzrostK = float(input('Proszę o podanie swojego wzrostu w cm: '))
        wiekK = float(input('Proszę o podanie swojego wieku: '))
        PPMK = (10 * masaK) + (6.25 * wzrostK) - (wiekK - 161)

        print('Proszę o określenie swojego trybu życia:')
        print('( 1 ) Praca siedząca, brak dodatkowej aktywności fizycznej.')
        print('( 2 ) Praca niefizyczna, mało aktywny tryb życia.')
        print('( 3 ) Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu.')
        print('( 4 ) Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu.')
        print('( 5 ) Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu.')

        opk = "K.TAK"
        while opk == "K.TAK":
                numer = input('Proszę o podanie numeru wybranej aktywności: ')

                if numer == '1':
                    print('Twoje zapotrzebowanie kaloryczne to:', PPMK * 1.2, 'kcal')
                    break
                elif numer == '2':
                    print('Twoje zapotrzebowanie kaloryczne to:', PPMK * 1.4, 'kcal')
                    break
                elif numer == '3':
                    print('Twoje zapotrzebowanie kaloryczne to:', PPMK * 1.6, 'kcal')
                    break
                elif numer == '4':
                    print('Twoje zapotrzebowanie kaloryczne to:', PPMK * 1.8, 'kcal')
                    break
                elif numer == '5':
                    print('Twoje zapotrzebowanie kaloryczne to:', PPMK * 2.0, 'kcal')
                    break
                else:
                    print('Podano nieprawidłową wartość.')
                    opk = input("Czy chcesz ponownie wprowadzić numer? (K.TAK/K.NIE)? ")

    else:
        print('Podano nieprawidłową wartość.')
    op = input("Czy chcesz ponownie wprowadzić podać wartość? (TAK/NIE)? ")

print('Dziękuję')