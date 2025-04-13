from models import WasteRequest

class WasteController:
    def __init__(self):
        self.requests = []

    def schedule_request(self, name, waste_type, date):
        req = WasteRequest(len(self.requests)+1, name, waste_type, date)
        self.requests.append(req)
