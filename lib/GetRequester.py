# import requests
# import json

# class GetRequester:

#     def __init__(self, url):
#         self.url = url

#     def get_response_body(self):
#         pass

#     def load_json(self):
#         pass

import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response = json.loads(self.get_response_body())
        return response

url = " https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

test = GetRequester(url)
print(test.load_json())