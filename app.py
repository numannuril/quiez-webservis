from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/bmi', methods=['POST'])
def bmi():
    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))
    bmi = weight / (height/100)**2
    msg = "BMI anda " + str(bmi)
    if bmi <= 18.5 :
        ket = " kurus "
    elif bmi <= 25 :
        ket = " normal"
    elif bmi <= 40 :
        ket = "berlebih"
    else :
        ket = "berbahaya"
    data = {'result': 'true', 'msg': msg, 'ket':ket}
    return jsonify(data)



if __name__ == "__main__":
    app.run(port=1500, debug=True) 
   



