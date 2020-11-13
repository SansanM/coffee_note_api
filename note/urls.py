from django.urls import re_path, include
from rest_framework import routers

from .views import ListNote,GetUser,ListUser


router = routers.SimpleRouter()
router.register(r'note', ListNote)
router.register(r'users', GetUser,basename="note") 
router.register(r'usersList', ListUser,basename="note") 
urlpatterns = [
    re_path('', include(router.urls))
]