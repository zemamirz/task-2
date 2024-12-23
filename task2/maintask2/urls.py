from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка доступна через /task2/admin/
    path('accounts/', include('django.contrib.auth.urls')),  # Авторизация через /task2/accounts/
    path('', include('blogs.urls')),  # Всё приложение через /task2/
]