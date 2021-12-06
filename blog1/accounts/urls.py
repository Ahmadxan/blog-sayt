from django.urls import path
from accounts.views import SignUp, login_page, home_page, about_page, contact_page, add_blog, blog_page, logout_page

urlpatterns = [
    path('accounts/signup/', SignUp.as_view(), name='signup'),
    path('accounts/login/', login_page, name='login'),
    path('accounts/logout/', logout_page, name='logout'),
    path('', home_page, name='home-page'),
    path('about/', about_page, name='about-page'),
    path('contact/', contact_page, name='contact-page'),
]