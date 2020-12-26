import psycopg2
import time
from psycopg2 import errors


def create(cursor, table, parameter_1, parameter_2, parameter_3):
    try:
        if table == 1:
            cursor.execute("INSERT INTO film (film_name) VALUES (%s)", (str(parameter_1),))
        elif table == 2:
            cursor.execute("INSERT INTO hall (hall_name, capacity) VALUES (%s, %s)", (parameter_1, parameter_2,))
        elif table == 3:
            cursor.execute("INSERT INTO show (film_id, hall_id, start_date)"
                           " VALUES (%s, %s, %s)", (parameter_1, parameter_2, parameter_3))
        elif table == 4:
            cursor.execute("INSERT INTO ticket (show_id, row, seat)"
                           " VALUES (%s, %s, %s)", (parameter_1, parameter_2, parameter_3,))
    except errors.ForeignKeyViolation:
        print("Error, ENTER WRONG DATA\n")


def delete(cursor, table, parameter, parameter_2, parameter_3):
    if table == 1:
        cursor.execute("DELETE FROM film WHERE film_id = %s", [parameter])
    elif table == 2:
        cursor.execute("DELETE FROM hall WHERE hall_id = %s", [parameter])
    elif table == 3:
        cursor.execute("DELETE FROM show WHERE show_id = %s", [parameter])
    elif table == 4:
        cursor.execute("DELETE FROM ticket WHERE show_id = %s and row = %s and seat = %s",
                       (parameter, parameter_2, parameter_3,))


def edit(cursor, table, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5):
    try:
        if table == 1:
            cursor.execute("UPDATE film SET film_name = %s"
                           " WHERE film_id = %s", (parameter_1, parameter_2,))
        elif table == 2:
            cursor.execute("UPDATE hall SET hall_name = %s, capacity = %s"
                           " WHERE hall_id = %s", (parameter_1, parameter_2, parameter_3,))
        elif table == 3:
            cursor.execute("UPDATE show SET film_id = %s, hall_id = %s, start_date = %s"
                           " WHERE show_id = %s", (parameter_1, parameter_2, parameter_3, parameter_4,))
        elif table == 4:
            cursor.execute("UPDATE ticket SET row = %s, seat = %s"
                           " WHERE show_id = %s and row = %s and seat = %s",
                           (parameter_1, parameter_2, parameter_3, parameter_4, parameter_5,))
    except errors.ForeignKeyViolation:
        print("Error, ENTER WRONG DATA\n")


def print_table(cursor, table):
    cursor.execute("SELECT * FROM {}".format(table))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def random_generation(cursor, table, number):
    try:
        if table == 1:
            cursor.execute("INSERT INTO film (film_name) SELECT chr(trunc(65 + random()*25)::int)||"
                           " chr(trunc(65 + random()*25)::int) FROM generate_series(1, %s)", [number])
        elif table == 2:
            cursor.execute("INSERT INTO hall (hall_name, capacity) "
                           " SELECT chr(trunc(65 + random()*25)::int)|| chr(trunc(65 + random()*25)::int),"
                           " trunc(random()*100::int) FROM generate_series(1, %s)", [number])
        elif table == 3:
            cursor.execute("INSERT INTO show (start_date, film_id, hall_id) "
                           "SELECT timestamp '2020-01-20 20:00:00' "
                           "+ random() * (timestamp '2020-10-20 20:00:00' - timestamp '2020-01-10 10:00:00'),"
                           "film_id, hall_id FROM film TABLESAMPLE BERNOULLI (100), hall TABLESAMPLE BERNOULLI (100)")
        elif table == 4:
            cursor.execute("INSERT INTO ticket (row, seat, show_id) SELECT  trunc(random()*25::int), "
                           "trunc(random()*100::int), show_id FROM show TABLESAMPLE bernoulli(100) ")
    except psycopg2.errors.UniqueViolation:
        print("Error\n")


def select_function(cursor, parameter, item):
        if item == 1:
            t1 = time.perf_counter()
            cursor.execute("with a as (SELECT film_id FROM film"
                           " where film.film_name = %s), "
                           "b as (SELECT hall_id FROM show inner join a on show.film_id = a.film_id)"
                           " SELECT hall_name from hall join b on hall.hall_id = b.hall_id", (str(parameter),))
            t2 = time.perf_counter()
            row = cursor.fetchone()
            print("Hall_name")
            print(row)
            print("Request processing time ", t2 - t1)
        elif item == 2:
            t1 = time.perf_counter()
            cursor.execute("with a as (SELECT show_id FROM show"
                           " where show.film_id = %s)"
                           " SELECT count(seat) FROM ticket join a on ticket.show_id = a.show_id",
                           [parameter])
            t2 = time.perf_counter()
            row = cursor.fetchone()
            print("Number of seats")
            print(row)
            print("Request processing time ", t2 - t1)
        elif item == 3:
            t1 = time.perf_counter()
            cursor.execute("with a as (SELECT hall_id FROM show"
                           " where show.show_id = %s)"
                           " SELECT capacity FROM hall join a on hall.hall_id = a.hall_id",
                           [parameter])
            t2 = time.perf_counter()
            row = cursor.fetchone()
            print("Capacity")
            print(row)
            print("Request processing time ", t2 - t1)
