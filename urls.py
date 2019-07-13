from django.urls import path

import views

urlpatterns = [
    path('', views.index, name="Wence Cajucom"),
    path('tech', views.tech, name="Tech"),
    path('repos', views.repos, name="Repos"),
    path('pta', views.pta, name="PTA"),
    path('jiujitsu', views.jiujitsu, name="Jiujitsu"),
]















# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)