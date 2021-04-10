from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from swapper import load_model
 
from .serializers import CaSerializer, CertSerializer
 

Ca = load_model('pki', 'Ca')
Cert = load_model('pki', 'Cert')


class CaListView(ListCreateAPIView):
   serializer_class = CaSerializer
   queryset = Ca.objects.all()


class CaDetailView(RetrieveUpdateDestroyAPIView):
   serializer_class = CaSerializer
   queryset = Ca.objects.all()


class CertListView(ListCreateAPIView):
   serializer_class = CertSerializer
   queryset = Cert.objects.all()


class CertDetailView(RetrieveUpdateDestroyAPIView):
   serializer_class = CertSerializer
   queryset = Cert.objects.all()
 
ca_list = CaListView.as_view()
ca_detail = CaDetailView.as_view()
cert_list = CertListView.as_view()
cert_detail = CertDetailView.as_view()

# TODO: Add download views for ca and cert