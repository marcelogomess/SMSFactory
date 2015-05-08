#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Funcionalidade : Script de automação do Gateway de SMS - GAMMU
# Criadores: Marcelo
# Data: 11/08/2014
# Versão: 2.0


import time
import os
from Classes.SMS import SMS
from Classes.dbSMS import DBSMS
from Classes.readTXTFile import ReadTXTFile

toSendDir = '/opt/SMSFactory/toSend'

while True:
    time.sleep(600)
    qtdChip = 3
    fileSpool = ReadTXTFile(toSendDir)
    if fileSpool.getFileList() == []:
        for chipID in range(0,qtdChip):
                newSMS = SMS('23423423423','dfsfdgsdfgsdfgsd')
                try:
                    qtdSMS = int(newSMS.getSMSStatus(chipID)['SIMUsed'])
                    print qtdSMS
                except:
                    print "Erro ao receber o status do modem."
                    qtdSMS = 0
                if qtdSMS > 0:
                   try:
                       sms = newSMS.readSMS(chipID)
                       smsData =  sms[0]
                       dataRecebimento =  smsData['SMSCDateTime']
                       numeroEnviou = smsData['Number']
                       numeroRecebeu = smsData['SMSC']['Number']
                       mensagem = smsData['Text']
                       location = smsData['Location']
                       newDBSMS = DBSMS()
                       newDBSMS.insertReadSMS(dataRecebimento,numeroEnviou,numeroRecebeu,mensagem)
                       newSMS.deleteSMS(chipID,location)
                   except:
                       print "Nao foi possivel ler o SMS."

