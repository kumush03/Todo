"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main.views import main,create,test,delete,edit,tasks,error
 
urlpatterns = [ 
    path('', main, name='main'), 
    path('create/',create,name='create'),
    path('test/<int:id>',test,name='test'),
    path('delete/<int:id>',delete,name='delete'),
    path('edit/<int:id>',edit,name='edit'),
    path('tasks/',tasks,name='tasks'),
    path('error/',error,name='error')

    
]










# from django.contrib import admin
# from django.urls import path
# from main.views import home,main,sendMessage
# from django.conf.urls.static import static
# from mysite.settings import STATIC_URL,STATIC_ROOT,MEDIA_ROOT,MEDIA_URL

# urlpatterns = [ 
#     path('admin/', admin.site.urls),
#     path('',home,name='home'),
#     path('main',main,name='main'),
#     path('sendMessage/',sendMessage,name='sendMessage')
# ]
# urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)
# urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)