from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
urlpatterns = [
    url(r'^visualize/', views.visualize),
]

# Add these for old code

    # url(r'^netcval/', views.netcval),
    # url(r'^netcvol/', views.netcvol),
    # url(r'^upi/', views.upi),
    # url(r'^nfs/', views.nfs),
    # url(r'^pos/', views.pos),