-- Tworzymy wyzwalacz dzięki któremu każdy serial, który trafia do tabeli Seriale
-- będzie również trafiać do tabeli Katalog

CREATE OR REPLACE FUNCTION dodaj_serial() RETURNS TRIGGER AS $$
BEGIN
	INSERT INTO Katalog (id_serialu) VALUES(NEW.id_serialu);
	RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';


DROP TRIGGER IF EXISTS dodaj_trig ON Seriale;
CREATE TRIGGER dodaj_trig
AFTER INSERT ON Seriale
FOR EACH ROW EXECUTE PROCEDURE dodaj_serial();


-- II wyzwalacz
-- Tworzymy wyzwalacz odpowiedzialny za korygowanie dostępności seriali
CREATE OR REPLACE FUNCTION wyp_serial() RETURNS TRIGGER AS $$
BEGIN
	UPDATE ser_kat SET dostepnosc = FALSE WHERE id_kopii = NEW.id_kopii;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';





DROP TRIGGER IF EXISTS wyp_trig ON wypozyczone;
CREATE TRIGGER wyp_trig
AFTER INSERT ON wypozyczone
FOR EACH ROW EXECUTE PROCEDURE wyp_serial();

INSERT INTO wypozyczone(id_kopii,tytul_serialu,id_klienta,data_wyp)
VALUES(1,'Gra o tron',2,'2019-01-30'),
(13,'Narcos',1,'2019-01-30');


-- III wyzwalacz
-- Tworzymy wyzwalacz, który z powrotem nadaje wartość TRUE
-- po usunięciu krotki z tabeli Wypożyczone

CREATE OR REPLACE FUNCTION od_serial() RETURNS TRIGGER AS $$
BEGIN
	UPDATE ser_kat SET dostepnosc = True WHERE id_kopii = OLD.id_kopii;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

DROP TRIGGER IF EXISTS od_trig ON Wypozyczone;
CREATE TRIGGER od_trig
AFTER DELETE ON Wypozyczone
FOR EACH ROW EXECUTE PROCEDURE od_serial();

DELETE FROM wypozyczone where id_klienta = 1;
