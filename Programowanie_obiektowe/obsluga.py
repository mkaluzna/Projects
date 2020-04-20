## Interakcja z użytkownikiem
from users import Users
from generator import Generator
from matplotlib import pyplot as plt
import pickle
import os
import seaborn as sns

def interaction():
    print('Witaj w programie, w którym zaplanujesz swój budżet. W razie problemów wpisz "help".')

    if os.path.exists('Uzytkownicy'):
        with open('Uzytkownicy', 'rb') as o:
            uzytkownicy = pickle.load(o)
    else:
        uzytkownicy = Users()

    help = '1 - Utwórz profil \n2 - Usuń profil \n3 - Wyświetl nazwy użytkowników \n4 - Wybierz profil (zaloguj się) ' \
           '\n5 - Przypomnij hasło \n6 - Zakończ program\n'

    while True:
        wybor = input('Co chcesz zrobić?   ').lower()

        #pomoc
        if wybor == 'help':
            print(help)

        # tworzenie profilu
        elif wybor == '1':
            try:
                login = input('Podaj login: ')
                haslo = input('Podaj hasło: ')
                # jeśli ktoś z takim loginem już istnieje: błąd
                if login in uzytkownicy.logins:
                    raise ValueError
                # gdy nie było jeszcze takiego loginu
                else:
                    uzytkownicy.add_user(login, haslo)
                    print('Użytkownik został dodany\n')
                    with open(login + '_pass', 'wb') as g:
                        pickle.dump(haslo, g)
            except ValueError:
                print('Użytkownik o podanym loginie już istnieje. Spróbuj jeszcze raz.\n')

        # koniec programu
        elif wybor == '6':
            odp = input('Czy na pewno chcesz wyjść z programu? T/N     ').upper()
            if odp == 'T':
                with open('Uzytkownicy', 'wb') as u:
                    pickle.dump(uzytkownicy, u)
                return
            else:
                pass

        # usuwanie profilu
        elif wybor == '2':
            try:
                login = input('Podaj login użytkownika, którego chcesz usunąć (UWAGA: Ta operacja usunie wszystkie dane '
                              'związane z podanym profilem): ')
                if login in uzytkownicy.logins:
                    haslo = input('Podaj hasło: ')
                    uzytkownicy.delete_user(login, haslo)
                    print('Użytkownik został usunięty\n')
                    # usuwamy informacje o uzytkowniku (login, haslo, budzet)
                    if os.path.exists(login + '_pass'):
                        os.remove(login + '_pass')
                    if os.path.exists(login + '_budget'):
                        os.remove(login + '_budget')
                else:
                    raise ValueError
            except ValueError:
                print('Użytkownik o podanym loginie nie istnieje lub wprowadzone hasło jest nieprawidłowe. '
                      'Spróbuj jeszcze raz.\n')

        # wyświetlanie obecnych użytkowników
        elif wybor == '3':
            if len(uzytkownicy.logins) == 0:
                print('Brak użytkowników\n')
            else:
                print('Obecni użytkownicy to: ' + uzytkownicy.show_users() + '\n')

        # przypomnienie hasła
        elif wybor == '5':
            try:
                login = input('Podaj login: ')
                if os.path.exists(login + '_pass'):
                    with open(login + '_pass', 'rb') as g:
                        haslo = pickle.load(g)
                        print('Twoje hasło to: ' + haslo)
                else:
                    raise ValueError
            except ValueError:
                print('Użytkownik o podanym loginie nie istnieje. Spróbuj jeszcze raz.')

        # logowanie się na konto
        elif wybor == '4':
            try:
                login = input('Podaj login: ')
                haslo = input('Podaj hasło: ')
                if os.path.exists(login + '_pass'):
                    with open(login + '_pass', 'rb') as p:
                        check = pickle.load(p)
                        if haslo == check:
                            if login not in uzytkownicy.logins:
                                uzytkownicy.add_user(login,haslo)
                            user = uzytkownicy.select_user(login, haslo)
                            print('Pomyślne zalogowanie do programu. W razie problemów, wpisz help.\n')
                        else:
                            raise ValueError
                else:
                    raise ValueError

                help2 = '\n1 - Zmień hasło \n2 - Dodaj transakcję' \
                        '\n3 - Pokaż wszystkie transakcje \n4 - Pokaż budżet \n5 - Pokaż ostrzeżenia ' \
                        '\n6 - Pokaż tabelę \n7 - Wyczyść cały budżet ' \
                        '\n8 - Wróć do poprzedniego menu \n9 - Zapisz zmiany \n10 - Stwórz przykładowy budżet '

                # wczytujemy budżet użytkownika, jeśli już istnieje
                if os.path.exists(user.login + '_budget'):
                    with open(user.login + '_budget', 'rb') as h:
                        budzet = pickle.load(h)
                        user.budzet = budzet

                while True:
                    wybor2 = input('Co dalej?     ').lower()

                    # pomoc
                    if wybor2 == 'help':
                        print(help2)

                    # powrót do poprzedniego menu
                    elif wybor2 == "8":
                        odp = input('Pamiętaj, aby zapisać zmiany! Czy na pewno chcesz wrócić do poprzedniego menu? T/N ')\
                            .upper()
                        if odp == 'T':
                            break
                        elif odp == 'N':
                            pass

                    elif wybor2 == '10':
                        n = int(input('Podaj przykładową liczbę transakcji w miesiącu:  '))
                        example = Generator(n)
                        example.simulation()

                    # zapisywanie zmian
                    elif wybor2 == '9':
                        # zapisujemy budżet użytkownika
                        with open(user.login + '_budget', 'wb') as f:
                            pickle.dump(user.budzet, f)

                        # zapisujemy ramki danych
                        fig = plt.figure(facecolor='w', edgecolor='k')
                        sns.heatmap(user.budzet.show_df_inc(), annot=True, cmap='viridis', cbar=False)
                        plt.savefig(user.login + '_inc')

                        fig = plt.figure(facecolor='w', edgecolor='k')
                        sns.heatmap(user.budzet.show_df_exp(), annot=True, cmap='viridis', cbar=False)
                        plt.savefig(user.login + '_exp')

                        fig = plt.figure(facecolor='w', edgecolor='k')
                        sns.heatmap(user.budzet.show_df_details(), annot=True, cmap='viridis', cbar=False)
                        plt.savefig(user.login + '_details')

                        # zapisywanie wykresów
                        user.budzet.show_pieplot()
                        plt.savefig(user.login + '_pie')
                        user.budzet.show_barplot()
                        plt.savefig(user.login + '_bar')

                    # zmiana hasła
                    elif wybor2 == '1':
                        try:
                            password = input('Podaj obecne hasło: ')
                            password2 = input('Podaj nowe hasło: ')
                            uzytkownicy.change_pass(user.login, password, password2)
                            print('Hasło zostało zmienione\n')
                            with open(user.login + '_pass', 'wb') as g:
                                pickle.dump(password2, g)
                        except ValueError:
                            print('Spróbuj ponownie\n')

                    # wprowadzenie transakcji / dodanie kategorii
                    elif wybor2 == '2':
                        print(user.budzet.kategorie)
                        typ = input('Wydatek czy przychód? (W/P) ').upper()

                        if typ == 'P':
                            dzialanie = input('Aby dodać nową kategorię wciśnij K, aby wprowadzić przychód wciśnij P:   ')\
                                .upper()
                            if dzialanie == 'K':
                                try:
                                    new_cat = input('Podaj nową kategorię:  ')
                                    user.budzet.add_inc_cat(new_cat)
                                    print('Pomyślnie dodano nową kategorię.')
                                except ValueError:
                                    print('Podana kategoria już istnieje. Spróbuj jeszcze raz.')
                            elif dzialanie == 'P':
                                try:
                                    category = input('Podaj kategorię: ')
                                    t = input('Podaj typ budżetu (r/p): ').lower()
                                    amount = float(input('Podaj kwotę: '))
                                    day = int(input('Podaj dzień: '))
                                    user.add_inc(category, t, amount, day)
                                    print('Dodano nowy przychód')
                                except ValueError:
                                    print('Coś poszło nie tak... Spróbuj jeszcze raz.')
                            else:
                                print('Masz do wyboru literkę P lub K. Spróbuj ponownie.')

                        elif typ == 'W':
                            dzialanie2 = input('Aby dodać nową kategorię wciśnij K, aby wprowadzić wydatek wciśnij W:   ').upper()
                            if dzialanie2 == 'K':
                                try:
                                    new_cat = input('Podaj nową kategorię:  ')
                                    user.budzet.add_exp_cat(new_cat)
                                    print('Pomyślnie dodano nową kategorię')
                                except ValueError:
                                    print('Podana kategoria już istnieje. Spróbuj jeszcze raz.')
                            elif dzialanie2 == 'W':
                                try:
                                    category = input('Podaj kategorię: ')
                                    t = input('Podaj typ budżetu (r/p): ').lower()
                                    amount = float(input('Podaj kwotę: '))
                                    day = int(input('Podaj dzień: '))
                                    user.add_exp(category, t, amount, day)
                                    print('Dodano nowy wydatek')
                                except ValueError:
                                    print('Coś poszło nie tak... Spróbuj jeszcze raz.')
                            else:
                                print('Masz do wyboru literkę W lub K. Spróbuj ponownie.')

                    # pokaż wszystkie transakcje
                    elif wybor2 == '3':
                        print(user.show_trans())

                    # pokaż inf. o budżecie
                    elif wybor2 == '4':
                        print(user.show_budget())

                    # pokaż ostrzeżenia
                    elif wybor2 == '5':
                        print(user.show_warnings())

                    # pokaż tabelę
                    elif wybor2 == '6':
                        tab = input('Przychodów (P), wydatków (W) czy wydatków dzień po dniu (D)?').upper()
                        if tab == 'P':
                            print(user.budzet.show_df_inc())
                        elif tab == 'W':
                            print(user.budzet.show_df_exp())
                        elif tab == 'D':
                            print('Wybierz zakres dni:')
                            try:
                                a = int(input('od: '))
                                if a < 1 or a > 31:
                                    raise ValueError
                                b = int(input('do: '))
                                if b < 1 or b > 31:
                                    raise ValueError
                                print(user.budzet.show_selected_days(a,b))
                            except ValueError:
                                print('Podano nieprawidłowy zakres (0 < a,b < 31). Spróbuj jeszcze raz.')
                        else:
                            print('Masz do wyboru literki: P/W/D. Spróbuj ponownie.')

                    elif wybor2 == '7':
                        answer = input('Czy jesteś pewny, że chcesz usunąć wszystkie dane ze swojego budżetu? (T/N)').upper()
                        if answer == 'T':
                            user.clear_budget()
                        elif answer == 'N':
                            pass

                    else:
                        print('Wspomóż się poleceniem "help"\n')

            except ValueError:
                print('Użytkownik o podanym loginie nie istnieje lub wprowadzone hasło jest nieprawidłowe. Spróbuj jeszcze raz.\n')

        else:
            print('Wspomóż się poleceniem "help"\n')

if __name__ == '__main__':
    interaction()
