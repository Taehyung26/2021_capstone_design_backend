from django.utils.functional import partition
from parkMoa.settings import ALLOWED_HOSTS
from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status, permissions

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

class SearchView(APIView):
    #  default: 세션기반, http basic기반 인증 제거 => auth 없이 접근 가능
    authentication_classes = []

    def get(self, request):
        es = Elasticsearch([{
            'cloud_id': 'team-parkMoa:YXAtbm9ydGhlYXN0LTIuYXdzLmVsYXN0aWMtY2xvdWQuY29tOjkyNDMkNjc2ODhhNjFmOTZiNDNjNTlkZWFiNDUwMzUwMmQ2YTckZGM4Y2EyMTg4N2FlNDM1Nzg2OTkxMTI2YmZmNzJmZTY=',
            'http_auth': 'elastic:IaPpgyeCkU38iytPPHn4jQny',
        }])

        search_word = request.query_params.get('search')
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')

        if (not search_word) & (latitude == '37.566361') & (longitude == '126.977944') : # 위치제공 안하고 검색값 없이 검색
            docs = es.search(index = 'parkmoa',
                            body = {
                                "size":2000,
                                "sort": [
                                    {
                                        "_geo_distance": {
                                            "location": {
                                                "lat": 37.566361,
                                                "lon": 126.977944
                                            },
                                            "order": "asc",
                                            "unit": "km"
                                        }
                                    }
                                    ]
                                })

            data_list = docs['hits'] #json 타입 반환
        
        elif (not search_word) & ((latitude != '37.566361') | (longitude != '126.977944')) :
            docs = es.search(index = 'parkmoa',
                            body = {
                                "size":2000,
                                "sort": [
                                    {
                                        "_geo_distance": {
                                            "location": {
                                                "lat": latitude,
                                                "lon": longitude
                                            },
                                            "order": "asc",
                                            "unit": "km"
                                        }
                                    }
                                    ]
                                })

            data_list = docs['hits'] #json 타입 반환
        
        else:
            if (latitude == '37.566361') & (longitude == '126.977944') :
                docs = es.search(index = 'parkmoa',
                                body = {
                                    "size":2000,
                                    "query": {
                                        "multi_match": {
                                            "query": search_word,
                                        }
                                    },
                                    "sort": [
                                        {
                                            "_geo_distance": {
                                                "location": {
                                                    "lat": 37.566361,
                                                    "lon": 126.977944
                                                },
                                                "order": "asc",
                                                "unit": "km"
                                            }
                                        }
                                    ]                                      
                                })
                data_list = docs['hits']

            elif (latitude != '37.566361') | (longitude != '126.977944') :
                docs = es.search(index = 'parkmoa',
                                body = {
                                    "size":2000,
                                    "query": {
                                        "multi_match": {
                                            "query": search_word,
                                        }
                                    },
                                    "sort": [
                                        {
                                            "_geo_distance": {
                                                "location": {
                                                    "lat": latitude,
                                                    "lon": longitude
                                                },
                                                "order": "asc",
                                                "unit": "km"
                                            }
                                        }
                                    ]                                      
                                })
                data_list = docs['hits']
            return Response(data_list)
        return Response(data_list)
