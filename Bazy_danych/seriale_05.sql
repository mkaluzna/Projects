-----------------WIDOKI
CREATE VIEW seriale_widok AS
SELECT Seriale.id_serialu, Seriale.tytuł, Seriale.rodzaj, Oceny2.srednia, producenci.nazwa_producenta
FROM Oceny2
JOIN Seriale ON (Seriale.id_serialu = Oceny2.id_serialu)
JOIN Produkcja ON (Produkcja.nazwa_serialu = Seriale.tytuł)
JOIN Producenci ON (Produkcja.id_producenta = Producenci.id_producenta);

CREATE VIEW wypozyczone_widok AS
SELECT Klienci.imie, Klienci.nazwisko, Wypozyczone.id_kopii, Wypozyczone.tytul_serialu, Wypozyczone.data_wyp
FROM Klienci
JOIN Wypozyczone ON (Wypozyczone.id_klienta = Klienci.id_klienta);