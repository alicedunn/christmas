from flask import Flask, render_template, request
import lirc

from form import VoteForm

app = Flask(__name__)
client = lirc.Client()


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    form = VoteForm()
    if request.method == 'POST':
        print(request.form)
        response = request.form['vote']
        if response == 'on':
            client.send_once("christmas", "KEY_POWER")
        elif response == 'off':
            client.send_once("christmas", "KEY_POWER2")
        elif response == 'brighter':
            client.send_once("christmas", "KEY_BRIGHTNESSUP")
        elif response == 'dimmer':
            client.send_once("christmas", "KEY_BRIGHTNESSDOWN")
        elif response == 'rotate':
            client.send_once("christmas", "KEY_NUMERIC_1")
        elif response == 'twinkle':
            client.send_once("christmas", "KEY_NUMERIC_2")
        elif response == 'flashing_changes':
            client.send_once("christmas", "KEY_NUMERIC_3")
        elif response == 'chill_mode':
            client.send_once("christmas", "KEY_NUMERIC_4")
        elif response == 'dancing':
            client.send_once("christmas", "KEY_NUMERIC_5")
        elif response == 'slow_fade':
            client.send_once("christmas", "KEY_NUMERIC_6")
        elif response == 'party_mode':
            client.send_once("christmas", "KEY_NUMERIC_7")
        elif response == 'solid':
            client.send_once("christmas", "KEY_NUMERIC_8")

    return render_template('christmas_vote.html', form=form)
