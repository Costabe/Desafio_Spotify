# DESAFIO PYTHON  Spotify 

#import json 
#json.load
#import os
#output = os.popen('ps -aux').read()
#print("output")

#1 - coletar os seguintes dados da maquina:
# hostname, USER, PID, CPU% MEM% COMMAND, date

# date '+%d-%m-%Y'
# ps -aux | awk '{print $1,$2,$3,$4,$11}' | sed -e 's/\s/,/g' 
# ps -aux | awk '{print $1,$2,$3,$4,$11}' | sed -e 's/\s/,/g' > $HOME' '$(date '+%d-%m-%Y' > output.csv)
	
#2 - montar uma string json no seguinte formato:
#"{"hostname" : hostname, "pid": PID, "CPU_usage": %CPU, "MEM_usage": %MEM, "command": COMMAND, "timestamp": date}"


# python library
import os
output = os.popen('ps -aux').read()
#print("output")
print( type(output) )
output_list = output.split('\n')

fisrt_row = output_list[1].split('')
cleaned_information =[] 

# Precisamos de fazer isso para os 10 primeiros 
for iterator in range (10):
    if fisrt_row[iterator] != '':
        cleaned_information.append(fisrt_row[iterator])

for element in fisrt_row:
    if element != '':
        cleaned_information.append(element)
import pdb; pdb.set_trace()   

# open json file 1

# how to create a json file
# reference: https://www.kite.com/python/answers/how-to-create-a-json-object-in-python


print('hostname, USER, PID, CPU% MEM% COMMAND, date')
my_json_person = { "hostname" : "USER", "pid": "CPU_usage": %CPU, "MEM_usage": %MEM, "command": COMMAND, "timestamp": "date", DATE"}
print(my_json_person)
print(type(my_json_person))
my_json_person_dump = json.dumps(my_json_person)
print(my_json_person_dump)
print(type(my_json_person_dump))


# how to save a json file
# reference: https://stackabuse.com/saving-text-json-and-csv-to-a-file-in-python/
file_json_my_json_person = open('my_json_person.json', 'w')
file_json_my_json_person.write(my_json_person_dump)
file_json_my_json_person.close()

# 
# 3 - enviar esses dados ao banco de dados MongoDB Atlas;

#EDITOR="gedit" crontab -e

# */5 * * * * $HOME/spotify.sh

#alisson    1909  0.0  0.0  16376  9984 ?        Ss   22:15   0:00 /lib/systemd/systemd --use
