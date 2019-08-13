from django.conf.urls import url


from . import views as v


urlpatterns = [
    url(r'^list/$', v.OrgList.as_view(), name='list'),
    url(r'^teacher_list/$', v.TeacherView.as_view(), name='teacher_list'),

]