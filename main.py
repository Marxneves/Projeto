from flask import Flask, render_template
from lib import DadosAbertos

app = Flask(__name__)


@app.route("/")
def deputados():
   obj = DadosAbertos()
   list_dep = obj.deputados()
   info = obj.deputado_id(id)
    
   escolaridades = {}  
   cont = 0  

   for dep in list_dep:
        info = obj.deputado_id(dep['id'])
        escolaridade = info['escolaridade']
        if escolaridade in escolaridades:
             escolaridades[escolaridade] += 1
        else:
          escolaridades[escolaridade]  =  1
       # cont += 1
       # if cont == 30:
        #  break  
   print(escolaridades)
   bar_labels=escolaridades.keys()
   bar_values=escolaridades.values()

   return render_template('index.html', max=280, labels=bar_labels, values=bar_values)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)