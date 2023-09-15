from google.cloud import storage
from flask import jsonify, make_response
import json

def get_active_employee_list(request):
    # Set your GCS bucket and file name
    bucket_name = 'roman_landin_demo_employees'
    file_name = 'employees.txt'

    # Initialize a GCS client
    storage_client = storage.Client()

    # Get the bucket and file
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Download the file's content as a string
    file_content = blob.download_as_text()

    # Parse the JSON data into a Python dictionary
    try:
        employees_dict = json.loads(file_content)
    except json.JSONDecodeError as e:
        return f"Error parsing JSON: {str(e)}"

    try:
        active_employees = {}
        for name, info in employees_dict.items():
            if info['status'] == 'active':
                active_employees[name] = info

        return make_response(jsonify({'Active employees': list(active_employees.keys())}), 200)
    except Exception as e:
        print(f'Error in get_employee_list - {e}')
        return make_response(jsonify({'message': 'Invalid request'}), 400)

