from flask import Flask, jsonify, request, make_response, render_template

# Creating an employee list to work with
employees_info = {
    'Roman_Landin':{'status': 'active', 'role':'data engineer', 'age': 34},
    'Jakob_Svensson':{'status': 'active', 'role':'manager', 'age': 35}
    }


app = Flask(__name__)

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

# driver function
if __name__ == '__main__':

    app.run(debug = True)