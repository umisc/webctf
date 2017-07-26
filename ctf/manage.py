"""Launches and renders routes for paced's resume page."""

import os

from flask import (Flask, make_response, redirect, render_template, request,
                   send_from_directory)

# Necessary settings
DEBUG = True

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """Standard page redirect."""
    return redirect("/level1/", code=301)


@app.route('/level1/', methods=['GET', 'POST'])
def level1():
    """Controller for CTF level."""
    if request.method == "POST":
        if request.form["pass"] == "Hunter2":
            redirect_to_index = redirect('/level2/')
            response = make_response(redirect_to_index)
            response.set_cookie('level1', value="true")

            return response
        else:
            return "Incorrect password. Go back."
    return render_template('pages/level1.jinja.html')


@app.route('/level2/', methods=['GET', 'POST'])
def level2():
    """Controller for CTF level."""
    if request.cookies.get("level1") != "true":
        return "Permission denied. Go back."
    return render_template('pages/level2.jinja.html')


@app.route('/level3/', methods=['GET', 'POST'])
def level3():
    """Controller for CTF level."""
    if request.cookies.get("level2") != "true":
        return "Permission denied. Go back."
    return render_template('pages/level3.jinja.html')


@app.route('/level4/', methods=['GET', 'POST'])
def level4():
    """Controller for CTF level."""
    if request.cookies.get("level3") != "true":
        return "Permission denied. Go back."
    return render_template('pages/level4.jinja.html')


@app.route('/level5/', methods=['GET', 'POST'])
def level5():
    """Controller for CTF level."""
    if request.cookies.get("level4") != "true":
        return "Permission denied. Go back."
    if request.method == "POST":
        if request.form["attempt"] == "still_clientside":
            return "true"
        else:
            return "false"
    return render_template('pages/level5.jinja.html')


@app.route('/level6/', methods=['GET', 'POST'])
def level6():
    """Controller for CTF level."""
    if request.cookies.get("level5") != "true":
        return "Permission denied. Go back."
    return render_template('pages/level6.jinja.html')


@app.route('/level7_secret_9005619802/', methods=['GET', 'POST'])
def level7():
    """Controller for CTF level."""
    if request.method == "POST":
        redirect_to_index = redirect('/level8/')
        response = make_response(redirect_to_index)
        response.set_cookie('level7', value="true")

        return response
    return render_template('pages/level7.jinja.html')


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Contact forms."""
    return send_from_directory('static/', 'sitemap.xml')


@app.route('/robots.txt')
def robots():
    """Robot file for SEO."""
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robots.txt')


if __name__ == "__main__":
    app.run(debug=DEBUG, host='localhost')
