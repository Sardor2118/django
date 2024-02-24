from django.contrib import admin
from django.urls import path
from products.views import home_page, products_page, MyLoginView, logout_view
from django.conf import settings
from django.conf.urls.static import static


class MyLogoutView:
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('products/', products_page),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

