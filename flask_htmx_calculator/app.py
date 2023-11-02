from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    first = request.form.get('firstNumber', type=float)
    second = request.form.get('secondNumber', type=float)
    operation = request.form.get('operation')

    if first is None or second is None or operation is None:
        abort(400, 'Invalid input')

    if operation == 'add':
        result = first + second
    elif operation == 'sub':
        result = first - second
    elif operation == 'mul':
        result = first * second
    elif operation == 'div':
        if second != 0:
            result = first / second
        else:
            abort(400, 'Cannot divide by zero')
    else:
        abort(400, 'Invalid operation')

    return f'{result:.2f}'

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
