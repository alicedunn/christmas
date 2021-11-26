from wtforms import Form, RadioField


class VoteForm(Form):
    vote = RadioField('vote', choices=[('dog', 'Dog'), ('cat', 'Cat')])