

#1 - coletar os seguintes dados da maquina:
# hostname,
#  USER,
#  PID,
#  CPU%
#  MEM%
#  COMMAND,
#  date

# Para coletar os dados da maquina,voce  pode usar a biblioteca "os do python que execute "	
import os
from utils import *
import pymongo # USADO PARA SE CONECTAR AO DATA MONGO
from pymongo.server_api import ServerApi 

output = os.popen('ps -aux').read()  # OUTPUT- USADO PARA EXTRAIR OS DADOS DA MAQUINA.
output_list = output.split('\n')     # SPLIT USADO PARA TRANSFORMAR OS TEXTO EM VARIAS  LINHAS 
output_list_cleaned = clean_output_list(output_list) # CLEAN USA PARA DEIXAR OS TEXTOS, MAIS FACEIS DE COMPREENDER ELIMINANDO TEXTO DESNECESARIOS. 

#2 - montar uma string json no seguinte formato:
#"{"hostname" : hostname,
#  "pid": PID,
#  "CPU_usage": %CPU,
#  "MEM_usage": %MEM,
#  "command": COMMAND,
#  "timestamp": date}"

list_dictionaries = output_list_cleaned_2_list_dictionaries(output_list_cleaned)
list_dictionaries_timesstamp = add_timesstramp(list_dictionaries) 

#list_dictionaries - OU SEJA O FORMATO QUE O DJSON IRA INTERPRETAR.
# ADD_TIMESTAMP - O FORMATO QUE O DJSON ADICIONAR/RECONHER A HORA 



# 3 - enviar esses dados ao banco de dados MongoDB Atlas;

# client = pymongo - ONDE SE CONECTAR AO BANCO DE DADOS DO MONGO ATLAS
client = pymongo.MongoClient("mongodb+srv://Walisson_S:walibe2512@cluster0.fegsf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test
for element in list_dictionaries_timesstamp:
    db["perfomaces_test"].insert_one(element)
    # CADA ELEMENT SERA INTREPRETADO POR LSITA DE DICIONARIO E ENCAMINHADO AO BANCO DE DADOS SENDO ASSIM INTERPRETANDO OS CODIGOS. 

db["perfomances_test"].insert_one(list_dictionaries_timesstamp[0])

#import pdb; pdb.set_trace()

# */5 * * * *  python3 /$home/python_tutorial/monitoration.py 
