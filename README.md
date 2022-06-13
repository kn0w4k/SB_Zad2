# SB_Zad2
Symulator Biznesu Zadanie 2

pip install psycopg2 żeby móc się łączyć z bazą postgresql

#Funkcje
Funkcja UserInterface() jest startem gdzie wprowadzamy wartości dowolne w odpowiednie kategorie bo nie mam symulacji.

Funkcja generateUserID losuje numer id w zakresie 1000-9999 dla identyfikatora użytkownika.

Funkcja insert_data() zapisuje dane w bazie danych w 3 tabelach (user_data, questions i answers) postgresql.

Miałem pierwotnie taki plan żeby zrobić trigger, który by z tabeli user_data zapisywał po insert/update wartości do questions i answers ale
ostatecznie mi się nie udało i za późno się za to zabrałem.

#Struktura sql tabel i type enum:

create type types as enum ('1_correct', '2_correct', '3_correct', 'order');

create table questions
(
	id varchar(8) not null,
	text text not null,
	type types not null,
	primary key (id)
);

create table user_data
(
	id varchar(8) not null,
	wartosc_sprzedazy integer not null,
	koszt_sprzedanego_towaru integer not null,
	koszty_stale integer not null,
	primary key (id)
);

create table answers
(
	id serial,
	question_id varchar(8) not null,
	is_correct boolean,
	value integer not null,
	primary key (id),
	foreign key (question_id) references questions
);

