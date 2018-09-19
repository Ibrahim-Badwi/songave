import josn
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import services


youtube = services.YoutubeDonwloader()

class SearchList(APIView):
    """
    get a list of youtube results based on user query
    """
    def get(self, request):
        query = request.GET.get('q', '')
        item_per_query = 1

        if 'n' in request.GET:
            item_per_query = request.GET.get('n', '') 

        try:
            search_string = " ".join(query.split('-'))
        except:
            search_string = query

        result_json_list = youtube.get_list(search_string, num=item_per_query)
        return Response(result_json_list)


class SearchDetail(APIView):
    """
    download specific youtube vedio by url id
    """
    def get(self, request, url_id):
        #url_id = request.GET.get('id', '')

        return Response(url_id)
