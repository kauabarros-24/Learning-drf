from rest_framework.viewsets import ModelViewSet
from core.models import Livro
from core.serializers import LivroSerializer, LivroDetailSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    def get_serializer_class(self):
        #O action é a ação tomada quando forms for enviado  
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer
