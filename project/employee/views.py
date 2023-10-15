from django.shortcuts import render
from .models import Employee

import csv
from datetime import datetime

# Define a function to read CSV file and return data as a list of lists
def read_csv_to_list(filename,encoding='latin-1'):
    data_dictionary = dict()
    column_list=list()
    with open(filename, 'r',newline='',encoding=encoding) as file:
        flag=0
        row_number=0
        csv_reader=csv.reader(file)
        for row in csv_reader:
            if(flag==0):
                #print(row)
                column_list=[i.lower() for i in row]
                print(len(column_list))
                print(column_list)
            else:
                column_dictionary=dict()
                # print(len(fields))
                # print(fields)
                # print(fields[8])
#                print(fields[9])
                for i in range(len(row)):
                    column_dictionary[column_list[i]]=row[i]
                data_dictionary[row_number]=column_dictionary
                row_number=row_number+1
            flag=1
    for keys in data_dictionary:
        print(keys)
        for key in data_dictionary[keys]:
            if (key=='decision_date' or key=='case_submitted' or key=='employment_start_date' or key=='employment_end_date' or key=='original_cert_date'):
                try:
                    input_date=datetime.strptime(data_dictionary[keys][key], "%d/%m/%y")
                    print('reached the above keys')
                    output_date_string=input_date.strftime("%Y-%m-%d")
                    data_dictionary[keys][key]=output_date_string
                except:
                    continue
        # if(keys=='full_time_pos')
        

    return data_dictionary

# Replace 'your_file.csv' with the actual path to your CSV file
csv_filename = './2016_2.csv'

# Call the function to read the CSV and store the data as a list of lists
data = read_csv_to_list(csv_filename)


def upload_data(self):
    data = {'case_number': 'I-200-13053-847481', 'case_status': 'DONDA', 'case_submitted': '2013-02-25', 'decision_date': '2016-01-13', 'visa_class': 'H-1B', 'employment_start_date': '2013-08-24', 'employment_end_date': '2016-08-23', 'employer_name': 'GOODMAN NETWORKS, INC.', 'employer_address': '6400 INTERNATIONAL PARKWAY, SUITE 1000', 'employer_city': 'PLANO', 'employer_state': 'TX', 'employer_postal_code': '75093', 'employer_country': 'UNITED STATES OF AMERICA', 'employer_province': '', 'employer_phone': '9724215173', 'employer_phone_ext': '', 'agent_attorney_name': 'HULME, RANDALL', 'agent_attorney_city': 'ADDISON', 'agent_attorney_state': 'TX', 'job_title': 'CHIEF OPERATING OFFICER', 'soc_code': '11-1011', 'soc_name': 'CHIEF EXECUTIVES', 'naic_code': '238210', 'total_workers': '1', 'full_time_position': False, 'prevailing_wage': 242674.00, 'pw_unit_of_pay': 'Year', 'pw_wage_source': 'OES', 'pw_source_year': '2012', 'pw_source_other': 'OFLC ONLINE DATA CENTER', 'wage_rate_of_pay_from': 400000.0, 'wage_rate_of_pay_to': '0.00', 'wage_unit_of_pay': 'Year', 'h1b_dependent': 'N', 'willful_violator': 'N', 'worksite_city': 'PLANO', 'worksite_county': 'COLLIN', 'worksite_state': 'TX', 'worksite_postal_code': '75093', 'original_cert_date':'2013-03-01'}
    instance = Employee(**data)
    instance.save()
    return HttpResponse("Uploaded")