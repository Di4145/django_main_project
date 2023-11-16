from django.urls import path, include
from rest_framework import routers
from api.views import ArticleModelViewSet

router = routers.DefaultRouter()
router.register('article', ArticleModelViewSet)

urlpatterns = [
    path('', include(router.urls)),

]