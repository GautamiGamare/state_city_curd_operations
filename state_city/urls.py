from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static
from state_city import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('state/',views.state,name='state'),
    path('city/',views.city,name='city'),
    path('save_state/',views.save_state,name='save_state'),
    path('update_state/',views.update_state,name='update_state'),
    path('updt_state/',views.updt_state,name='updt_state'),
    path('delete_state/',views.delete_state,name='delete_state'),

    path('save_city/',views.save_city,name='save_city'),
    path('update_city/',views.update_city,name='update_city'),
    path('updt_city/',views.updt_city,name='updt_city'),
    path('delete_city/',views.delete_city,name='delete_city'),

    path('add_cuisine/',views.add_cuisine,name='add_cuisine'),
    path('save_cuisine/',views.save_cuisine,name='save_cuisine'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)