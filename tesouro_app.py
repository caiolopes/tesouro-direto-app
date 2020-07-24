from flask import Flask
import consulta_rentabilidade as cr

app = Flask(__name__)


@app.route("/api/rentabilidade/dia/<titulo>")
def rentabilidade_dia(titulo):
    df = cr.rentabilidade_dia(titulo)

    response = app.make_response(df.to_json())
    response.headers["Content-Type"] = "application/json"
    return response


if __name__ == "__main__":
    app.run(debug=True)
