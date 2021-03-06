from rest_framework import generics
from rest_framework.response import Response
from .custom_renderers import JPEGRenderer,PNGRenderer
from rest_framework.response import Response
from ..images.models import Images

class ImageAPIView(generics.RetrieveAPIView):
    renderer_classes = [JPEGRenderer]
    
    def get(self,request,*args,**kwargs):
      
      queryset = Images.objects.get(id = self.kwargs['id'].image)
      data = queryset 
      return Response(data,content_type='image/jpg ')

