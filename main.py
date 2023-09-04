from flask import Flask, jsonify, request, make_response, render_template

########## Use following end URLs for this REST API demo ###########
"""
curl -X GET http://127.0.0.1:5000/api_information
curl -X GET http://127.0.0.1:5000/active_employees
curl -X POST -H "Content-Type: application/json" -d '{"name": "Lisa_Kyhlberg", "status":"active", "role":"data engineer", "age": 28}' http://127.0.0.1:5000/add_employee
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Lisa_Kyhlberg", "status":"inactive"}' http://127.0.0.1:5000/update_employee_status
"""

# Creating an employee list to work with
employees_info = {
    'Roman_Landin':{'status': 'active', 'role':'data engineer', 'age': 34},
    'Jakob_Svensson':{'status': 'active', 'role':'manager', 'age': 35}
    }

# creating the flask app
app = Flask(__name__)

# Redirect to a home page
@app.route('/')
def home():
    return render_template('html/home.html')

# GET request to retrieve API information
@app.route('/api_information', methods=['GET'])
def api_information():
    return make_response(jsonify({'message': 'This REST API is used as a demonstration of Flask capabilities'}), 200)

# GET request to retrieve names of all active employees
@app.route('/active_employees', methods=['GET'])
def get_employee_list():
    try:
        active_employees = {}
        for name, info in employees_info.items():
            if info['status'] == 'active':
                active_employees[name] = info

        return make_response(jsonify({'The name list of all employees': list(active_employees.keys())}), 200)
    except Exception as e:
        print(f'Error in get_employee_list - {e}')
        return make_response(jsonify({'message': 'Invalid request'}), 400)

# POST request to add information about a new employee
@app.route('/add_employee', methods=['POST'])
def add_employee():
    information = request.get_json()
    if not information:
        return make_response(jsonify({'message': 'Invalid employee data'}), 400)
    else:
        try:
            employees_info[information['name']] = {'status': information['status'], 'role': information['role'], 'age': information['age']}
            return make_response(jsonify({'message': 'Succesfully recorded a new employee'}), 200)
        except Exception as e:
            print(f'Error in add_employee - {e}')
            return make_response(jsonify({'message': 'Invalid employees information. Provide information in the right format'}), 400)

# PUT request to update information for an existing employee
@app.route('/update_employee_status', methods=['PUT'])
def update_employee():
    information = request.get_json()
    if not information:
        return make_response(jsonify({'message': 'Invalid employee data'}), 400)
    else:
        try:
            employees_info[information['name']]['status'] = information['status']
            return make_response(jsonify({'message': 'Succesfully updated an employees information'}), 200)
        except Exception as e:
            print(f'Error in update_employee - {e}')
            return make_response(jsonify({'message': 'Invalid employees information. Provide information in the right format'}), 400)
  

# driver function
if __name__ == '__main__':
  
    app.run(debug = True)





