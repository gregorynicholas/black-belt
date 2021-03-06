from slacker import Slacker
from blackbelt.config import config

class Slack(object):
    def __init__(self, token=None):
        if not token:
            token = config['slack']['access_token']
            slack = Slacker(token)
            self.slack = slack
        if not token:
            raise ValueError("Can't do things with Slack without access token. Run bb init.")

        self.token = token

    def post_message(self, message, room='#engine-room'):
        return self.slack.chat.post_message(room, message)


def post_message(message):
    client = Slack()
    client.post_message(message)
