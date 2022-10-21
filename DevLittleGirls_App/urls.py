from .views import site_list
from django.urls import path, re_path

app_name = 'DevLittleGirls_App'

urlpatterns = [
    path('', site_list, name='AlunoList_teste'),
]
