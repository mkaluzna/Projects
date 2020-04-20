## Baza użytkowników
from user import User

class Users():
    def __init__(self):
        self.users = []
        self.logins = []
        self.krotki = {} # (login, hasło)

    def add_user(self, login, password):
        login = str(login)
        password = str(password)
        if login not in self.logins:
            uzytkownik = User(login, password)
            self.logins.append(login)
            self.users.append(uzytkownik)
            self.krotki[login] = password
        else:
            raise ValueError('Użytkownik o podanym loginie już istnieje!')

    def delete_user(self, login, password):
        if login in self.logins and self.krotki[login] == password:
            self.logins.remove(login)
            del self.krotki[login]
            for user in self.users:
                if user.login == login:
                    self.users.remove(user)
        else:
            raise ValueError('Użytkownik o podanym loginie nie istnieje lub wprowadzono nieprawidłowe hasło!')

    def show_users(self):
        return ', '.join(self.logins)

    def select_user(self, login, password):
        if login in self.logins and self.krotki[login] == password:
            for user in self.users:
                if user.login == login:
                    return user
        else:
            raise ValueError('Użytkownik o podanym loginie nie istnieje lub wprowadzono nieprawidłowe hasło!')

    def change_pass(self, login, password1, password2):
        if login in self.logins and password1 == self.krotki[login]:
            for user in self.users:
                if user.login == login:
                    user.change_password(password2)
                    self.krotki[login] = password2
        else:
            raise ValueError('Użytkownik o podanym loginie nie istnieje lub wprowadzono nieprawidłowe hasło!')

if __name__ == "__main__":
    uzytkownicy = Users()