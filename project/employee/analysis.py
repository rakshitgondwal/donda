# Postgre SQl queries
from employee.models import Employee
from django.db.models import Avg
from django.db import connection
from django.http import HttpResponse, JsonResponse



########### Count Records ##############
def count_records(self):
    # Get a queryset for the model
    queryset = Employee.objects.all()

    # Use the count() method to find the total number of data points
    total_data_points = queryset.count()
    print(total_data_points)
    data = {
        'total_data_points': total_data_points
    }
    return JsonResponse(data)

############# Mean #############
def find_mean(self):
    # Calculate the average salary
    average_salary = Employee.objects.aggregate(Avg('prevailing_wage'))

    # The result is a dictionary with the average value
    average_salary_value = average_salary['prevailing_wage__avg']

    data = {
        'average_salary_value': average_salary_value
    }
    return JsonResponse(data)


############ Median ###########
def median(self):
    # Your raw SQL query to calculate the median
    query = """
        SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY prevailing_wage) AS median
        FROM employee_Employee;
    """

    # Execute the raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    median_salary = result[0] if result else None

    data = {
        'median_salary': median_salary
    }
    return JsonResponse(data)


########### 25 percentile ################
def percentile_25(self):
    # Your raw SQL query to calculate the 25th percentile
    query = f"""
        SELECT percentile_cont(0.25) WITHIN GROUP (ORDER BY prevailing_wage) AS percentile_25
        FROM employee_Employee;
    """

    # Execute the raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    percentile_25_salary = result[0] if result else None

    data = {
        'percentile_25_salary': percentile_25_salary
    }
    return JsonResponse(data)


######## 75 percentile #########
def percentile_75(self):
    # Your raw SQL query to calculate the 25th percentile
    query = """
        SELECT percentile_cont(0.75) WITHIN GROUP (ORDER BY prevailing_wage) AS percentile_75
        FROM employee_Employee;
    """

    # Execute the raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    percentile_75_salary = result[0] if result else None

    data = {
        'percentile_75_salary': percentile_75_salary
    }
    return JsonResponse(data)