from django.urls import path
from .views import *

urlpatterns = [
  # path("logonview/", logonView.as_view(), name='logonview'),
  path("nivelAcesso/", nivelAcessoView.as_view(), name='nivelAcesso'),
  path('nivelAcesso/<int:pk>/', nivelAcessoView.as_view(), name='nivelAcessoParameters'),

  path("Responsavel/", ResponsavelView.as_view(), name='Responsavel'),
  path('Responsavel/<int:pk>/', ResponsavelView.as_view(), name='ResponsavelParameters'),

  path("Produto/", ProdutoView.as_view(), name='Produto'),
  path('Produto/<int:pk>/', ProdutoView.as_view(), name='ProdutoParameters'),

  path("TransacaoSucata/", TransacaoSucataView.as_view(), name='TransacaoSucata'),
  path('TransacaoSucata/<int:pk>/', TransacaoSucataView.as_view(), name='TransacaoSucataParameters'),

  path("TransacaoProduto/", TransacaoProdutoView.as_view(), name='TransacaoProduto'),
  path('TransacaoProduto/<int:pk>/', TransacaoProdutoView.as_view(), name='TransacaoProdutoParameters'),

  path("cod_sucata/",CentralTrabView.as_view(), name='cod_sucata'),
  
  path("foto/", FotosAPIView.as_view(), name='foto'),
  path('foto/<int:pk>/', FotosAPIView.as_view(), name='fotoParameters'),

  path("Usuario/", UsuarioAPIView.as_view(), name='Usuario'),
  path('Usuario/<int:pk>/', UsuarioAPIView.as_view(), name='UsuarioParameters'),

  path("HistoricoSucata/", HistoricoSucataAPIView.as_view(), name='HistoricoSucata'),
  path('HistoricoSucata/<int:pk>/', HistoricoSucataAPIView.as_view(), name='HistoricoSucataParameters'),

  path("HistoricoProduto/", HistoricoProdutoAPIView.as_view(), name='HistoricoProduto'),
  path('HistoricoProduto/<int:pk>/', HistoricoProdutoAPIView.as_view(), name='HistoricoProdutoParameters'),

  path("Pesquisa/", PesquisaView.as_view(), name='Pesquisa'),
]