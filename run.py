# run.py

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    if request.method == 'POST':
        valor_auto = float(request.form['valor_auto'])
        monto_cuota_12 = calcular_monto_cuota(valor_auto, 12)
        monto_cuota_24 = calcular_monto_cuota(valor_auto, 24)
        monto_cuota_36 = calcular_monto_cuota(valor_auto, 36)
        entrega_inicial = calcular_entrega_inicial(valor_auto)
        return render_template('resultado.html', valor_auto=valor_auto, entrega_inicial=entrega_inicial, monto_cuota_12=monto_cuota_12, monto_cuota_24=monto_cuota_24, monto_cuota_36=monto_cuota_36)
    else:
        return render_template('resultado.html')

def calcular_monto_cuota(valor_auto, cuotas):
    # Aquí implementa la lógica para calcular el monto de la cuota
    # Puedes usar fórmulas financieras o cualquier otra lógica que prefieras
    # En este ejemplo, simplemente se devuelve el valor del auto dividido por el número de cuotas
    return valor_auto / cuotas

def calcular_entrega_inicial(valor_auto):
    # Aquí implementa la lógica para calcular la entrega inicial
    # Por ejemplo, puede ser un porcentaje del valor del auto
    # En este ejemplo, simplemente se devuelve el 20% del valor del auto
    return valor_auto * 0.2

if __name__ == '__main__':
    app.run(debug=True)
