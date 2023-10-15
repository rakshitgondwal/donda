# Postgre SQl queries
from employee.models import Employee
from django.db.models import Avg
from django.db import connection


########### Count Records ##############
def count_records():
    # Get a queryset for the model
    queryset = Employee.objects.all()

    # Use the count() method to find the total number of data points
    total_data_points = queryset.count()
    return total_data_points

############# Mean #############
def find_mean():
    # Calculate the average salary
    average_salary = Employee.objects.aggregate(Avg('salary'))

    # The result is a dictionary with the average value
    average_salary_value = average_salary['salary__avg']

    return average_salary_value


############ Median ###########
def median():
    # Your raw SQL query to calculate the median
    query = """
        SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY salary) AS median
        FROM employee_Employee;
    """

    # Execute the raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    median_salary = result[0] if result else None

    return median_salary


########### 25 percentile ################
def percentile_25():
    # Your raw SQL query to calculate the 25th percentile
    query = """
        SELECT percentile_cont(0.25) WITHIN GROUP (ORDER BY salary) AS percentile_25
        FROM employee_Employee;
    """

    # Execute the raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    percentile_25_salary = result[0] if result else None

    return percentile_25_salary


######## 75 percentile #########
def percentile_75():
    # Your raw SQL query to calculate the 25th percentile
    query = """
        SELECT percentile_cont(0.75) WITHIN GROUP (ORDER BY salary) AS percentile_75
        FROM employee_Employee;
    """

    # Execute the raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    percentile_75_salary = result[0] if result else None

    return percentile_75_salary
