from django.conf.urls import url


from . import views as v


urlpatterns = [
    url(r'^course_list/$', v.CourseList.as_view(), name='course_list'),


]