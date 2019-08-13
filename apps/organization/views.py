from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CityDict, CourseOrg, Teacher

# Create your views here.
class OrgList(View):
    '''课程机构功能'''
    def get(self, request):
        #课程机构和城市
        all_orgs = CourseOrg.objects.all()
        all_cities = CityDict.objects.all()
        org_numbers = all_orgs.count()

        city_id = request.GET.get('city', '')
        category = request.GET.get('category', '')

        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        if category:
            all_orgs = all_orgs.filter(category=category)



        #分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        #筛选功能

        context = {'all_orgs': orgs,
                   'all_cities': all_cities,
                   'org_numbers': org_numbers,
                   'city_id': city_id,
                   'category': category,
                   }

        return render(request, 'org-list.html', context)





