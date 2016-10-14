from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from app.utils.utils import do_something


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)



def testView(request):
    do_something() # prints hello world
    template = loader.get_template('testHtml.html')
    return HttpResponse(template.render())

def testView2(request):
    do_something() # prints hello world
    template = loader.get_template('test/test2.html')
    return HttpResponse(template.render())

