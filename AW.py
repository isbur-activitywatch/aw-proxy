"""
Wrapper around `requests` lib

HIDE EVERYTHING!!!
"""
import requests 
from urllib.parse import urljoin


class AW(requests.Session):

    def __init__(self, url):
        requests.Session.__init__(self)
        self.base_url = url
        self.buckets = self.get("/api/0/buckets")
        for bucket_id in self.buckets.keys():
            self.buckets[bucket_id]["n_previous"] = self.get_event_count_from_(bucket_id)
    
    def get(self, appendix = "", **kwargs):        
        my_url = urljoin(self.base_url, appendix)
        return requests.Session.get(self, my_url, **kwargs).json()
    
    def post(self, appendix = "", **kwargs):
        my_url = urljoin(self.base_url, appendix)
        return requests.Session.post(self, my_url, **kwargs)

    def get_buckets_quickly(self):
        return self.buckets

    def get_event_count_from_(self, bucket_id):
        if type(bucket_id) != type(""):
            raise TypeError("must be str")

        return self.get(
        "/api/0/buckets/"   +
                    bucket_id  +
                    "/events/count"
        )
    
    def ping(self):
        return "pong"


AW = AW("http://localhost:5600")