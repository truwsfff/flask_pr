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
    sp = ['Человечество вырастает из детства.',
          'Человечеству мала одна планета.',
          'Мы сделаем обитаемыми безжизненные пока планеты.',
          'И начнем с Марса!',
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


@app.route('/promotion_image')
def ad_image():
    return """<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                            
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="static/img/mars.png">
                            <p>Вот она какая, красная планета.</p>
                            <div class="alert alert-dark" role="alert">
  Человечество вырастает из детства.
</div>

                            <div class="alert alert-success" role="alert">
  Человечеству мала одна планета.
</div>

                            <div class="alert alert-secondary" role="alert">
  Мы сделаем обитаемыми безжизненные пока планеты.
</div>

                            <div class="alert alert-warning" role="alert">
  И начнем с Марса
</div>

                            <div class="alert alert-danger" role="alert">
  Присоединяйся!
</div>
                          </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
