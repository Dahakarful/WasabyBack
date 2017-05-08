import json
import elasticsearch
import certifi
from requests_aws4auth import AWS4Auth

host = 'search-elasticwasaby-y2o2s4be7d3uiwq3tr6jrkfr7i.eu-west-2.es.amazonaws.com'
awsauth = AWS4Auth('AKIAJVGUUFRVMOJVBEIA', 'p9MPwHHMg+15LRbTgXcenreY5n+ikb3i9LgHv+Wc', 'eu-west-2', 'es')

es = elasticsearch.Elasticsearch(
    hosts=[{'host': host, 'port':443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=elasticsearch.RequestsHttpConnection
)
print(es.info())
#es = elasticsearch.Elasticsearch(['https://search-elasticwasaby-y2o2s4be7d3uiwq3tr6jrkfr7i.eu-west-2.es.amazonaws.com/'])

nodes = json.load(open('../resources/result.json'))
print(len(nodes))

for buoy in nodes:
    print(buoy)
    id = buoy['id']
    #variables = v[u'variables'] #'u' pour unicode
    res = es.index(index="wasaby", doc_type="buoys", id=id, body=buoy)
    print(id)
print("Finished!")