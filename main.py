from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def welcome_m():
    return "Миссия Колонизация Марса"

@app.route('/index')
def text():
    return 'И на Марсе будут яблони цвести!'

@app.route('/promotion')
def ad():
    sp = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
          'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
          'Присоединяйся!']
    return '</br></br>'.join(sp)

@app.route('/image_mars')
def image():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="static/img/mars.png">
                        <p>Вот она какая, красная планета.</p>
                      </body>
                    </html>"""

@app.route('/image_mars1')
def image1():
    return f'''<img src="{url_for('static', filename='img/mars.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')