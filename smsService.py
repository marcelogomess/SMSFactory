#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Funcionalidade : Script de automação do Gateway de SMS - GAMMU
# Criadores: Marcelo 
# Data: 15/01/2014
# Versão: 2.0

import time
from Classes.SMS import SMS
from Classes.database import DataBase


while True:
    time.sleep(1)
    listaSMS = []
    try:
        newSMSSpool = DataBase()
        totalChip = int(newSMSSpool.totalModemsSituacao('A', 'pegasus')[0][0])
        chipID = 0
        # ###Levanta lista de arquivos pendetes
        listaSMS = newSMSSpool.pesquisaUmSMSEnvios('P')
        newSMSSpool.reservaSMSEnvios(listaSMS)
    except:
        "Erro ao conectar ao banco de dados."
    if listaSMS != []:
        #### Envia SMS a partir dos arquivos
        for oneSMS in listaSMS:
            if oneSMS != []:
                if chipID >= totalChip:
                    chipID = 0
                idSMS = oneSMS[0]
                telefone = oneSMS[1]
                mensagem = oneSMS[2]
                newSMS = SMS(telefone, mensagem)
                try:
                    newSMS.sendSMS(chipID)
                    newSMSSpool.atualizaSituacaoSMSEnvios('E', str(idSMS))
                    chipID = chipID + 1
                except:
                    if chipID >= totalChip:
                        chipID = 0
                    else:
                        chipID = chipID + 1
                    try:
                        newSMS.sendSMS(chipID)
                        newSMSSpool.atualizaSituacaoSMSEnvios('E', str(idSMS))
                    except:
                        newSMSSpool.atualizaSituacaoSMSEnvios('F', str(idSMS))
                        chipID = chipID + 1
