from wtforms import Form, RadioField


class VoteForm(Form):
    vote = RadioField('vote', choices=[('on', 'On'),
                                       ('off', 'Off'),
                                       ('brighter', 'Brighter'),
                                       ('dimmer', 'Dimmer'),
                                       ('rotate', 'Rotate Modes'),
                                       ('twinkle', 'Twinkle'),
                                       ('flashing_changes', 'Flashing Changes'),
                                       ('chill_mode', 'Chill Mode'),
                                       ('dancing', 'Dancing'),
                                       ('slow_fade', 'Slow Fade'),
                                       ('party_mode', 'Party Mode'),
                                       ('solid', 'Solid Light')])
