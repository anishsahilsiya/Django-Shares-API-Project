from django.urls import path
from . import views
import re
app_name = 'main_site'

urlpatterns = [
	path("", views.homepage, name = 'homepage'),
	path("signup/", views.signup_page, name = 'signup_page'),
	path("logout/", views.logout_request, name = 'logout'),
	path("login/", views.login_page, name = 'login_page'),
	path("market/", views.market_page, name = 'market_page'),
	path(r"^company/(?P<company_id>[0-9]+)$", views.company_page, name = 'company_page'),
]