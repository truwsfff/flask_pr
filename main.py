from flask import Flask

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def ad_image(nickname, level, rating):
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                            
                            <title>Результаты</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h3>Претендента на участие в миссии {nickname}:</h3>

                            <div class="alert alert-success" role="alert">
  <h4>Поздравляем! Ваш рейтинг после {level} этапа отбора</h4>
</div>

                            <div class="alert alert-light" role="alert">
  <h4>составляет {rating}!</h4>
</div>

                            <div class="alert alert-warning" role="alert">
  <h3>Желаем удачи!</h3>
</div>
                          </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
