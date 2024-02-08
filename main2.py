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


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
