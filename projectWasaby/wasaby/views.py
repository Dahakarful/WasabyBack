import json
import requests
import elasticsearch
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

url = 'https://search-elasticwasaby-y2o2s4be7d3uiwq3tr6jrkfr7i.eu-west-2.es.amazonaws.com/'
indexName = 'wasaby'
typeName = 'buoys'
jsonPath = '../resources/result.json'

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
