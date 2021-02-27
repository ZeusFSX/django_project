from rest_framework import routers
from .api import ArticleViewSet, EntityViewSet


router = routers.DefaultRouter()
router.register('api/article', ArticleViewSet, 'article')
router.register('api/entity', EntityViewSet, 'entity')

urlpatterns = router.urls
