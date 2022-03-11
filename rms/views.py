from django.shortcuts import render
from .models import OhrmJobTitle, HsHrEmployee
# Create your views here.


def count_hramps_employees(request):
    all_employees = HsHrEmployee.objects.count()
    all_permanent_staff = HsHrEmployee.objects.filter(emp_status=1, eeo_cat_code=2).count()
    all_casual_staff = HsHrEmployee.objects.filter(emp_status=2, eeo_cat_code=2).count()
    all_permanent_faculty = HsHrEmployee.objects.filter(emp_status=1, eeo_cat_code=1).count()
    all_casual_faculty = HsHrEmployee.objects.filter(emp_status=2, eeo_cat_code=1).count()
    all_muslim_employees = HsHrEmployee.objects.filter(nation_code=1).count()
    all_non_muslim_employees = HsHrEmployee.objects.filter(nation_code=2).count()
    all_muslim_permanent = HsHrEmployee.objects.filter(nation_code=1, emp_status=1).count()
    all_non_muslim_permanent = HsHrEmployee.objects.filter(nation_code=2, emp_status=1).count()
    all_muslim_casual = HsHrEmployee.objects.filter(nation_code=1, emp_status=2).count()
    all_non_muslim_casual = HsHrEmployee.objects.filter(nation_code=2, emp_status=2).count()

    context = {
        'all_employees': all_employees,
        'all_permanent_staff': all_permanent_staff,
        'all_casual_staff': all_casual_staff,
        'all_permanent_faculty': all_permanent_faculty,
        'all_casual_faculty': all_casual_faculty,
        'all_muslim_employees': all_muslim_employees,
        'all_non_muslim_employees': all_non_muslim_employees,
        'all_muslim_permanent': all_muslim_permanent,
        'all_non_muslim_permanent': all_non_muslim_permanent,
        'all_muslim_casual': all_muslim_casual,
        'all_non_muslim_casual': all_non_muslim_casual
    }
    return render(request, 'index.html', context)
