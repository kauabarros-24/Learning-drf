from rest_framework.viewsets import ModelViewSet
from core.models import Livro
from core.serializers import LivroSerializer, LivroDetailSerializer, LivroListSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    def get_serializer_class(self):
        #O action é a ação tomada quando forms for enviado  
        return LivroListSerializer if self.action == "list" else LivroDetailSerializer
        return LivroSerializer  
