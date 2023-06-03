"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myshop import views
from rest_framework_jwt.views import obtain_jwt_token
from myshop.models import Real_estate

from django.conf import settings
from django.conf.urls.static import static   #추가

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/realestate/$', views.RS_ViewSet.as_view(), name="RealEstate"),
    url(r'^api/category/$', views.CateViewSet.as_view(), name="Category"),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api/realestate/landmark/$', views.LandMark.as_view(), name="Landmark"),
    url(r'^api/realestate/commercial/$', views.Commercial.as_view(), name="Commercial"),
    url(r'^api/realestate/residential/$', views.Residential.as_view(), name="Residential"),
    url(r'^api/realestate/(?P<id>\d+)/$', views.Detail.as_view(), name="Detail"),  
    url(r'^api/signup/$', views.Signup.as_view(), name="signup"),
    url(r'^api/realestate/(?P<id>\d+)/like/$', views.Recommand.as_view(), name="Like"),
    # url(r'^api/message/recent/$', views.RecentMessage.as_view(), name="RecentMessage"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)   #추가
