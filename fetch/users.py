import requests


class UserFetcher:
    def __init__(self):
        self._url = "https://randomuser.me/api/"

    def get_users(self, n: int):
        number_result = f"?results={n}"
        include_path = "?inc=gender,name,nat,picture,email,login,location,dob"
        response = requests.get(self._url + number_result + include_path).json()["results"]
        return response



