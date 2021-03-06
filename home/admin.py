from django.contrib import admin
from .models import *

class detCentroCusto(admin.ModelAdmin): #Views
    list_display = ('id','codigoCentro')

class dettipoMovimento(admin.ModelAdmin): #Views
    list_display = ('id','nometipoMovimento')

class detcontaRazao(admin.ModelAdmin): #Views
    list_display = ('id','nomeContaRazao')

class dettipoOrdem(admin.ModelAdmin): #Views
    list_display = ('id','nomeTipoOrdem')

class detlocalInstal(admin.ModelAdmin): #Views
    list_display = ('id','nomeLocalInstal')

class dettipoAtv(admin.ModelAdmin):  #Views
    list_display = ('id','nometipoAtv')

class detCentralTrab(admin.ModelAdmin):#Views
    list_display = ('id','nomeCentralTrab', 'den', 'des' , 'ex','ori')

class detResponsavel(admin.ModelAdmin): #Views
    list_display = ('id','nomeResponsavel', 'email_resp')

class detProduto(admin.ModelAdmin):#Views
    list_display = ('id','nomeProduto','partNumber')

class detnivelAcesso(admin.ModelAdmin):#Views
    list_display = ('id','nomeAcesso')

class detDivisao(admin.ModelAdmin): #Views
    list_display = ('id','nomeDivisao')

class detTransacaoSucata(admin.ModelAdmin):#Views
    list_display = ('id','desc','txtBreve','dataInser','user', 'trab','un','idtipoOrdemFK','idLocalFK', 'idtipoavtFK', 'idCenTrabFK', 'iddivisaoFK', 'idCentroCustoFK')

class detTransacaoProduto(admin.ModelAdmin):#Views
    list_display = ('id', 'idCentroCFK','dataIInsercao','user_Salva', 'codigo', 'idTipoMovimentoFK', 'idContaRazaoFK', 'recebedor', 'material', 'quantidade','umr','dep')

class detFotos(admin.ModelAdmin):#Views
    list_display = ('id','idProdutoFK','image')

class detUsuario(admin.ModelAdmin):#Views
    list_display = ('id', 'edv', 'senha','email','idNivelAcessFK','idUserFK')

class detHistoricoSucata(admin.ModelAdmin):#Views
    list_display = ('id', 'data', 'idTransSucataFK', 'idUsuarioFK')

class detHistoricoProduto(admin.ModelAdmin):#Views
    list_display = ('id', 'date', 'idTraProdutoFK', 'idUsuarioFK')
 
admin.site.register(centroCusto, detCentroCusto)
admin.site.register(tipoMovimento, dettipoMovimento)
admin.site.register(contaRazao, detcontaRazao)
admin.site.register(tipoOrdem, dettipoOrdem)
admin.site.register(localInstal, detlocalInstal)
admin.site.register(tipoAtv, dettipoAtv)
admin.site.register(CentralTrab, detCentralTrab)
admin.site.register(Responsavel, detResponsavel)
admin.site.register(Produto, detProduto)
admin.site.register(nivelAcesso, detnivelAcesso)
admin.site.register(Fotos, detFotos)
admin.site.register(divisao, detDivisao)
admin.site.register(TransacaoSucata, detTransacaoSucata)
admin.site.register(TransacaoProduto, detTransacaoProduto)
admin.site.register(Usuario, detUsuario)
admin.site.register(HistoricoSucata, detHistoricoSucata)
admin.site.register(HistoricoProduto, detHistoricoProduto)

