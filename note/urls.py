from django.urls import re_path, include
from rest_framework import routers

from .views import ListNote


router = routers.SimpleRouter()
router.register(r'note', ListNote)

urlpatterns = [
    re_path('', include(router.urls))
]