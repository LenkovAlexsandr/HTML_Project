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
    list_pr = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
               'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
               'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
               'киберинженер', 'штурман', 'пилот дронов']
    return render_template('list_prof.html', list=list, list_pr=list_pr)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    dict = {'title': 'Анкета', 'surname': 'Wanty', 'name': 'Mark', 'education': 'выше среднего',
            'profession': 'штурман марсохода', 'sex': 'male',
            'motivation': 'Всегда хотел застрять на Марсе!', 'ready': 'True'}
    return render_template('answer.html', dict=dict)


@app.route('/login')
def login():
    pass


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')

