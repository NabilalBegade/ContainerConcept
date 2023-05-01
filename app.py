from flask import Flask, request, render_template


app = Flask(__name__)
print("hello1")

# Home page
@app.route('/')
def home():
    print("hello")
    return render_template('./index.html')


# Vaccination status page
@app.route('/vaccination_status', methods=['POST'])
def vaccination_status():
    # Get the registration number entered by the user
    reg_no = request.form['reg_no']
    print("hello")
    # Send a request to the database container to get the vaccination status of the student
    response = requests.get('http://database:5001/vaccination_status', params={'reg_no': reg_no})

    # Display the vaccination status of the student
    if response.status_code == 200:
        return render_template('vaccination_status.html', reg_no=reg_no, status=response.text)
    else:
        return 'Error: Could not retrieve vaccination status.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
#File "/usr/local/lib/python3.8/site-packages/flask/templating.py", line 95, in _get_source_fast