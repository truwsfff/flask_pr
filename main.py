from flask import Flask, url_for, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1 align='center'>Анкета претендента</h1>
                                <h4 align='center'>на участие в миссии</h4>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" placeholder="Введите фамилию" name="surname">
                                        <input type="text" class="form-control" placeholder="Введите имя" name="name">
                                        </br>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                            </select>
                                         </div>
                                         </br>
                                         <label for="classSelect">Какие у Вас есть профессии?</label>
                                         <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="work" name="work1">
                                            <label class="form-check-label" for="acceptRules">Врач</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="work" name="work2">
                                            <label class="form-check-label" for="acceptRules">Штурман</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="work" name="work3">
                                            <label class="form-check-label" for="acceptRules">Климатолог</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="work" name="work4">
                                            <label class="form-check-label" for="acceptRules">Киберинженер</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="work" name="work5">
                                            <label class="form-check-label" for="acceptRules">Пилот</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="work" name="work6">
                                            <label class="form-check-label" for="acceptRules">Строитель</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="work" name="work7">
                                            <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="work" name="work8">
                                            <label class="form-check-label" for="acceptRules">Астрогеолог</label>
                                        </div>
                                        </br>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        </br>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        </br>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        </br>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        </br>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
