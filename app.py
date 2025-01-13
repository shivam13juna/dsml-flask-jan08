from flask import Flask, request, jsonify # from flask (library) import Flask (class)
import pickle

pancakes = Flask(__name__) # Flas(__name__) is the name of the application's module or package

print(__name__)

with open('new_classifier.pkl', 'rb') as f:
    clf = pickle.load(f)

# classifier is a random forest model

@pancakes.route('/ping', methods=['GET'])
def ping():
    return {'message': 'Pinging Model Application!!'}



@pancakes.route('/predict', methods=['POST', 'GET'])
def test_predict():
    loan_req = request.get_json()
    
    # Convert the input data to a 2D array
    #input_data = [[
    #    test_data['gender'],
    #    test_data['married'],
    #    test_data['applicant_income'],
    #    test_data['loan_amount'],
    #    test_data['credit_history']
    #]]

    if loan_req['gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['married'] == "Unmarried":
        Married = 0
    else:
        Married = 1

    if loan_req['credit_history'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['applicant_income']
    LoanAmount = loan_req['loan_amount'] / 1000

    # Making predictions
    prediction = clf.predict(
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
    
    # Assuming clf is a scikit-learn model and input_data is preprocessed correctly
    
    # Convert prediction to a human-readable format
    loan_approval_status = "Approved" if prediction[0] == 1 else "Rejected"
    #assert response.status_code == 200
    #assert response.json == {'loan_approval_status': "Rejected"}
    return jsonify({'loan_approval_status': loan_approval_status})



def sum_something(a, b):
    return a + b

def sub_something(a, b):
    return a - b

def mul_something(a, b):
    return a * b
# pytest, in pytest unit is a function that you can test independently























# def do_sth():
#     return 'Pinging sfsdfsd Model Application!!'

# flask --pancakes pancakes.py run

# http://127.0.0.1:5000/ping

# gender, married, credit_history, applicant_income, loan_amount. 

@pancakes.route('/predict', methods = ['POST', 'GET'])
def predict():
    """
    Returns the loan approved or not
    """
    # {'criminal': True}

    loan_req = request.get_json()

    if loan_req['gender'] =='Male':
        gender = 0
    else:
        gender = 1
    
    if loan_req['married'] =='Unmarried':
        marital_status = 0
    else:
        marital_status = 1

    if loan_req['credit_history'] =='Unclear Debts':
        credit_history = 0
    else:
        credit_history = 1

    applicant_income = loan_req['applicant_income']
    loan_amount = loan_req['loan_amount']

    result = clf.predict([[gender, marital_status, credit_history, applicant_income, loan_amount]])

    if result == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'

    return {"loan_approval_status": pred}

@pancakes.route("/template", methods = ['GET'])
def get_template():
    return {
	"gender": "Male/Female",
	"married": "Married/Unmarriefd",
	"applicant_income": "<Numeric Salary>",
	"loan_amount": "Numeric loan amount",
	"credit_history": "Cleared Debts / Uncleared Debts"}





# {
# 	"gender": "Male",
# 	"married": "Married",
# 	"applicant_income": "10",
# 	"loan_amount": "10000000",
# 	"credit_history": "Cleared Debts"
#     }

# pip install pipreqs


# For running on docker
# docker built -t ano .
"""
1. Build the image by running the following command from the project root directory:
    docker build -t ano .



2. Run the Docker container using the command shown below:
    docker run -d -p 5000:5000 loan-prediction-pancakes # Here first 5000 is the port number of the host machine and second 5000 is the port number of the container.

3. To push a docker image named "ano" to docker hub, run the following command:
    docker tag loan-prediction-pancakes:latest ano/loan-prediction-pancakes:latest
    docker push ano/loan-prediction-pancakes:latest

"""


# docker build -t image_jan .

# docker image ls

# docker tag image_jan shivam13juna/mlops-jan10:latest