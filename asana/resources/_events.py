# This file is automatically generated by generate.py using api.json

class _Events:
    def __init__(self, session=None):
        self.session = session

    def get(self, params={}):
        return self.session.get('/events', params, {u'fullPayload': True})