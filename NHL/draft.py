import requests


class Draft:
    def __init__(self):
        self.draft_url = 'https://statsapi.web.nhl.com/api/v1/draft/'
        self.players = {}
        pass

    def get_draft(self, year):
        url = self.draft_url + str(year)
        api_response = requests.get(url)
        return api_response.json()




