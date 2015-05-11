from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setupDatabase import Base, Empresas, Modems, Campanhas, Telefones, Envios, Recebimentos, Usuarios

engine = create_engine('sqlite:///smsfactory.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_empresa = Empresas(nome_fantasia='Sem empresa', razao_social='Sem empresa', cnpj='0000000000000')
session.add(new_empresa)
session.commit()

new_modem = Modems(imei_modem='000000000000', imei_chip='000000000000', marca='Sem marca',
                   situacao='A', dispositivo='/dev/USBx')
session.add(new_modem)
session.commit()

new_campanha = Campanhas(id_empresa=1, mensagem='Primeira campanha')
session.add(new_campanha)
session.commit()

new_telefone = Telefones(id_campanha=1, numero='3188125480', operadora='OI')
session.add(new_telefone)
session.commit()

new_envio = Envios(id_empresa=1, id_campanha=1, id_modem=1, id_telefone=1)
session.add(new_envio)
session.commit()

new_recebimento = Recebimentos(remetente='3192722676', destinatario='3188125480', mensagem='Hello World')
session.add(new_recebimento)
session.commit()

new_usuario = Usuarios(nome='Marcelo Gomes da Silva',usuario='marcelo',email='celo.gomess@gmail.com',  senha='QualquerSenha', id_empresa=1)
session.add(new_usuario)
session.commit()



