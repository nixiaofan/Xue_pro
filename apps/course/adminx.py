import xadmin
from .models import *


xadmin.site.register(Course)
xadmin.site.register(Lesson)
xadmin.site.register(Video)
xadmin.site.register(CourseResource)



