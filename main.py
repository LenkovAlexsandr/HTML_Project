from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

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


class LoginForm(FlaskForm):
    astronaut = StringField('id астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain = StringField('id капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    list = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', list=list)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
