#Product service
from flask import Flask
from flask_restful import Resource, Api
from googletrans import Translator, constants
from pprint import pprint
app = Flask(__name__)
api = Api(app)

translator = Translator()
translation = translator.translate("Hola Mundo")

class Product(Resource):
  def get(self):
    return{
      'product': ['Ice cream',
                  'Chocolate',
                  'Fruit1',
                  translation.text]
          }
api.add_resource(Product,'/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)