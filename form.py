from flask import Flask, render_template, request

form = Flask(__name__)

@form.route('/')
def root():
    return render_template('form.html')

@form.route('/echo')
def echo():
    return render_template('echo.html', user = request.args['user'])

if __name__ == '__main__':
    form.debug = True
    form.run()
