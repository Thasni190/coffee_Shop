
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('coffee/',include('coffee.urls'))
     path('',include('coffee.urls'))
]
