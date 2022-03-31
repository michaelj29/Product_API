from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from products import serializers

@api_view(['GET'])
def product_list(request):
  product = Product.objects.all()
  serializer = ProductSerializer(product, many=True)
  return Response(serializer.data)



# Create your views here.
