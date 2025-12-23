from flask import Flask
from flask_cors import CORS
from test.response import defult_response


app = Flask(__name__)
CORS(app,resources={r"/*": {"origins": "*"}}, supports_credentials=True)


@app.route('/', methods=['GET'])
def hello_world():
    data = defult_response()
    return data


if __name__ == '__main__':
    app.run()
