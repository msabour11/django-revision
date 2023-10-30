from django.urls import reverse,path,include

urlpatterns=[
    path('',include('django.contrib.auth.urls'))
]