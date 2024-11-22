from django.contrib import admin
from django.urls import path, include
from tasks import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),  # This adds the homepage URL
    path('tasks/', include('tasks.urls')),  # Including the tasks app's URLs
]
