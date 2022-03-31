from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET', 'POST'])
def product_list(request):
  product = Product.objects.all()
  if request.method == 'GET':
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
