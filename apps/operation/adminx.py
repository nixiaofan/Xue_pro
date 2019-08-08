import xadmin
from .models import *


xadmin.site.register(UserAsk)
xadmin.site.register(CourseComment)
xadmin.site.register(UserFavorite)
xadmin.site.register(UserMessage)
xadmin.site.register(UserCourse)


