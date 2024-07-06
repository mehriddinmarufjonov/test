from django.urls import path, include
from .views import (HeaderView, CategoryView, ToursView, ArticleView, NetworksView, CommentView, FooterView)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


from rest_framework import routers


router = routers.SimpleRouter()
router.register('header', HeaderView)
router.register('category', CategoryView)
router.register('tours', ToursView)
router.register('article', ArticleView)
router.register('comment', CommentView)
router.register('footer', FooterView)


urlpatterns = [
    path('travel/', include(router.urls)),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]