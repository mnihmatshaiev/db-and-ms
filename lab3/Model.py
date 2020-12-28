import psycopg2
import time
from psycopg2 import errors

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy import exc

Base = declarative_base()


class Film(Base):
    __tablename__ = 'film'
    film_id = Column(Integer, primary_key=True)
    film_name = Column(String(32))
    show = relationship('Show')

    def __repr__(self):
        return "<(film_id='{}', name='{}'>" \
            .format(self.film_id, self.film_name)


class Hall(Base):
    __tablename__ = 'hall'
    hall_name = Column(String(8))
    hall_id = Column(Integer, primary_key=True)
    capacity = Column(Integer)
    show = relationship("Show")

    def __repr__(self):
        return "<(hall_id='{}', hall_name='{}', capacity='{}'>" \
            .format(self.hall_id, self.hall_name, self.capacity)


class Show(Base):
    __tablename__ = 'show'
    show_id = Column(Integer, primary_key=True)
    hall_id = Column(Integer, ForeignKey('hall.hall_id'))
    film_id = Column(Integer, ForeignKey('film.film_id'))
    start_date = Column(Date)

    def __repr__(self):
        return "<(show_id='{}', hall_id='{}', film_id='{}', start_date='{}'>" \
            .format(self.show_id, self.hall_id, self.film_id, self.start_date)


class Ticket(Base):
    __tablename__ = 'ticket'
    show_id = Column(Integer, ForeignKey('show.show_id'), primary_key=True)
    row = Column(Integer, primary_key=True)
    seat = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<(show_id='{}', row='{}', seat='{}'>" \
            .format(self.show_id, self.row, self.seat)


def create(s, table, parameter_1, parameter_2, parameter_3):
    try:
        arg = None
        if table == 1:
            arg = Film(film_name=parameter_1)
        elif table == 2:
            arg = Hall(hall_name=parameter_1, capacity=parameter_2)
        elif table == 3:
            arg = Show(hall_id=parameter_1, film_id=parameter_2, start_date=parameter_3)
        elif table == 4:
            arg = Ticket(show_id=parameter_1, row=parameter_2, seat=parameter_3)
        s.add(arg)
        s.commit()
    except exc.SQLAlchemyError:
        s.rollback()
        print("Error")


def edit(s, table, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5):
    try:
        x = None
        if table == 1:
            x = s.query(Film).get(parameter_2)
            x.film_name = parameter_1
        elif table == 2:
            x = s.query(Hall).get(parameter_3)
            x.hall_name = parameter_1
            x.capacity = parameter_2
        elif table == 3:
            x = s.query(Show).get(parameter_4)
            x.hall_id = parameter_1
            x.film_id = parameter_2
            x.start_date = parameter_3
        elif table == 4:
            x = s.query(Ticket).get(parameter_3, parameter_4, parameter_5)
            x.row = parameter_1
            x.seat = parameter_2
        s.add(x)
    except exc.SQLAlchemyError:
        s.commit()
        print("Error")


def delete(s, table, parameter_1, parameter_2, parameter_3):
    try:
        x = None
        if table == 1:
            x = s.query(Film).get(parameter_1)
        elif table == 2:
            x = s.query(Hall).get(parameter_1)
        elif table == 3:
            x = s.query(Show).get(parameter_1)
        elif table == 4:
            x = s.query(Ticket).get((parameter_1, parameter_2, parameter_3))
        s.delete(x)
        s.commit()
    except exc.SQLAlchemyError:
        s.rollback()
        print("Error")


def print_table(s, table):
    if table == 1:
        for film in s.query(Film).all():
            print(film)
    elif table == 2:
        for hall in s.query(Hall).all():
            print(hall)
    elif table == 3:
        for show in s.query(Show).all():
            print(show)
    elif table == 4:
        for ticket in s.query(Ticket).all():
            print(ticket)