DROP TABLE Rodzaje CASCADE;
CREATE TABLE Rodzaje(
	rodzaj varchar(50) PRIMARY KEY ); --poszlo 
	
DROP TABLE Seriale CASCADE;
CREATE TABLE Seriale(
	id_serialu SERIAL PRIMARY KEY NOT NULL,
	tytuł TEXT UNIQUE NOT NULL,
	rodzaj varchar(50)  NOT NULL   REFERENCES Rodzaje(rodzaj) ON DELETE CASCADE, 
	rok INTEGER NOT NULL CHECK(rok > 1920),
	kraj TEXT NOT NULL,
	liczba_sezonow INTEGER NOT NULL DEFAULT(1) CHECK(liczba_sezonow > 0 ));---poszlo 
	
DROP TABLE Oceny CASCADE;
CREATE TABLE Oceny(
id_serialu INTEGER REFERENCES Seriale(id_serialu) ON DELETE RESTRICT ON UPDATE CASCADE,
imdb FLOAT NOT NULL CHECK (imdb > 0),
filmweb FLOAT NOT NULL CHECK (filmweb > 0),
studenci FLOAT NOT NULL CHECK (studenci > 0),
srednia FLOAT,
PRIMARY KEY (id_serialu)
);--- tutaj daje nulle bo wyliczymy srednia z funkcji wiec na poczatku nic nie wstawimy --poszlo

DROP TABLE Producenci CASCADE; 
CREATE TABLE Producenci(
	id_producenta SERIAL PRIMARY KEY NOT NULL,
	nazwa_producenta VARCHAR(50) UNIQUE NOT NULL);-----poszlo

DROP TABLE Produkcja CASCADE;
CREATE TABLE Produkcja(
id_producenta INTEGER NOT NULL,
nazwa_serialu VARCHAR(50) NOT NULL,
Foreign KEY(id_producenta) REFERENCES Producenci(id_producenta) ON DELETE RESTRICT ON UPDATE CASCADE);----poszlo --- jak chce tez dodac jako foreign key to moge jak w tabeli ponizej 
	
DROP TABLE Tworcy_serialu CASCADE ;
CREATE TABLE Tworcy_serialu(
nazwisko Varchar(50) NOT NULL,
id_serialu INTEGER NOT NULL,
FOREIGN KEY(id_serialu) REFERENCES Seriale(id_serialu) ON DELETE RESTRICT ON UPDATE CASCADE);--- jak daje tutaj foreign key to mus byc z cala reszta 
--poszlo 

DROP TABLE Aktorzy CASCADE;
CREATE TABLE Aktorzy(
	imie Varchar(50),
	nazwisko Varchar(50) NOT NULL,
	tytul Varchar(50) NOT NULL,
	plec Varchar(50) NOT NULL);--poszlo 
	
DROP TABLE Katalog CASCADE;
CREATE TABLE Katalog(
	id_kopii SERIAL PRIMARY KEY NOT NULL,
	id_serialu INT NOT NULL ,
	sezon INTEGER NOT NULL CHECK(sezon >= 1),
	dostepnosc  BOOLEAN DEFAULT(true) NOT NULL,
	cena FLOAT NOT NULL DEFAULT(10),
	FOREIGN KEY (id_serialu) REFERENCES Seriale(id_serialu) ON DELETE RESTRICT ON UPDATE CASCADE);-----poszlo 
	
--DROP TABLE Nosnik CASCADE;
--CREATE TABLE Nosnik(
--	id_kopi INT NOT NULL ,
--	typ Varchar(50) ,
--	PRIMARY KEY (id_kopi),
--	FOREIGN KEY(id_kopi)REFERENCES Katalog(id_kopi)ON DELETE RESTRICT ON UPDATE CASCADE );----poszlo 


------------------- wywalam sezon 
--ALTER TABLE katalog
--DROP COLUMN sezon ;

DROP TABLE Klienci CASCADE;
CREATE TABLE Klienci(
id_klienta SERIAL PRIMARY KEY NOT NULL,
imie TEXT,
nazwisko TEXT NOT NULL,
nr_telefonu INTEGER,
e_mail Varchar(50) NOT NULL UNIQUE);

DROP TABLE Wypozyczone CASCADE;
CREATE TABLE Wypozyczone(
id_kopii INT NOT NULL PRIMARY KEY,
tytul_serialu TEXT NOT NULL,
id_klienta INT NOT NULL,
data_wyp  DATE NOT NULL CHECK (data_wyp = current_date),
FOREIGN KEY(id_kopii)REFERENCES Katalog(id_kopii)ON DELETE RESTRICT ON UPDATE CASCADE);









-----------------------------------!!!!!!!!!!!!!------------------------------------------
Create table ser_kat AS
SELECT * FROM katalog as k 
JOIN seriale USING(id_serialu)

INSERT INTO klienci(imie,nazwisko,nr_telefonu,e_mail)
VAlues
('Szymon','Czop',123456789,'szymonczop@malpa.pl'),
('Marta','Kaluzna',987654321,'k.marta@prawda.pl');


INSERt INTO wypozyczone(id_kopii,tytul_serialu,id_klienta,data_wyp)
VALUES(9,'Kompania braci',1,'2019-01-29');



	