import random

from expr import evaluate as expr_evaluate


class Calculator:
    def __init__(self):
        self.expression = ""

    # genera una expresion aleatorea
    def generate_expression(self):
        operadores = ['+', '-', '*', '/', '**', '%']
        operando1 = random.randint(1, 100)
        operando2 = random.randint(1, 100)
        operador = random.choice(operadores)
        self.expression = f"{operando1} {operador} {operando2}"
        return self.expression

    #Asigna una expresion a la calculadora
    def set_expression(self, expression):
        self.expression = expression

    #funcion encargada de usar la funcion eval que ejecuta la expresion
    def evaluate_with_evalfunciton(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error triggered from the evalfunction(): {e}"

    #funcion encargada de usar la fuincion expr.py cuya libreria es instalada
    # para instalarla ejecuta el comando:
    #pip install git+https://github.com/jay3332/expr.py.git
    def evaluate_with_exprpyfunciton(self):
        try:
            result = expr_evaluate(self.expression)
            return result
        except Exception as e:
            return f"Error triggered from the expr.py library: {e}"
