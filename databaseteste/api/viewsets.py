from rest_framework import viewsets, status
from rest_framework.response import Response

from databaseteste.api import serializers
from databaseteste import models

import pandas as pd


class DatabaseViewset(viewsets.ModelViewSet):
    serializer_class = serializers.DatabaseSerializer
    queryset = models.DatabaseTeste.objects.all()
    
    def list(self, request, *args, **kwargs):
        res = super().list(request=request).data
        return Response(res, status=status.HTTP_200_OK)

class DatabaseViewTotalVendas(viewsets.ModelViewSet):
    serializer_class = serializers.DatabaseSerializer
    queryset = models.DatabaseTeste.objects.all()
    
    def list(self, request, *args, **kwargs):
        data = super().list(request=request).data
        df = pd.DataFrame(data)
        df.total_vendas = df.total_vendas.astype(int)
        df = df.groupby('mes_referencia').sum('total_vendas').reset_index().to_dict('records')
        res = {"meses":[], "valores":[]}
        for d in df:
            res['meses'].append(d['mes_referencia'])
            res['valores'].append(d['total_vendas'])
        return Response(res, status=status.HTTP_200_OK)
