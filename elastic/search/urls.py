from django.urls import path
from . import views

urlpatterns = [
    path(
        "document/", views.VerDocumento.as_view()
    ),  # URL para busqueda y subir documento
    path("document/<int:id>/", views.ModificarDocumento.as_view()),
]
