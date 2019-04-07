from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [

		url('^home$', views.index, name = 'index1'),
		url('^$', views.index, name = 'index'),
		url('^xx$',views.xx,name='xx'),
		url('^patient$', views.patient, name = 'patient'),
		url('^data_virtualization$', views.data_virt, name = "data_virt"),
		url('^doctor$', views.doctor_1, name = "doctor"),
		url('^doctor_1$', views.doctor_1, name = "doctor_1"),
		url('^doctor_2$', views.doctor_display, name = "doctor_2"),
		url('^doctor_3$', views.doctor_display_1, name = "doctor_3"),

		#url('^internship/form$', views.form_save_internship, name = 'internship_form_save'),
		url('^login$', views.login, name = "login"),
	    url('^logout$', views.logout, name = "logout"),
		url('^login/auth$', views.user_auth, name = "login_auth"),
		url('^register$', views.register, name = "register"),
		url('^register/auth$', views.register_auth, name = "register_auth"),
		url('^resetpassword$', views.forgot_psw, name = "reset_psw")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT);
