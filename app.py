from flask import Flask, render_template, request, session
from chatgpt import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/cleardata', methods=["GET", "POST"])
def set_data():
    session['user_data'] = None
    return 'Veri silindi'


# Define route for home page
@app.route("/get", methods=["GET", "POST"])
def gpt_response():
    
    userText = request.args.get('msg')
    
    response = get_response(userText)

    response_text = response
    return str(response_text)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=5000)
