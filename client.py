from twirp.context import Context
from twirp.exceptions import TwirpServerException

import  counting_pb2, counting_twirp

client = counting_twirp.NumRequestCallClient("http://localhost:4772")


for i in range(10):
    response = client.ping(ctx=Context(), request=counting_pb2.Request(count=1))
    print(response)
