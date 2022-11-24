import json
from urllib import response
from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from yaml import serialize

from products.models import Product
from products.serializers import ProductSerializer







@api_view(["POST"])
def api_home(request, *args, **kwargs): #this has now become a DRF Api View
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)











# @api_view(["GET"])
# def api_home(request, *args, **kwargs): #this has now become a DRF Api View
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
      
#     if instance:  #i.e. if model_data is set to something (exxists)
#         data = ProductSerializer(instance).data


#         # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
#         # print(data)
#         # json_data_str = json.dumps(data)
#     # data['headers'] = {'content-type':'application/json'}
#     return Response(data)
 


# Create your views here.







    # if model_data:  #i.e. if model_data is set to something (exxists)
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    # return JsonResponse(data)







# print(dict(request.GET))
# body = request.body

# data = {}
# try:
#     data = json.loads(body) #this takes a strong of JSON data and converts into a python dictionart
# except:
#     pass #if body has no content, nothing in loaded and empty dict is dsiplayed
# # echoing the data in json
# print(data)
# # print(request.headers)
# data['params'] = dict(request.GET)
# data['headers'] = dict(request.headers)
# data['content_type'] = request.content_type
# data['content-length'] = '24'

# return JsonResponse(data)














































































# import json
# from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from products.models import Product

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View
#     """
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     # return JsonResponse(data)
#     #     print(data)
#     #     data = dict(data)
#     #     json_data_str = json.dumps(data)
#     # return HttpResponse(json_data_str, headers={"content-type": "application/json"})
#     return Response(data)