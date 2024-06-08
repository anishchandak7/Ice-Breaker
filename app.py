"""Main file to execute with """
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_break_with

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    """
    The above function defines a route in a Flask web application that renders an HTML template named
    'index.html' when the route is accessed.
    :return: The `index()` function is returning the result of `render_template('index.html')`, which is
    typically an HTML file rendered by the Flask application.
    """
    return render_template('index.html')

@app.route("/process", methods=["POST"])
def process():
    """
    The function "process" takes a POST request with a name parameter, calls the "ice_break_with"
    function with the provided name, and returns a JSON response with the summary and profile picture
    URL.
    :return: The `process` route is returning a JSON response with two keys: "summary_and_facts" and
    "picture_url". The "summary_and_facts" key contains the summary and facts of the person obtained
    from the `ice_break_with` function in dictionary format, and the "picture_url" key contains the URL
    of the person's profile picture.
    """
    name = request.form["name"]
    summary, profile_pic_url = ice_break_with(name=name)
    print(profile_pic_url)
    return jsonify(
        {
            "summary_and_facts": summary.to_dict(),
            "picture_url": profile_pic_url
        }
    )

if __name__=='__main__':
    app.run(host="0.0.0.0", debug=True)
