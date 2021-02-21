from rest_framework import routers
from .api import ArticleViewSet


router = routers.DefaultRouter()
router.register('api/article', ArticleViewSet, 'article')

urlpatterns = router.urls
