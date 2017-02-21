from django.conf.urls import url, include
# from . import views
from rest_framework import routers
from .views import index, ProductViewSet



router = routers.DefaultRouter()
router.register(r'api', ProductViewSet)



urlpatterns = [
    url(r'^myshop/', index),
    url(r'^', include(router.urls))
]