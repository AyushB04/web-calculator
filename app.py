from flask import Flask, request, jsonify, render_template
import math

app = Flask(__name__)

class AdvancedCalculator:
    def __init__(self):
        self.allowed = {
            "pow": pow,

            # Math functions
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "factorial": math.factorial,

            # Constants
            "pi": math.pi,
            "e": math.e
        }

    def evaluate(self, expression):
        return eval(expression, {"__builtins__": {}}, self.allowed)


calc = AdvancedCalculator()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        expr = request.json["expression"]
        result = calc.evaluate(expr)
        return jsonify(result=result)
    except Exception as e:
        return jsonify(error=str(e)), 400


if __name__ == "__main__":
    app.run(debug=True)