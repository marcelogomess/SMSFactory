from sqlalchemy import Column, ForeignKey, Integer, String, CHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

Base = declarative_base()

class Empresas(Base):
    __tablename__ = 'empresas'
    id = Column(Integer, primary_key=True)
    nome_fantasia = Column(String(250), nullable=False)
    razao_social = Column(String(250), nullable=False)
    cnpj = Column(String(60), nullable=True)

class Modems(Base):
    __tablename__ = 'modems'
    id = Column(Integer, primary_key=True)
    imei_modem = Column(String(60), nullable=True)
    imei_chip = Column(String(60), nullable=True)
    marca = Column(String(60),nullable=True)
    situacao = Column(CHAR, nullable=False, default='D')
    dispositivo = Column(String(250), nullable=False)
    data_registro = Column(DateTime, default=datetime.datetime.now)
    data_modificacao = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now)

class Campanhas(Base):
    __tablename__ = 'campanhas'
    id = Column(Integer, primary_key=True)
    id_empresa = Column(Integer, ForeignKey('empresas.id'))
    mensagem = Column(String(250), nullable=False)
    situacao = Column(CHAR, nullable=False, default='D')
    data_registro = Column(DateTime, default=datetime.datetime.now)
    data_modificacao = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now)

class Telefones(Base):
    __tablename__ = 'telefones'
    id = Column(Integer, primary_key=True)
    id_campanha = Column(Integer,ForeignKey('campanhas.id'))
    numero = Column(String(20), nullable=False)
    operadora = Column(String(30), nullable=True)
    data_registro = Column(DateTime, default=datetime.datetime.now)

class Envios(Base):
    __tablename__ = 'envios'
    id = Column(Integer, primary_key=True)
    id_empresa = Column(Integer, ForeignKey('empresas.id'))
    id_campanha = Column(Integer, ForeignKey('campanhas.id'))
    id_modem = Column(Integer, ForeignKey('modems.id'))
    id_telefone = Column(Integer, ForeignKey('telefones.id'))
    situacao = Column(CHAR, nullable=False, default='P')
    data_registro = Column(DateTime, default=datetime.datetime.now)
    data_modificacao = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now)


class Recebimentos(Base):
    __tablename__ = 'recebimentos'
    id = Column(Integer, primary_key=True)
    remetente = Column(String(60), nullable=False)
    destinatario = Column(String(60), nullable=False)
    mensagem = Column(String(250))
    situacao = Column(CHAR, nullable=False, default='P')
    data_registro = Column(DateTime, default=datetime.datetime.now)
    data_modificacao = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now)


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(250), nullable=False)
    usuario = Column(String(20), nullable=False)
    senha = Column(String(20), nullable=False)
    email = Column(String(60), nullable=True)
    id_empresa = Column(Integer, ForeignKey('empresas.id'))


engine = create_engine('sqlite:///smsfactory.db')
Base.metadata.create_all(engine)

