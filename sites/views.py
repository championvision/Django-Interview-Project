from django.shortcuts import render
from django.db.models import Avg
from django.shortcuts import render_to_response
from sites.models import Demosite, Abcsite, Xyzsite


def sites(request):
    # For sites.html
    return render_to_response('sites/sites.html')


def demosite(request):
    # For Demosite.html
    demosites = Demosite.objects.all()
    return render(request, 'sites/1.html', {'demosites': demosites})


def abcsite(request):
    # For Abcsite.html
    abcsites = Abcsite.objects.all()
    return render(request, 'sites/2.html', {'abcsites': abcsites})


def xyzsite(request):
    # For Xyzsite.html
    xyzsites = Xyzsite.objects.all()
    return render(request, 'sites/3.html', {'xyzsites': xyzsites})


def summary(request):
    # For example Demosite.objects.values('a_value') returns
    # a queryset that consists of dictionaries of one
    # key-value pair for a_values of Demosite model.qs_sum take
    # queryset as input parameter, and sums each value in each
    # dictionary in the queryset. Owing to qs_sum method, we can
    # sum all a_values of Demosite model.qs_sum returns float
    demo_a_values = Demosite.objects.values('a_value')
    sum_demo_a_values = qs_sum(demo_a_values)
    demo_b_values = Demosite.objects.values('b_value')
    sum_demo_b_values = qs_sum(demo_b_values)
    abc_a_values = Abcsite.objects.values('a_value')
    sum_abc_a_values = qs_sum(abc_a_values)
    abc_b_values = Abcsite.objects.values('b_value')
    sum_abc_b_values = qs_sum(abc_b_values)
    xyz_a_values = Xyzsite.objects.values('a_value')
    sum_xyz_a_values = qs_sum(xyz_a_values)
    xyz_b_values = Xyzsite.objects.values('b_value')
    sum_xyz_b_values = qs_sum(xyz_b_values)
    return render(request, 'sites/summary.html',
                 {'sum_demo_a_values': sum_demo_a_values,
                 'sum_demo_b_values': sum_demo_b_values,
                 'sum_abc_a_values': sum_abc_a_values,
                 'sum_abc_b_values': sum_abc_b_values,
                 'sum_xyz_a_values': sum_xyz_a_values,
                 'sum_xyz_b_values': sum_xyz_b_values})


def qs_sum(qs):
    # qs_sum take queryset as input parameter, and sums each value in each
    # dictionary in the queryset. Owing to qs_sum method, we can
    # sum all a_values of Demosite model. qs_sum returns float.
    result = 0.0
    for d in qs:
        for v in d.values():
            result = result + v
    return result


def summary_average(request):
    avg_demo_a_values = Demosite.objects.all().aggregate(Avg('a_value'))
    avg_demo_b_values = Demosite.objects.all().aggregate(Avg('b_value'))
    avg_abc_a_values = Abcsite.objects.all().aggregate(Avg('a_value'))
    avg_abc_b_values = Abcsite.objects.all().aggregate(Avg('b_value'))
    avg_xyz_a_values = Xyzsite.objects.all().aggregate(Avg('a_value'))
    avg_xyz_b_values = Xyzsite.objects.all().aggregate(Avg('b_value'))
    return render_to_response('sites/summary-average.html',
                             {'avg_demo_a_values': avg_demo_a_values,
                             'avg_demo_b_values': avg_demo_b_values,
                             'avg_abc_a_values': avg_abc_a_values,
                             'avg_abc_b_values': avg_abc_b_values,
                             'avg_xyz_a_values': avg_xyz_a_values,
                             'avg_xyz_b_values': avg_xyz_b_values})
