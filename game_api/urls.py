from .views import GameList
from rest_framework.routers import DefaultRouter


app_name = 'game_api'

router = DefaultRouter()
router.register('', GameList, basename='game')
urlpatterns = router.urls