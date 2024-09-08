from flask import Flask

from src import resume_maker

app = Flask(__name__, static_url_path="", static_folder="public")

@app.route("/")
def resume_from_file():

    return resume_maker.generate_()

@app.route("/methods/generate", methods=["POST"])
def generate_():
    resume_maker.generate_()
    return resume_maker.generate_()

if __name__ == '__main__':
    resume_maker.generate_()
    app.run(host="localhost", port=4352, debug=True)