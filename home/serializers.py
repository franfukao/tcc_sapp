from rest_framework import serializers
from .models import *
from rest_framework import viewsets

# -------------------------------------------------------------------------
class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'
class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
# -------------------------------------------------------------------------
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
# -------------------------------------------------------------------------
class FotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
        fields = '__all__'
class FotosViewSet(viewsets.ModelViewSet):
    queryset = Fotos.objects.all()
    serializer_class = FotosSerializer

#---------------------------------------------------------------------------
# class logonUser(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
# -------------------------------------------------------------------------

class CentralTrabSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralTrab
        fields = '__all__'
class CentralTrabViewSet(viewsets.ModelViewSet):
    queryset = CentralTrab.objects.all()
    serializer_class = CentralTrabSerializer
# -------------------------------------------------------------------------
    
class nivelAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = divisao
        fields = '__all__'
class nivelAcessoViewSet(viewsets.ModelViewSet):
    queryset = divisao.objects.all()
    serializer_class = nivelAcessoSerializer
# -------------------------------------------------------------------------
class TransacaoSucataSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = TransacaoSucata
        fields = '__all__'
# -------------------------------------------------------------------------
class TransacaoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransacaoProduto
        fields = '__all__'
class TransacaoProdutoViewSet(viewsets.ModelViewSet):
    queryset = TransacaoProduto.objects.all()
    serializer_class = TransacaoProdutoSerializer
# -------------------------------------------------------------------------
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
# -------------------------------------------------------------------------
class HistoricoSucataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoSucata
        fields = '__all__'
class HistoricoSucataViewSet(viewsets.ModelViewSet):
    queryset = HistoricoSucata.objects.all()
    serializer_class = HistoricoSucataSerializer
# -------------------------------------------------------------------------
class HistoricoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoProduto
        fields = '__all__'
class HistoricoProdutoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoProduto.objects.all()
    serializer_class = HistoricoProdutoSerializer
# -------------------------------------------------------------------------

