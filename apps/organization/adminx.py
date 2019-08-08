import xadmin
from .models import *


xadmin.site.register(CityDict)
xadmin.site.register(CourseOrg)
xadmin.site.register(Teacher)


