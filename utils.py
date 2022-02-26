# NICE TOOLS THAT WE CAN USE 
import datetime  #

def clean_row(row):
    # clean_row 
    cleaned_information_step_1 =[] 
    for element in row:
       if element != '':
            cleaned_information_step_1.append(element)
    cleaned_information_step_2 = []
    iterator = 0
    string_command = ''
    for element in cleaned_information_step_1:
        if iterator > 9:
            string_command +=  element + ' '
        else: 
            cleaned_information_step_2.append(element)
        iterator += 1

    string_command = string_command[:-1]
    cleaned_information_step_2.append(string_command)  
    return cleaned_information_step_2

    # clean  output list
def clean_output_list (output_list):
    output_list_cleaned = []
    for row in output_list:
        row_splitted = row.split(' ')
        cleaned_row = clean_row(row_splitted)
        if cleaned_row != ['']:
             output_list_cleaned.append(cleaned_row)
    output_list_cleaned = output_list_cleaned[1:]
    return output_list_cleaned


     # Transform row in dictionary 
def row_2_dic(row):
    HOSTNAME_slot = 0
    USER_slot = 1
    PID_slot = 2
    CPU_slot = 3
    MEM_slot = 4
    COMMAND_slot = 10
    dict_row = {}
    for iterator in range( len(row) ):
        if iterator == HOSTNAME_slot:
            dict_row['walisson-soares'] = row[iterator]
        if iterator == USER_slot:
            dict_row['user'] = row[iterator]
        elif iterator == PID_slot: 
            dict_row['pid'] = row[iterator]
        elif iterator == CPU_slot: 
            dict_row['CPU_USAGE'] = row[iterator]
        elif iterator == MEM_slot: 
             dict_row['MEM_USAGE'] = row[iterator]        
        elif iterator == COMMAND_slot: 
             dict_row['commmand'] = row[iterator]
    return dict_row

# Transform output list cleaned to list of dictionaries 
def output_list_cleaned_2_list_dictionaries(output_list_cleaned):
    list_dictionaries = []
    for row in output_list_cleaned:
        list_dictionaries.append( row_2_dic(row) )
    return(list_dictionaries)

# add timesstamp in dictionaries 
def add_timesstramp(list_dictionaries):
    list_dictionaries_timesstamp = []
    for element in list_dictionaries:
        timestamp = str(datetime.datetime.now())
        element['timestamp'] = timestamp
        list_dictionaries_timesstamp.append(element)
    return list_dictionaries_timesstamp