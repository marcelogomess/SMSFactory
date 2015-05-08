#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Funcionalidade : Script de automação do Gateway de SMS - GAMMU
# Criadores: Marcelo
# Data: 11/08/2014
# Versão: 2.0

import SimpleHTTPServer
import SocketServer
import cgi
import sys
import urlparse
import re
from Classes.database import DataBase

if len(sys.argv) > 2:
    PORT = int(sys.argv[2])
    I = sys.argv[1]
elif len(sys.argv) > 1:
    PORT = int(sys.argv[1])
    I = ""
else:
    PORT = 8000
    I = ""


class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
## http://192.168.41.165:8000/?NumUsu=CONEKTA&Senha=A4S5D6&SeuNum=00001&Celular=3188125480&Mensagem=%22teste%20do%20webservice%22
    def do_GET(self):
        o = urlparse.urlparse(self.path)
        dados = urlparse.parse_qs(o.query)
        telefone = str(re.sub('[\[\]\']','',str(dados['Celular'])))
        texto =  re.sub('[\[\]\']','',str(dados['Mensagem']))
        newSMS = DataBase()
        newSMS.insereSMSEnvios('1', '1', telefone, texto)


    def do_POST(self):
        postContent = []
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        if "NumUsu" and "Senha" and "SeuNum" and "Celular" and "Mensagem" in form:
            for item in form.list:
                postContent.append(item.value)
            telefone = postContent[3]
            texto = postContent[4]
            newSMS = DataBase()
            newSMS.insereSMSEnvios('1', '1', telefone, texto)

Handler = ServerHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
httpd.serve_forever()
