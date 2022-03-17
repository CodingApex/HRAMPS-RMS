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
    faye_employees = HsHrEmployee.objects.filter(work_station__in=[101, 102, 103, 107, 109, 111, 307, 320, 370]).count()
    jomari_employees = HsHrEmployee.objects.filter(work_station__in=[105, 201, 203, 301, 330]).count()
    palor_employees = HsHrEmployee.objects.filter(work_station__in=[108, 304, 305, 311, 313, 331, 354]).count()
    grace_employees = HsHrEmployee.objects.filter(work_station__in=[202, 302, 340, 351, 353, 370, 380, 381]).count()
    faye_perma_emp = HsHrEmployee.objects.filter(work_station__in=[101, 102, 103, 107, 109, 111, 307, 320, 370], emp_status=1, eeo_cat_code=2).count()
    faye_cas_emp = HsHrEmployee.objects.filter(work_station__in=[101, 102, 103, 107, 109, 111, 307, 320, 370], emp_status=2, eeo_cat_code=2).count()
    jomari_perma_emp = HsHrEmployee.objects.filter(work_station__in=[105, 201, 203, 301, 330], emp_status=1, eeo_cat_code=2).count()
    jomari_cas_emp = HsHrEmployee.objects.filter(work_station__in=[105, 201, 203, 301, 330], emp_status=2, eeo_cat_code=2).count()
    palor_perma_emp = HsHrEmployee.objects.filter(work_station__in=[108, 304, 305, 311, 313, 331, 354], emp_status=1, eeo_cat_code=2).count()
    palor_cas_emp = HsHrEmployee.objects.filter(work_station__in=[108, 304, 305, 311, 313, 331, 354], emp_status=2, eeo_cat_code=2).count()
    grace_perma_emp = HsHrEmployee.objects.filter(work_station__in=[202, 302, 340, 351, 353, 370, 380, 381], emp_status=1, eeo_cat_code=2).count()
    grace_cas_emp = HsHrEmployee.objects.filter(work_station__in=[202, 302, 340, 351, 353, 370, 380, 381], emp_status=2, eeo_cat_code=2).count()

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
        'all_non_muslim_casual': all_non_muslim_casual,
        'faye_employees': faye_employees,
        'jomari_employees': jomari_employees,
        'palor_employees': palor_employees,
        'grace_employees': grace_employees,
        'faye_oc_perma_staff': faye_perma_emp,
        'faye_oc_cas_staff': faye_cas_emp,
        'jomari_perma_emp': jomari_perma_emp,
        'jomari_cas_emp': jomari_cas_emp,
        'palor_perma_emp': palor_perma_emp,
        'palor_cas_emp': palor_cas_emp,
        'grace_perma_emp': grace_perma_emp,
        'grace_cas_emp': grace_cas_emp
    }
    return render(request, 'index.html', context)
