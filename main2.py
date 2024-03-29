from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def a():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    'Миссия Колонизация Марса'
                  </body>
                </html>"""


@app.route('/index')
def index():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    "И на Марсе будут яблони цвести!"
                  </body>
                </html>"""


@app.route('/promotion')
def promotion():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    Человечество вырастает из детства.</br>
                    </br>Человечеству мала одна планета.</br>
                    </br>Мы сделаем обитаемыми безжизненные пока планеты.</br>
                    </br>И начнем с Марса!</br>
                    </br>Присоединяйся!
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1><r1>Жди нас, Марс!<r1></h1>
            <img src="{url_for('static', filename='img/mars.jpg')}" 
            alt="здесь должна была быть картинка, но не нашлась">
            </br><fb>Человечество вырастает из детства.</fb>
            </br><fg>Человечеству мала одна планета.</fg>
            </br><fgr>Мы сделаем обитаемыми безжизненные пока планеты.</fgr>
            </br><fy>И начнем с Марса!</fy>
            </br><fr>Присоединйся!</fr>
        </body>
        </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
            <html lang="en">
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
            <title>Варианты выбора!</title>
            <body>
                <h1>Мое предложение: {planet_name}</h1>
                Эта планета близко к Земле;</br>
                <fg>На ней много необходимых ресурсов;</fg></br>
                <fgr>На ней есть вода и атмосфера;</fgr></br>
                <fy>На ней есть небольшое магнитное поле;</fy></br>
                <fr>Наконец, она просто красива!</fr>
            </body>
            </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                <meta charset="utf-8">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                <title>Результаты</title>
                <body>
                    <h2>Результаты отбора</h2>
                    <h3>Претендента на участие в миссии {nickname}:</h3>
                    <fg>Поздравляем! Ваш рейтинг после {level} этапа отбора</fg></br>
                    составляет {rating}!</br>
                    <fy>Желаем удачи!</fy>
                </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
