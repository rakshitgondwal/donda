from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
import csv
from datetime import datetime

csv_filename = 'D:/Hackathons/donda/project/employee/2016_2.csv'


def upload_data(self):
    read_csv_to_list(csv_filename) 
    return HttpResponse("Uploaded")

def clear_cache(self,insertion_list,counter):
    Employee.objects.bulk_create(insertion_list)
    counter=0
    insertion_list.clear()
    return insertion_list,counter

def column_cleaning(row,column_list):
    column_dictionary=dict()
    for i in range(len(row)):
        column_dictionary[column_list[i]]=row[i]
        key=column_list[i]
        if (key=='decision_date' or key=='case_submitted' or key=='employment_start_date' or key=='employment_end_date' or key=='original_cert_date'):
            if (column_dictionary[key] == ""):
                column_dictionary[key] = None
            else:
                input_date=datetime.strptime(column_dictionary[key], "%d-%m-%Y")
                output_date_string=input_date.strftime("%Y-%m-%d")
                column_dictionary[key]=output_date_string
        if(key=='prevailing_wage' or key=='wage_rate_of_pay_from' or key=='wage_rate_of_pay_to'):
            if (column_dictionary[key] == ""):
                column_dictionary[key] = None 
            try:
                column_dictionary[key]=float(column_dictionary[key].replace(',',''))
            except:
                continue   
        if(key=='pw_source_year' or key=='total_workers'):
            if (column_dictionary[key] == ""):
                column_dictionary[key] = None
    return column_dictionary

# Define a function to read CSV file and return data as a list of lists
def read_csv_to_list(filename,encoding='latin-1'):
    column_list=list()
    data_to_insert=list()
    with open(filename, 'r',newline='',encoding=encoding) as file:
        flag=0
        count=0
        csv_reader=csv.reader(file)
        for row in csv_reader:

            #The above flag is to store separately the first row obtained from the csv_reader which is the list of columns.
            if(flag==0):
                #the above list of columns with the given titles converted to lowercase to match the models.
                column_list=[i.lower() for i in row]
                column_list[33]='h1b_dependent'
                flag=1
            else:
                print(count)

                #Create a batch of 10000 size and whenever the count value reaches above 10000, it is reset to 0 and the list of instances is cleared.
                if (count > 10000):
                    data_to_insert,count=clear_cache(data_to_insert,count)
                
                #Sending and updating the column dictionary by sending it to a function to adjust the date format and decimal values
                column_dictionary=column_cleaning(row,column_list)

                #Creating the instance of Employee       
                instance=Employee(**column_dictionary)

                #Appending the instances to the list to later do bulk create
                data_to_insert.append(instance)
                count+=1

        Employee.objects.bulk_create(data_to_insert)


