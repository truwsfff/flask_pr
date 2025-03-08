from flask import Flask

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def ad_image(planet_name):
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                            
                            <title>Варианты выбора</title>
                          </head>
                          <body>
                            <h1>Мое предложение: {planet_name}</h1>
                            <h4>Эта планета близка к Земле;</h4>

                            <div class="alert alert-success" role="alert">
  <h4>На ней много необходимых ресурсов;</h4>
</div>

                            <div class="alert alert-secondary" role="alert">
  <h4>На ней есть вода и атмосфера;</h4>
</div>

                            <div class="alert alert-warning" role="alert">
  <h4>На ней есть небольшое магнитное поле;</h4>
</div>

                            <div class="alert alert-danger" role="alert">
  <h4>Наконец, она просто красива!</h4>
</div>
                          </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
