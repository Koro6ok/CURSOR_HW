from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def info():
    return render_template('info.html')


@app.route('/calc/<int:x>/<int:y>/<string:operation>')
def calculation(x,y,operation):

    if operation == 'div':
        if y==0:
            return render_template('calc.html', result="WRONG OPERATION! Division by zero!")
        else:
            return render_template('calc.html', x=x, y=y, operation="/", result=x/y)
    elif operation == 'sum':
        return render_template('calc.html', x=x, y=y, operation="+", result=x+y)
    elif operation == 'dif':
        return render_template('calc.html', x=x, y=y, operation="-", result=x-y)
    elif operation == 'mult':
        return render_template('calc.html', x=x, y=y, operation="*", result=x*y)
    else:
        return "Shit happens"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')