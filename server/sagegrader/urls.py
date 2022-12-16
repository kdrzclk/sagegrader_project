from django.urls import path
from .views import InstitutionView, InstitutionViewRUD, UserView, UserViewRUD

urlpatterns = [
    path('institutions/', InstitutionView.as_view()),
    path('institutions/<uuid:pk>', InstitutionViewRUD.as_view()),

    path('user/', UserView.as_view()),
    path('user/<uuid:pk>', UserViewRUD.as_view()),


]