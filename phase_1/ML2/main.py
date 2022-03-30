from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
with open("pipeline.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/") # homepage (get)
def model_prediction():
    Education = eval(request.args.get('Education'))
    JoiningYear = eval(request.args.get('JoiningYear'))
    City = eval(request.args.get('City'))
    PaymentTier = eval(request.args.get('PaymentTier'))
    Age = eval(request.args.get('Age'))
    Gender = eval(request.args.get('Gender'))
    EverBenched = eval(request.args.get('EverBenched'))
    ExperienceInCurrentDomain = eval(request.args.get('ExperienceInCurrentDomain'))
    new_data = [Education, JoiningYear, City, PaymentTier, Age, Gender, EverBenched, ExperienceInCurrentDomain ]
    res = model.predict([new_data])
    classes = ['Bertahan', 'Resign']
    response = {'status':'success',
            'code':200,
            'data':{'result':classes[res[0]]}
            }
    return jsonify(response)

app.run(debug=True)

