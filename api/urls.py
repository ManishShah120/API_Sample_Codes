from django.urls import path
from . import views as api_views

urlpatterns = [
    path('ca/', api_views.ca_list, name='api_ca_list'),
    path('ca/<str:pk>', api_views.ca_detail, name='api_ca_detail'),
    path('cert/', api_views.cert_list, name='api_cert_list'),
    path('cert/<str:pk>', api_views.cert_detail, name='api_cert_detail'),
]

# TODO: Add the endpoints to allow downloading of the `.crl` files
