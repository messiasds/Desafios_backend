from django.urls import path
from .views import RedirecionarURL
from .views import EncurtadorURL

urlpatterns = [
    path('', EncurtadorURL.as_view()),
    path('<str:url_curta>', RedirecionarURL.as_view())
]