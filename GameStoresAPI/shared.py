import requests
import os


class Shared:

    @staticmethod
    def get_page_raw(page):
        """Get the Raw Data (whether that be html or json) of the URL given"""
        response = requests.request("GET", page)
        if response.status_code == requests.codes.ok:
            return response.text
        else:  # print(response.status_code)
            return "Error"

    @staticmethod
    def get_json(url):
        """Get the Raw Data (whether that be html or json) of the URL given"""
        response = requests.request("GET", url)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:  # print(response.status_code)
            return "Error"

    @staticmethod
    def get_cache_folder():
        """Get the location of the cache folder"""
        folder = os.path.join(os.getcwd(), "GSAPI_Cache")
        if os.path.exists(folder) is False:
            os.mkdir(folder)  # Ensure folder exists
        return folder







