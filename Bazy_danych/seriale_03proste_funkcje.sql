


-------------------- Zmiana ceny ze wzgledu na tytul
CREATE OR REPLACE FUNCTION zmiana_ceny_tytul(tytul_serialu TEXT , procent DECIMAL(3,2)) RETURNS TEXT AS $$
BEGIN
	UPDATE ser_kat SET cena= cena + procent*cena WHERE tytul_serialu = tytuł;
	RETURN 'Zmiana cen filmów z roku ' || rok_wydania;
END;
$$ LANGUAGE 'plpgsql';

—- jak dziala? —-
SELECT * FROM ser_kat;
SELECT zmiana_ceny_rok(2015, 0.2);
SELECT * FROM ser_kat where rok = 2015;

------- Zmiana ceny dla seriali od konkretnego roku 
—- funkcja zmieniajaca ceny wedlug kategorii (blu-ray/cd)—
CREATE OR REPLACE FUNCTION zmiana_ceny_rok(rok_wydania INTEGER) RETURNS TEXT AS $$
BEGIN
	UPDATE ser_kat SET cena = 15 WHERE rok >= rok_wydania;
	RETURN 'Zmiana cen filmów z roku ' || rok_wydania;
END;
$$ LANGUAGE 'plpgsql';

------------------------------

