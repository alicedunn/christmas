from flask import Flask, render_template, request
import lirc

from form import VoteForm

app = Flask(__name__)
client = lirc.Client()


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    form = VoteForm()
    print(request)
    if request.method == 'POST':
        if request.form.get('on'):
            client.send_once("christmas", "KEY_POWER")
        elif request.form.get('off'):
            client.send_once("christmas", "KEY_POWER2")
        elif request.form.get('brighter'):
            client.send_once("christmas", "KEY_BRIGHTNESSUP")
        elif request.form.get('dimmer'):
            client.send_once("christmas", "KEY_BRIGHTNESSDOWN")
        elif request.form.get('rotate'):
            client.send_once("christmas", "KEY_NUMERIC_1")
        elif request.form.get('twinkle'):
            client.send_once("christmas", "KEY_NUMERIC_2")
        elif request.form.get('flashing_changes'):
            client.send_once("christmas", "KEY_NUMERIC_3")
        elif request.form.get('chill_mode'):
            client.send_once("christmas", "KEY_NUMERIC_4")
        elif request.form.get('dancing'):
            client.send_once("christmas", "KEY_NUMERIC_5")
        elif request.form.get('slow_fade'):
            client.send_once("christmas", "KEY_NUMERIC_6")
        elif request.form.get('party_mode'):
            client.send_once("christmas", "KEY_NUMERIC_7")
        elif request.form.get('solid'):
            client.send_once("christmas", "KEY_NUMERIC_8")

    return render_template('christmas_vote.html', form=form)
