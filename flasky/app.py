from flask import Flask

from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/adder/<int:a>/<int:b>')
class HelloWorld(Resource):
    def get(self, a, b):
        return {'calc': a + b}


if __name__ == '__main__':
    app.run(debug=True)