import random

import psycopg2

# pip install psycopg2;

connection = psycopg2.connect(
    database='Symulator_Biznesu',
    user='username',
    password='password',
    host='localhost',
    port='5432'
)
cursor = connection.cursor()


def generateUserID():
    randID = 'user' + str(random.randrange(1000, 10000))
    return randID


def answer_Question(us_id):
    cursor.execute("SELECT text FROM questions WHERE id='{0}'".format(us_id))
    question = str(cursor.fetchall())
    question = question[3:-4]
    print(question)
    cursor.execute("SELECT value FROM answers WHERE question_id='{0}'".format(us_id))
    value = str(cursor.fetchall())
    value = int(value[2:-3])
    answer = int(input())
    if answer == value:
        print("Poprawna odpowiedź")
        cursor.execute("UPDATE answers SET is_correct = true WHERE question_id ='{0}'".format(us_id))
        connection.commit()
    else:
        print("Twój biznes upadł i nadszedł trzeci 'Wielki Kryzys'")
        print("Poprawna odpowiedź to: " + str(value))
        cursor.execute("UPDATE answers SET is_correct = false WHERE question_id ='{0}'".format(us_id))
        connection.commit()


def insert_data(us_id, ws, kspt, kst):
    cursor.execute(
        "INSERT INTO user_data(id, wartosc_sprzedazy, koszt_sprzedanego_towaru, koszty_stale) VALUES ('{0}', {1}, {2}, {3})".format(
            us_id, ws, kspt, kst))

    question = 'W marcu Twój sklep osiągnął wartość sprzedaży {0} zł, koszt sprzedanego towaru wynosi {1} zł. Koszty stałe sklepu wyniosły {2} zł. Oblicz próg rentowności sklepu.'.format(
        ws, kspt, kst)
    cursor.execute(
        "INSERT INTO questions(id, text, type) VALUES ('{0}', '{1}', '{2}')".format(us_id, question, '1_correct'))

    results = int(ws * (kst / (ws - kspt)))
    cursor.execute(
        "INSERT INTO answers(question_id, is_correct, value) VALUES ('{0}', NULL, {1})".format(us_id, results))

    connection.commit()
    answer_Question(us_id)


def UserInterface():
    print("Witamy w symulacji!")
    print("Podaj wartość sprzedaży")
    wartosc_sprzedazy = int(input())
    print("Podaj koszt sprzedanego towaru")
    koszt_spt = int(input())
    print("Podaj koszt stały")
    koszt_st = int(input())
    insert_data(generateUserID(), wartosc_sprzedazy, koszt_spt, koszt_st)


if __name__ == '__main__':
    UserInterface()
