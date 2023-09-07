from flask import Flask, jsonify, request, make_response, render_template


app = Flask(__name__)

@app.route('/api_information', methods=['GET'])
def api_information():
    return make_response(jsonify({'message': 'This REST API is used as a demonstration'}), 200)

# driver function
if __name__ == '__main__':

    app.run(debug = True)