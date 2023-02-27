from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from alch_db import Base

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(40), nullable=False)
    login = Column(String(40), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)

    def __init__(self, name, login, password, email):
        self.name = name
        self.login = login
        self.password = password
        self.email = email

    def __repr__(self):
        return f'<User {self.name}>'

class Vacancy(Base):
    __tablename__ = 'vacancy'
    vacancy_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    status = Column(Integer, nullable=False)
    position_name = Column(String(50), nullable=False)
    company = Column(String(50), nullable=False)
    creation_date = Column(String(40), default=datetime.now().isoformat())
    description = Column(String(200), nullable=False)
    contacts_id = Column(String(120))
    comment = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)

    def __init__(self, status, position_name, company, description, contacts_id, comment, user_id):
        self.status = status
        self.position_name = position_name
        self.company = company
        self.description = description
        self.contacts_id = contacts_id
        self.comment = comment
        self.user_id = user_id

    def __repr__(self):
        return f'<Vacancy {self.position_name}>'

class Events(Base):
    __tablename__ = 'events'
    event_id = Column(Integer, primary_key=True, nullable=False)
    vacancy_id = Column(Integer, ForeignKey('vacancy.vacancy_id'))
    title = Column(String(80), nullable=False)
    description = Column(String(200), nullable=False)
    event_date = Column(DateTime)
    due_to_date = Column(DateTime)
    status = Column(Integer, nullable=False)

    def __init__(self, event_id, vacancy_id, title, description, event_date, due_to_date, status):
        self.event_id = event_id
        self.vacancy_id = vacancy_id
        self.title = title
        self.description = description
        self.event_date = event_date
        self.due_to_date = due_to_date
        self.status = status

    def __repr__(self):
        return f'<Vacancy {self.title}>'
