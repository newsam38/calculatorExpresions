from Calculator import Calculator


class Application:
    def __init__(self):
        self.calculator = Calculator()

    def run(self):
        while True:
            print("\n Calculator Menu")
            print("1. Generar una expression aleatoria")
            print("2. Introdusca una expresion personalizada")
            print("3. Evaluar la expresion usando la funcion eval()")
            print("4. Evaluar la expresion usando la funcion expr.py")
            print("5. Exit")

            choice = input("Selecciona una opcion de las existentes: ")

            if choice == "1":
                expr = self.calculator.generate_expression()
                print(f"Expresion generada: {expr}")

            elif choice == "2":
                expr = input("Introdusca su expresion (ejemplo, 5 + (3 * 7)): ")
                self.calculator.set_expression(expr)

            elif choice == "3":
                if not self.calculator.expression:
                    print("Expresion a evualar no disponible. Genere una aleatoria o introdusca una empresion "
                          "personalizada.")
                else:
                    result = self.calculator.evaluate_with_evalfunciton()
                    print(f" Resultado de la funcion eval() : {result}")

            elif choice == "4":
                if not self.calculator.expression:
                    print("Expresion a evualar no disponible. Genere una aleatoria o introdusca una empresion "
                          "personalizada.")
                else:
                    result = self.calculator.evaluate_with_exprpyfunciton()
                    print(f"Resultado de la funcion expr.py : {result}")

            elif choice == "5":
                print("Salir de la calculadora")
                break

            else:
                print("Opcion no existente. introduzca una de las opciones de la lista")



if __name__ == "__main__":
    app = Application()
    app.run()