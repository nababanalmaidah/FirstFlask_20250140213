from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None

    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
        if nama:
            hasil = f"Halo, {nama}! Data berhasil dikirim."

    return render_template("index.html", hasil=hasil)


if __name__ == "__main__":
    app.run(debug=True)

    p