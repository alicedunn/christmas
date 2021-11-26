from flask import Flask, render_template, request
# import lirc

from form import VoteForm

app = Flask(__name__)
# client = lirc.Client()


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    form = VoteForm()
    if request.method == 'POST':
        response = request.form['vote']
        if response == 'dog':
            # client.send_once("christmas", "KEY_POWER")
            print('dog')
        if response == 'cat':
            print('cat')
            # client.send_once("christmas", "KEY_POWER2")

    return render_template('christmas_vote.html', form=form)
