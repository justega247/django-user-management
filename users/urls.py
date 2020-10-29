# from django.urls import path, include
# from .views import dashboard, register
#
# urlpatterns = [
#     path("accounts/", include("django.contrib.auth.urls")),
#     path("dashboard/", dashboard, name="dashboard"),
#     path("register/", register, name="register"),
#     path("oauth/", include("social_django.urls")),
# ]

from django.conf.urls import include, url
from .views import dashboard, register

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^oauth/", include("social_django.urls")),
    url(r"^register/", register, name="register"),
]
