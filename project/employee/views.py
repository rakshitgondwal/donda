from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
import csv
from datetime import datetime

csv_filename = 'D:/Hackathons/donda/project/employee/2016_2.csv'


def upload_data(self):
    read_csv_to_list(csv_filename) 
    return HttpResponse("Uploaded")

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
                column_list=[i.lower() for i in row]
                column_list[33]='h1b_dependent'
            else:
                column_dictionary=dict()
                for i in range(len(row)):
                    column_dictionary[column_list[i]]=row[i]
                    key=column_list[i]
                    print(key)
                    if (key=='decision_date' or key=='case_submitted' or key=='employment_start_date' or key=='employment_end_date' or key=='original_cert_date'):
                        if (column_dictionary[key] == ""):
                            column_dictionary[key] = None
                        else:
                            input_date=datetime.strptime(column_dictionary[key], "%d-%m-%Y")
                            output_date_string=input_date.strftime("%Y-%m-%d")
                            column_dictionary[key]=output_date_string
                            print("date formated")
                    if(key=='prevailing_wage' or key=='wage_rate_of_pay_from' or key=='wage_rate_of_pay_to'):
                        try:
                            column_dictionary[key]=float(column_dictionary[key].replace(',',''))
                        except:
                            continue   
                    print(column_dictionary)                                         
                instance=Employee(**column_dictionary)  
                instance.save()
            flag=1
