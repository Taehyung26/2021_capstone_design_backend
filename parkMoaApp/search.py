from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Keyword, Text, Integer, Date, Search, Double
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models
connections.create_connection()

class park_info_index(Document):

    Num = Integer()
    District = Text()
    Park_division = Text()
    Park_name = Text()
    Road_address = Text()
    Parcel_address = Text()
    Park_overview = Text()
    Park_area = Text()
    Main_facility = Text()
    Sporting_goods = Text()
    Guidemap = Text()
    Direction = Text()
    Use_notes = Text()
    Image = Text()
    Park_number = Text()
    Latitude = Double()
    Longitude = Double()
    Shortcut = Text()
    Grade = Integer()
    # Keyword = 

    class Index:
        name = 'parkmoa'

def bulk_indexing():
    park_info_index.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.park_info.objects.all().iterator()))

def search(display):
    s = Search().filter('match', display=display)
    response = s.execute()
    return response