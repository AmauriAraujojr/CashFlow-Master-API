from django.urls import path
from .views import CaixaView, CaixaDetailView
from receitas.views import ReceitasView, ReceitasAllView, ReceitasDetailView
from despesas.views import DespesaView, DespesasAllView, DespesasDetailView


urlpatterns=[

    path("caixa/", CaixaView.as_view()),
    path("receitas/", ReceitasAllView.as_view()),
    path("caixa/<int:pk>/receitas/", ReceitasView.as_view()),
    path("caixa/<int:pk>/despesas/", DespesaView.as_view()),
    path("despesas/", DespesasAllView.as_view()),
    path("despesas/<int:pk>/", DespesasDetailView.as_view()),
    path("receitas/<int:pk>/", ReceitasDetailView.as_view()),
    path("caixa/<int:pk>/", CaixaDetailView.as_view()),


]