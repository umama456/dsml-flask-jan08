from flask import Flask
import pickle 

app= Flask(__name__) 

print(__name__) 


with open('classifier.pkl', 'rb') as f :
    clf= pickle.load(f) 

#classifier is a random forest model
    

@app.route('/ping', methods=['GET'])
def ping():
    return "Pinging Model Application!!"

#flask --app app.py run

#gender, married, credit history, applicant income, loan amount.

@app.route('/predict', methods=['POST','GET'])
def predict():
     loan_req=request.get_json()

     if loan_req['gender']=='Male' :
         gender=0
     else:
         gender=1
     if loan_req['married']== "Unmarried" :
         marital_status=0
     else:
         marital_status=1
     if loan_req['credit_history']== "Unclear Debts" :
         credit_history=0
     else:
         credit_history=1

     applicant_income = loan_req['applicant_income'] 
     loan_amount=loan_req['loan_amount']

     result=clf.predict([[gender,marital_status,credit_history,applicant_income,loan_amount]])

     if result==0:
        pred= 'Rejected'
     else:
         pred='Approved'
     return{'loan_approval_status': pred}


@app.route("/template", methods = ['GET'])
def get_template():
    return {
	"gender": "Male/Female",
	"married": "Married/Unmarriefd",
	"applicant_income": "<Numeric Salary>",
	"loan_amount": "Numeric loan amount",
	"credit_history": "Cleared Debts / Uncleared Debts"}
         
