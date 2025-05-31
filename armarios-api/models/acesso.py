from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Utilizadores(Base):

    __tablename__ = 'Utilizadores' 
    UID = Column(String(255), primary_key=True, unique=True, index=True)  
    Nome = Column(String(255)) 

class RegistoAcesso(Base):

    __tablename__ = "registo_acessos"
    Contador = Column(Integer, primary_key=True, autoincrement=True, index=True)
    ID_Armario = Column(Integer, primary_key=True, index=True)
    UID = Column(String(255), ForeignKey('Utilizadores.UID'))  
    Abertura = Column(DateTime, default=datetime.utcnow)
    Fecho = Column(DateTime, nullable=True, default=None)

class AcessosNegados(Base):

    __tablename__ = "Acessos_Negados"
    Contador = Column(Integer, primary_key=True, autoincrement=True, index=True)
    ID_Armario= Column(Integer, primary_key=True, index=True)
    UID_Rejeitado = Column(String(50), nullable=False, default='')
    Abertura = Column(DateTime, nullable=False, default=datetime.utcnow)
    Fecho = Column(DateTime, nullable=True, default=None)


class Permissoes(Base):
    __tablename__ = "Permissoes"
    UID = Column(String(255), ForeignKey('Utilizadores.UID'))  
    ID_Armario = Column(Integer, primary_key=True, index=True)
