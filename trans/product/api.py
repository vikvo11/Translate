#Product service
import json
from flask import Flask, render_template, render_template_string, request
from flask_restful import Resource, Api
from googletrans import Translator, constants
from pprint import pprint
app = Flask(__name__)
api = Api(app)

translator = Translator()
#translation1 = translator.translate("Hello World!", dest="ru")
#translation1 = translator.translate("Привет!", dest="en")
try:
    res=translator.translate("Hello World BIG MAN!", dest="ru").text
except Exception as e:
    print(e)

class Product(Resource):
  def get(self):
    d={
      'product': ['Ice cream',
                  'Chocolate',
                  'Fruit1',
                  translation1.text,
                  #str(res.encode('utf8').decode("cp850"))
                  #str(res.decode('utf8').)
                  ]
          }
    return json.loads(json.dumps(d))
api.add_resource(Product,'/api')
test= '''
<html>
   <body>
      <form action = "/" method = "POST">
         <p>Eng <input type = "text" name = "Eng" /></p>
         <p>Rus <input type = "text" name = "Rus" /></p>
         
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>
'''
@app.route("/", methods=['POST','GET'])
def hello():
    if request.method == 'POST':
        transl = translator.translate(str(request.form['Eng']),dest="ru").text
        trans2 = translator.translate(str(request.form['Rus']),dest="en").text
        return render_template_string('{% block body %}'+test+str(transl)+str(trans2)+'{% endblock %}')
    return render_template_string('{% block body %}'+test+res+'{% endblock %}')

if __name__ == '__main__':
    #print(str(res.encode('cp1252', 'ignore')))
    #print (res)
    app.run(host='0.0.0.0', port=80, debug=True)