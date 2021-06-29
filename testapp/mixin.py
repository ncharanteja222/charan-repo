from django.http import HttpResponse

class httpresponsemixin(object):
    def render_to_httpresponse(self,emp_data):
        return HttpResponse(emp_data,content_type='application/json')
