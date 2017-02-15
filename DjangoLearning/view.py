from django.http import HttpResponse, Http404
import datetime
#from django.template import Template, Context
#from django.template.loader import get_template
from django.shortcuts import render_to_response

'''
A view is a function in Django which needs to satisfy the following two conditions:
1. input param is a HttpRequest obj;
2. output param is a HttpResponse obj.
'''
def res_hello_view_request(request):
    return HttpResponse('Hello World!')

def res_date_view_request(request, month='', day=''):
    try:
        assert(isinstance(month, str))
        assert(isinstance(day, str))
    except AssertionError:
        raise Http404()

    #t = get_template('date.html')
    #html = t.render(Context({'month':month, 'day':day}))
    #return HttpResponse(html)
    return render_to_response('date.html', locals())

def res_datetime_view_request(request, offset):
    try:
        offset = int(offset)
    except TypeError:
        raise Http404()
    now = datetime.datetime.now()
    dt = now + datetime.timedelta(hours=offset)
    html = "<html><body> It is now %s. And in %d hours, it will be %s</body></html>" % (now, offset, dt)
    return HttpResponse(html)
