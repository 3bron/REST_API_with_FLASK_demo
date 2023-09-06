from flask import Flask, jsonify, request, make_response, render_template

# Creating an employee list to work with
employees_info = {
    'Roman_Landin':{'status': 'active', 'role':'data engineer', 'age': 34},
    'Jakob_Svensson':{'status': 'active', 'role':'manager', 'age': 35}
    }


app = Flask(__name__)


# Redirect to a home page
@app.route('/home')
def home():
    return render_template('html/home.html', employees=employees_info)
        

# driver function
if __name__ == '__main__':

    app.run(debug = True)