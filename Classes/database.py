#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import MySQLdb
import time

class DataBase:
    def __init__(self):
        try:
            self.dataBase=MySQLdb.connect("localhost","root","","controlgroup")
            self.cursor = self.dataBase.cursor()
        except:
            print "Erro ao conectar a base de dados."
            
### Tabela empresas
###
###nome VARCHAR 80
###razao_social VARCHAR 80
###cpf_cnpj VARCHAR 80
###

    def insereEmpresa(self,nome,razao_social,cpf_cnpj):
        self.nome = "'"+nome+"'"
        self.razao_social = "'"+razao_social+"'"
        self.cpf_cnpj = "'"+cpf_cnpj+"'"
        self.dataBase.query("""INSERT INTO empresas (nome, razao_social, cpf_cnpj) VALUES (%s,%s,%s) """ % (nome,razao_social,cpf_cnpj))
        self.dataBase.commit()

    
    def pesquisaEmpresa(self):
        return(self)
    
    def atualizaEmpresa(self):
        return(self)            

### Tabela sms_campanhas
###
### id_empresa INT FK
### texto VARCHAR 160
### situacao CHAR 1
### data_campanha TIMESTAMP CURRENT_TIMESTAMP

    def insereSMSCampanhas(self,id_empresa,id_campanha, id_modem, telefone, texto, situacao):
        self.id_empresa = id_empresa
        self.id_campanha = id_campanha
        self.id_modem = id_modem
        self.telefone = "'"+telefone+"'"
        self.texto = "'"+texto+"'"
        self.situacao = "'"+situacao+"'"
        self.dataBase.query("""INSERT INTO sms_envios (id_empresa, id_campanha, id_modem, 
        telefone, texto, situacao) VALUES (%s,%s,%s) """ % (id_empresa, id_campanha, id_modem, telefone, texto, situacao))
        self.dataBase.commit()
        
        

    def pesquisaSMSCampanhas(self):
        return(self)
    
    def atualizaSMSCampanhas(self):
        return(self)
    
### Tabela sms_envios    
###
### id_empresa INT FK
### id_campanha INT FK
### id_modem INT FK
### telefone VARCHAR 15
### texto VARCHAR 170
### situacao CHAR 1
### data_cadastro TIMESTAMP CURRENT_TIMESTAMP
### data_processamento DATETIME
### data_atualizacao DATETIME
### data_envio
###
    
    def insereSMSEnvios(self,idEmpresa,idCampanha, telefone, texto):
        self.idEmpresa = "'"+str(idEmpresa)+"'"
        self.idCampanha = "'"+str(idCampanha)+"'"
        self.telefone = "'"+telefone+"'"
        self.texto = "'"+texto+"'"
        self.dataBase.query("""INSERT INTO sms_envios (id_empresa, id_campanha, telefone, texto) VALUES (%s,%s,%s,%s) """ % (self.idEmpresa, self.idCampanha, self.telefone, self.texto))
        self.dataBase.commit()
     
    def pesquisaSMSEnvios(self,situacao):
        self.situacao = "'"+situacao+"'"
        self.cursor.execute("""SELECT id, telefone, texto FROM sms_envios WHERE situacao = %s""" % (self.situacao))
        return (self.cursor.fetchall())
        
    def pesquisaUmSMSEnvios(self,situacao):
        self.situacao = "'"+situacao+"'"
        self.cursor.execute("""SELECT id, telefone, texto FROM sms_envios WHERE situacao = %s LIMIT 1 """ % (self.situacao))
        return (self.cursor.fetchall())

    def atualizaSituacaoSMSEnvios(self,situacao, idSMS):
        self.situacao = "'"+situacao+"'"
        self.idSMS = "'"+idSMS+"'"
        self.cursor.execute(""" UPDATE sms_envios SET situacao = %s WHERE id = %s""" % (self.situacao,self.idSMS))
        self.dataBase.commit()

    def reservaSMSEnvios(self, listaSMS):
        for oneSMS in listaSMS:
            self.atualizaSituacaoSMSEnvios('R', str(oneSMS[0]))
    
### Tabela sms_modems
### imei_modem VARCHAR 80
### imei_chip VARCHAR 80
### marca VARCHAR 80
### modelo VARCHAR 80
### situacao CHAR 1
### mapeamento VARCHAR 80
### data_registro TIMESTAMP CURRENT_TIMESTAMP
###
    def insereSMSModems(self,imei_modem,imei_chip,marca,modelo,situacao,mapeamento):
        self.imei_modem = "'"+imei_modem+"'"
        self.imei_chip = "'"+imei_chip+"'"
        self.marca = "'"+marca+"'"
        self.modelo = "'"+modelo+"'"
        self.situcacao = "'"+situacao+"'"
        self.mapeamento = "'"+mapeamento+"'"
        self.dataBase.query("""INSERT INTO sms_modems (imei_modem,imei_chip, marca, modelo, situacao, mapeamento) VALUES (%s,%s,%s) """ % (imei_modem,imei_chip,marca,modelo,situacao,mapeamento))
        self.dataBase.commit()
       
    def totalModemsSituacao(self, situacao, servidor):
        self.situacao = "'"+situacao+"'"
        self.servidor = "'"+servidor+"'"
        self.cursor.execute("""SELECT COUNT(id) FROM sms_modems WHERE situacao = %s AND servidor = %s """ % (self.situacao, self.servidor))
        return (self.cursor.fetchall())
        

    def pesquisaSMSModems(self):
        return(self)
    
    def atualizaSMSModems(self):
        return(self)    
    
### Tabela sms_recebimentos
### numero_remetente VARCHAR 15
### numero_destinatario VARCHAR 15
### texto VARCHAR 170
### situacao CHAR 1
### data_recebimento TIMESTAMP CURRENT_TIMESTAMP

    def insereSMSRecebimentos(self):
        return(self)

    def pesquisaSMSRecebimentes(self):
        return(self)

    def atualizaSMSRecebimentos(self):
        return(self)
