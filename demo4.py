from flask import Flask, jsonify, request, make_response, render_template

# Creating an employee list to work with
employees_info = {
    'Roman_Landin':{'status': 'active', 'role':'data engineer', 'age': 34},
    'Jakob_Svensson':{'status': 'active', 'role':'manager', 'age': 35}
    }


app = Flask(__name__)

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

# driver function
if __name__ == '__main__':

    app.run(debug = True)