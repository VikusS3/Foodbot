from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from chat import get_response


app = Flask(__name__)
CORS(app)  # para que no haya problemas con el cors

##antihuo metodo para que el bot responda
# @app.route("/", methods=["GET"])
# @app.get("/")
# def index_get():
#     return render_template('base.html')


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)