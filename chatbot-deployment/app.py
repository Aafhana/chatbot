from flask import Flask,render_template,request,jsonify
from chat import get_response
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    #print("Received data:", data)
    
    if data and "message" in data:
        text = data["message"]
        #print("Received message:", text)
        
        response = get_response(text)
        message = {"answer": response}
        #print("bot message",message)
        return jsonify(message)
    else:
        return jsonify({"error": "Invalid request format"}), 400



# @app.post("/predict")
# def predict():
#     j=request.get_json()#input from user
#     #print(j)
#     print(j.get("message"))
#     text=j.get("message")
#     text=str(text)
#     print(text,00)
#     #todo: check if text is valid
#     response=get_response("hello")
#     message={"answer":response}
#     return jsonify(message)#output giving to js 



if __name__=="__main__":
    app.run(debug=True)
    











# @app.get('/')
# def index_get():
#     return render_template("base.html")






# @app.route("/predict", methods=['POST'])
# @app.post("/predict")
# def predict():
#     data = request.get_json()
#     #print(data)
#     # 
#     if 'message' not in data:
#         return jsonify({'error': 'No message provided'}), 400

#     message = data['message']
#     print(message)
#     response = get_response(message)
#     return jsonify({'response': response})

# if __name__ == '__main__':
#     app.run(debug=True)
    
    