# REST_API_with_FLASK_demo
Introduction to how to build a simple REST API using Flask library in python

#### HOME PAGE IN YOUR BROWSER
http://127.0.0.1:5000/home

#### CURL API REQUESTS ####
Call your locally deployed APIs in terminal with CURL

# GET API_information
curl -X GET http://127.0.0.1:5000/api_information

# GET ACTIVE EMPLOYEES
curl -X GET http://127.0.0.1:5000/active_employees

# CREATE A NEW EMPLOYEE
curl -X POST -H "Content-Type: application/json" -d '{"name": "Lisa_Kyhlberg", "status":"active", "role":"data engineer", "age": 28}' http://127.0.0.1:5000/add_employee

# UPDATE AN EXISTING EMPLOYEE
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Roman_Landin", "status":"inactive"}' http://127.0.0.1:5000/update_employee_status