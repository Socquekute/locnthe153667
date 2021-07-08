  
from flask import Flask, jsonify
from flask_restful import  Api, Resource
import json
import sql

class API(Resource):
    def post(self):
        with open("API.json", encoding="utf-8") as f:
            data= json.load(f)
        dumps= json.dumps(data)
        y= json.loads(dumps)
        for i in range(data):
            sql.add_question(y[i])

    def get(self):
        num = sql.answer()  
        data=[]
        for r in num:
            data.append({"Number": r[0], "Answer": r[1]})
        
        return jsonify({"response": data})

app = Flask(__name__)
api = Api(app)
api.add_resource(API,"/body")
if __name__ == '__main__':
    app.run(debug=True)

