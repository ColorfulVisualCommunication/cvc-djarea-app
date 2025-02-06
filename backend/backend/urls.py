from django.contrib import admin
#-----------add----------------
from django.urls import path, include, re_path
from django.views.generic import TemplateView
#-----------end----------------

urlpatterns = [
    path('admin/', admin.site.urls),
    #-----------add----------------
    path('api/', include('api.urls')),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')), # for frontend
    #-----------end----------------
]
