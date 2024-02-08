from pysnc import ServiceNowClient


class ServiceNowConnector:
    def __init__(self, url, user, password):
        self.client = ServiceNowClient(url, (user, password))

    def get_incidents(self):
        gr = self.client.GlideRecord('incident')
        gr.query()
        return gr
