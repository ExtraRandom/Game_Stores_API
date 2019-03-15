import requests
import os


class Shared:

    @staticmethod
    def get_page_raw(page):
        """Get the Raw Data (whether that be html or json) of the URL given"""
        response = requests.request("GET", page)
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            print(response.status_code)
            return "Error"

    @staticmethod
    def get_json(url):
        """Get the Raw Data (whether that be html or json) of the URL given"""
        response = requests.request("GET", url)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            print(response.status_code)
            return "Error"

    @staticmethod
    def url_encode(to_encode, encode_char_list):
        """ """
        output = to_encode
        for replace_char in encode_char_list:
            output = output.replace(replace_char, "%20")
        return output

    @staticmethod
    def dbg_working_dir():
        """Return current working directory (varies from OS)"""
        return str(os.getcwd())







