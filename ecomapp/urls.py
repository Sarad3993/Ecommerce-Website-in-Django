from django.urls import path
from .views import * 
# esari sabai views import garnu bhanda chine chine garnu is best practice 

app_name = 'ecomapp'
# aba yo app name lai main urls (project ko urls ) ma gayera include garnu parxa 

# no need to make separate urlpatterns for function based views and class based views ; eutai bhitra include garna milxa majale 

urlpatterns = [ 
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>',ItemView.as_view(),name='product'),
    path('contact', contact, name='contact'),

]
