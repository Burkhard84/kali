# O módulo de soquete em Python é uma interface para a API de soquetes Berkeley.
import socket
# Importamos o módulo ipaddress. Queremos usar o ipaddress.ip_address (endereço)
# método para ver se podemos instanciar um endereço IP válido para testar.
import ipaddress
# Precisamos criar expressões regulares para garantir que a entrada esteja formatada corretamente.
import re

# Padrão de expressão regular para extrair o número de portas que você deseja verificar.
# Você deve especificar <lowest_port_number> - <highest_port_number> (ex 10-100)
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Inicializando os números das portas, usaremos as variáveis mais tarde.
port_min = 0
port_max = 65535

# Este script usa a API de soquete para ver se você pode se conectar a uma porta em um endereço IP especificado.
# Depois de conectar com sucesso, uma porta é vista como aberta.
# Este script não discrimina a diferença entre portas filtradas e fechadas.

# Cabeçalho básico da interface do usuário

print(r"""********************************************************************************************                                             
                                  _           _     
                        __      _| |__   ___ (_)___ 
                        \ \ /\ / / '_ \ / _ \| / __|
                         \ V  V /| | | | (_) | \__ \
                          \_/\_/ |_| |_|\___/|_|___/
                                   
                            Como fazer uma consulta
                            
                  Domínios: digite o nome completo do domínio:
               minhaempresa.com.br ou meunome.meusobrenome.nom.br. 
            Verifique as regras sintáticas para nomes de domínio em Dicas 
                     e regras para o registro de um domínio. 
                  
    IP ou bloco CIDR: digite um número IP (200.200.200.200) ou um bloco CIDR (200.200/16).
                                                                               
                             Abrir o programa : python3 whois.py                                                  
                             Exemplo de uso: Digite Domínio ou IP: google.com.br                             
                             Exemplo de uso: Digite Domínio ou IP: 127.0.0.1                        """)
print("\n*********************************************************************************************")

import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('200.160.2.3', 43))
url = input("                             Digite Domínio ou IP: ")
s.send((url + "\r\n").encode())
resposta = b''
while True:
    recebe = s.recv(1024)
    resposta += recebe
    if not recebe:
        break
s.close()
print(resposta.decode('iso-8859-1'))
time.sleep(9999)

