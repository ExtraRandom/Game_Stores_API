import requests


class Shared:

    @staticmethod
    def get_page_raw(page):
        """Get the Raw Data (whether that be html or json) of the URL given"""
        response = requests.request("GET", page)
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            return "Error"

