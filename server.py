from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument

import  counting_pb2, counting_twirp

class CountClass(object):

    def __init__(self):
        self.counter = 0
    
    def ping(self, request, context):
        self.counter += 1
        return counting_pb2.Counter(count=self.counter)

service = counting_twirp.NumRequestCallServer(service=CountClass())
app = TwirpASGIApp()
app.add_service(service)
        
