from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, LogoutView, UserViewSet, RegisterView, InactiveUsersViewSet


app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'inactive-user', InactiveUsersViewSet, basename='inactive-user')


urlpatterns = [
    path('', include(router.urls)),


    # Authentication URLs
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

]