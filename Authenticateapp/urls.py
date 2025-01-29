from django.urls import path
from Authenticateapp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.user_logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('update/',views.Update,name='update')
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)