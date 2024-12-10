from django.urls import path

from .views import index,  other_page,  BBLoginView, profile, BBLogoutView, ProfileEditView


app_name = 'main'


urlpatterns = [
    path('<str:page>', other_page, name='other'),
    path('', index, name='index'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/edit/', ProfileEditView.as_view(), name='profile_ edit'),
]

