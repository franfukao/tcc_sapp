from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
from django.db import connection
import cx_Oracle as Database
from django.shortcuts import render
import cx_Oracle
import math 

# from django.contrib.auth.models import User

# class logonView(APIView):
#     """
#     API logonView
#     """
#     def post(self, request):
#         myuser: {
#             'username':'',
#             'password':'',
#             'email':'',
#         }

#         myuser = User.objects.save()
#         serializer1 = logonUser(data=request.data, many=True)
#         serializer1.is_valid(raise_exception=True)
#         serializer1.save()
#         id = User.objects.latest('id')
#         data = request.data
#         data[0]['idUserFK'] = id.id
#         print(data[0]['idUserFK'])

#         serializer2 = UsuarioSerializer(data=data, many=True)
#         serializer2.is_valid(raise_exception=True)
#         serializer2.save()
#         return Response({"msg": "Inserido com sucesso"})


def getPagination(request, listItems):
    paginas = math.ceil(listItems.count()/10)
    if 'page' in request.GET:
        try:
            parameter_page = request.GET['page']
            
            if (int(parameter_page) <= 0):
                parameter_page = '1'
            page = Paginator(listItems, 10)
            return [page.page(parameter_page), page.count, page.num_pages]
        except (EmptyPage, PageNotAnInteger):
            return [page.page(1), 0, 0]
    else:
        return [listItems, 0, 0]
# ----------------------------------------------------------------------------------------------
class PesquisaView(APIView):
    """
    API pesquisa
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
            if 'produto_num' in request.GET:            
                produto_num = request.GET['produto_num']
                pesquisa = redlakeSearch_numero(produto_num)
                return Response({"produtos": pesquisa})
            
            elif 'produto_name' in request.GET: 
                produto_name = request.GET['produto_name']
                pesquisa = redlakeSearch_name(produto_name)
                return Response({"produtos": pesquisa})
#-----------------------------------------------------------------------------------------#
def redlakeSearch_numero(produto_num):
    connection = cx_Oracle.connect(user="lge1ca", password="Safira2021!leo",dsn="redlake_dwhp.world")
    cursor = connection.cursor()
    sql = """SELECT MARD.MATNR, MARD.LABST, MAKT.MAKTX FROM INFM_PSLA_CSC2.V_REPL_MARD_B2 MARD inner join INFM_PSLA_CSC2.V_REPL_MAKT_B2 MAKT
    ON MARD.MATNR = MAKT.MATNR where MARD.MATNR = :mid and MARD.WERKS = '908A' and MARD.LABST <> 0"""
    cursor.execute(sql, mid=produto_num)
    
    # for row in cursor:
        # print(row)

    return cursor

#-----------------------------------------------------------------------------------------#
def redlakeSearch_name(produto_name):
    produto_name = '%' + produto_name + '%'
    print (produto_name)
    connection = cx_Oracle.connect(user="lge1ca", password="Safira2021!leo",dsn="redlake_dwhp.world")
    cursor = connection.cursor()
    sql = """SELECT MARD.MATNR, MARD.LABST, MAKT.MAKTX FROM INFM_PSLA_CSC2.V_REPL_MARD_B2 MARD inner join INFM_PSLA_CSC2.V_REPL_MAKT_B2 MAKT
    ON MARD.MATNR = MAKT.MATNR where lower(MAKT.MAKTX) like lower(:mid) and MARD.WERKS = '908A' and MARD.LABST <> 0"""
    cursor.execute(sql, mid=produto_name)

    # for row in cursor:
        # print(row)

    return cursor
# -------------------------------------------------------------------------------------------
class nivelAcessoView(APIView):
    """
    API nivelAcesso
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        # redlakeSearch()
        if 'nivel' in request.GET:            
            nivel = request.GET['nivel']
            Acesso = nivelAcesso.objects.filter(id=nivel)
            serializer = nivelAcessoSerializer(Acesso, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            Acesso = nivelAcesso.objects.get(id=pk)
            serializer = nivelAcessoSerializer(Acesso)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            Acesso = nivelAcesso.objects.all()
            serializer = nivelAcessoSerializer(Acesso, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = nivelAcessoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
  
    def put(self, request, pk=''):
        Acesso = nivelAcesso.objects.get(id=pk)
        serializer = nivelAcessoSerializer(Acesso, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        Acesso = nivelAcesso.objects.get(id=pk)
        Acesso.delete()
        return Response({"msg": "Apagado com sucesso"})
#-----------------------------------------------------------------------------------------#
class ResponsavelView(APIView):
    """
    API Responsavel
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'respon' in request.GET:
            respon = request.GET['respon']
            dado = Responsavel.objects.filter(id=respon)
            serializer = ResponsavelSerializer(dado, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            dado = Responsavel.objects.get(id=pk)
            serializer = ResponsavelSerializer(dado)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            dado = Responsavel.objects.all()
            serializer = ResponsavelSerializer(dado, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = ResponsavelSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        dado = Responsavel.objects.get(id=pk)
        serializer = ResponsavelSerializer(dado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dado = Responsavel.objects.get(id=pk)
        dado.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class ProdutoView(APIView):
    """
    API Produto
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'prod' in request.GET:
            prod = request.GET['prod']
            dad = Produto.objects.filter(id=prod)
            serializer = ProdutoSerializer(dad, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            dad = Produto.objects.get(id=pk)
            serializer = ProdutoSerializer(dad)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            dad = Produto.objects.all()
            serializer = ProdutoSerializer(dad, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        dad = Produto.objects.get(id=pk)
        serializer = ProdutoSerializer(dad, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dad = Produto.objects.get(id=pk)
        dad.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class TransacaoSucataView(APIView):
    """
    API TransacaoSucata
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'Sucata' in request.GET:
            Sucata = request.GET['Sucata']
            infoss = TransacaoSucata.objects.filter(id=Sucata)
            serializer = TransacaoSucataSerializerRead(infoss, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            infoss = TransacaoSucata.objects.get(id=pk)
            serializer = TransacaoSucataSerializerRead(infoss)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            infoss = TransacaoSucata.objects.all()
            serializer = TransacaoSucataSerializerRead(infoss, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = TransacaoSucataSerializerRead(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        infoss = TransacaoSucata.objects.get(id=pk)
        serializer = TransacaoSucataSerializerRead(infoss, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        infoss = TransacaoSucata.objects.get(id=pk)
        infoss.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class TransacaoProdutoView(APIView):
    """
    API TransacaoProduto
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'prod' in request.GET:
            prod = request.GET['prod']
            base = TransacaoProduto.objects.filter(id=prod)
            serializer = TransacaoProdutoSerializer(base, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            base = TransacaoProduto.objects.get(id=pk)
            serializer = TransacaoProdutoSerializer(base)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            base = TransacaoProduto.objects.all()
            serializer = TransacaoProdutoSerializer(base, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = TransacaoProdutoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        base = TransacaoProduto.objects.get(id=pk)
        serializer = TransacaoProdutoSerializer(base, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        base = TransacaoProduto.objects.get(id=pk)
        base.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class FotosAPIView(APIView):
    """
    API Fotos
    """

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'produto' in request.GET:   
            produto = request.GET['produto']
            fotos = Fotos.objects.filter(idProdutoFK=produto)
            resp = getPagination(request, fotos)
            serializer = FotosSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        elif pk != '':
            fotos = Fotos.objects.get(id=pk)
            serializer = FotosSerializer(fotos)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            fotos = Fotos.objects.all()
            resp = getPagination(request, fotos)
            serializer = FotosSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )


    def post(self, request):
        serializer = FotosSerializer(data=request.data)
        # print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        # return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        fotos = Fotos.objects.get(id=pk)
        serializer = FotosSerializer(fotos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        fotos = Fotos.objects.get(id=pk)
        fotos.delete()
        return Response({"msg": "Apagado com sucesso"})
#-----------------------------------------------------------------------
class UsuarioAPIView(APIView):
    """
    API Usuario
    """

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'user' in request.GET:
            user = request.GET['user']
            usuarios = Usuario.objects.filter(user=user)
            serializer = UsuarioSerializer(usuarios, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )            
        elif pk == '':
            usuarios = Usuario.objects.all()
            resp = getPagination(request, usuarios)
            serializer = UsuarioSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        else:
            usuarios = Usuario.objects.get(idUserFK=pk)
            serializer = UsuarioSerializer(usuarios)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )


    def post(self, request):        
        serializer = UsuarioSerializer(data=request.data, many=True)      
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        usuarios = Usuario.objects.get(id=pk)
        serializer = UsuarioSerializer(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        usuarios = Usuario.objects.get(id=pk)
        usuarios.delete()
        return Response({"msg": "Apagado com sucesso"})

# ---------------------------------------------------------------------#
class CentralTrabView(APIView):
    """
    API CentralTrab
    """
    def get(self, request, pk=''):
            Acesso = CentralTrab.objects.all()
            resp = getPagination(request, Acesso)   
            serializer = CentralTrabSerializer(resp[0], many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2],

                    "msg": "sucesso"
                }
            )
#-------------------------------------------------------------------------
class HistoricoSucataAPIView(APIView):
    """
    API HistoricoSucata
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'sucata' in request.GET:            
            sucata = request.GET['sucata']
            hist = HistoricoSucata.objects.filter(id=sucata)
            serializer = HistoricoSucataSerializer(hist, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            hist = HistoricoSucata.objects.get(id=pk)
            serializer = HistoricoSucataSerializer(hist)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            hist = HistoricoSucata.objects.all()
            serializer = HistoricoSucataSerializer(hist, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = HistoricoSucataSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
  
    def put(self, request, pk=''):
        hist = HistoricoSucata.objects.get(id=pk)
        serializer = HistoricoSucataSerializer(hist, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        hist = HistoricoSucata.objects.get(id=pk)
        hist.delete()
        return Response({"msg": "Apagado com sucesso"})
#-----------------------------------------------------------------------------------------#
class HistoricoProdutoAPIView(APIView):
    """
    API HistoricoProduto
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'sucata' in request.GET:            
            sucata = request.GET['sucata']
            histo = HistoricoProduto.objects.filter(id=histo)
            serializer = HistoricoProdutoSerializer(histo, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            histo = HistoricoProduto.objects.get(id=pk)
            serializer = HistoricoProdutoSerializer(histo)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            histo = HistoricoProduto.objects.all()
            serializer = HistoricoProdutoSerializer(histo, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = HistoricoProdutoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
  
    def put(self, request, pk=''):
        histo = HistoricoProduto.objects.get(id=pk)
        serializer = HistoricoProdutoSerializer(histo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        histo = HistoricoProduto.objects.get(id=pk)
        histo.delete()
        return Response({"msg": "Apagado com sucesso"})
# -------------------------------------------------------------------------------------

    

