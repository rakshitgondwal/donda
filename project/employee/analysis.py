# Postgre SQl queries
from employee.models import Employee
from django.db.models import Avg
from django.db import connection
from django.http import HttpResponse, JsonResponse



def count_records(self):
    queryset = Employee.objects.all()

    total_data_points = queryset.count()
    data = {
        'total_data_points': total_data_points
    }
    return JsonResponse(data)

def find_mean(self):
    # Calculate the average salary excluding empty values
    average_salary = Employee.objects.exclude(prevailing_wage__isnull=True).aggregate(Avg('prevailing_wage'))

    # The result is a dictionary with the average value
    average_salary_value = average_salary['prevailing_wage__avg']

    data = {
        'average_salary_value': average_salary_value
    }
    return JsonResponse(data)

def median(self):
    # Your modified raw SQL query to calculate the median excluding empty values
    query = """
        SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY prevailing_wage) AS median
        FROM employee_Employee
        WHERE prevailing_wage IS NOT NULL;
    """

    # Execute the modified raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    median_salary = result[0] if result else None

    data = {
        'median_salary': median_salary
    }
    return JsonResponse(data)


def percentile_25(self):
    # Your modified raw SQL query to calculate the 25th percentile excluding empty values
    query = f"""
        SELECT percentile_cont(0.25) WITHIN GROUP (ORDER BY prevailing_wage) AS percentile_25
        FROM employee_Employee
        WHERE prevailing_wage IS NOT NULL;
    """

    # Execute the modified raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    percentile_25_salary = result[0] if result else None

    data = {
        'percentile_25_salary': percentile_25_salary
    }
    return JsonResponse(data)

def percentile_75(self):
    # Your modified raw SQL query to calculate the 75th percentile excluding empty values
    query = """
        SELECT percentile_cont(0.75) WITHIN GROUP (ORDER BY prevailing_wage) AS percentile_75
        FROM employee_Employee
        WHERE prevailing_wage IS NOT NULL;
    """

    # Execute the modified raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    percentile_75_salary = result[0] if result else None

    data = {
        'percentile_75_salary': percentile_75_salary
    }
    return JsonResponse(data)
