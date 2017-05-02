import json
import requests
import elasticsearch
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

url = 'http://localhost:9200/index/buoys'
indexName = 'index'
typeName = 'buoys'
jsonPath = 'C:/Users/Ragonda/gitHub/Wasaby/back/projectWasaby/resources/buoys.json'

es = elasticsearch.Elasticsearch()


def indexBuoys(request):
    print(request)
    nodes = json.load(open(jsonPath))
    print(len(nodes))
    for k, v in nodes.items():
        id = k
        res = es.index(index=indexName, doc_type=typeName, id=id, body=v)
        print(res)
    return HttpResponse("Number of created objects %d" % len(nodes))


@csrf_exempt
def searchABuoy(self):
    data = self.request.data
    print(data)
