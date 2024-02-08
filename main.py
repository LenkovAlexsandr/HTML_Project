from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    if list not in ['ol', 'ul']:
        return 'Error'
    list_pr = ['a', 'b', 'c', 'd']
    return render_template('list_prof.html', list=list, list_pr=list_pr)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')

