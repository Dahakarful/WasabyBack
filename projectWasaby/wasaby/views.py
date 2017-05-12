import json
import elasticsearch
from django.http import HttpResponse
from requests_aws4auth import AWS4Auth
from django.http import JsonResponse

indexName = 'wasaby'
typeName = 'buoys'
jsonPath = '../resources/result.json'

host = 'search-elasticwasaby-y2o2s4be7d3uiwq3tr6jrkfr7i.eu-west-2.es.amazonaws.com'
awsauth = AWS4Auth('AKIAJVGUUFRVMOJVBEIA', 'p9MPwHHMg+15LRbTgXcenreY5n+ikb3i9LgHv+Wc', 'eu-west-2', 'es')

es = elasticsearch.Elasticsearch(
    hosts=[{'host': host, 'port':443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=elasticsearch.RequestsHttpConnection
)

def indexBuoys(request):
    print(request)
    nodes = json.load(open(jsonPath))
    print(len(nodes))
    for k, v in nodes.items():
        id = k
        res = es.index(index=indexName, doc_type=typeName, id=id, body=v)
        print(res)
    return HttpResponse("Number of created objects %d" % len(nodes))

def searchAll(request):
    print(request)
    res = es.search(index=indexName, filter_path=['hits.hits._source.*'], body={"query": {"match_all": {}}})
    print(res)
    jsonObj = json.dumps(res)
    return JsonResponse(jsonObj, safe=False)

def searchABuoy(request):
    print(request)
    id = request.GET.get('id')
    print(id)
    res = es.search(index=indexName, filter_path=['hits.hits._source.*'], body={"query":{"match":{"id": id}}})
    print(res)
    jsonObj = json.dumps(res)
    return JsonResponse(jsonObj, safe=False)