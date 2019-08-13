from django.shortcuts import render
from django.views.generic import View

from .models import Course, Video, CourseResource

# Create your views here.

class CourseList(View):
    '''课程列表'''

    def get(self, request):
        all_course = Course.objects.all()

        context = {'all_course': all_course}

        return render(request, 'course-list.html', context)