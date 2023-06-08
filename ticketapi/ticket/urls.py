from django.urls import path
from . import views

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("ticket-list/", views.ticketList, name="ticket-list"),
    path("ticket-detail/<str:pk>/", views.ticketDetail, name="ticket-Detail"),
    path("ticket-update/<str:pk>/", views.ticketUpdate, name="ticket-update"),
    path("ticket-create/", views.ticketCreate, name="ticket-Create"),
    path("ticket-delete/<str:pk>/", views.ticketDelete, name="ticket-delete"),
    path("ticket-reserve/<str:pk>/", views.ticketReserve, name="ticket-reserve"),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
