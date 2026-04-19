from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/length", methods=["GET", "POST"])
def length():
    if request.method == "POST":
        text = request.form["text"]

        result = len(text)

        return render_template("result11.html", result=result)

    return render_template("index11.html")

if __name__ == "__main__":
    app.run(debug=True)
