from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/imc')
def imc():
    args = request.args
    height = args.get('height', 0)
    weight = args.get('weight', 0)

    if height == 0 or weight == 0:
        return jsonify(
            success=False,
            message='You should provide height (cm) and weight (kg) args.'
        ), 400

    imc = float(weight) / ((float(height) / 100) ** 2)

    return jsonify(success=True, data=imc)