from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from app1.forms import PersonForm
from app1.models import Person
from django.views import View


def article(request, year):
    content = 'the year is %s' % year
    return HttpResponse(content)


def person_detail(request, pk):
    try:
        p = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        raise Http404('Person Does Not Exist')
    return render(request, 'person_detail.html', {'person': p})


def get_name(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            return  HttpResponse(first_name + ' ' + last_name)
        else:
            return HttpResponseRedirect('/error/')
    return render(request, 'name.html', {'form': PersonForm()})


# 基于类的视图，替代get_name函数视图
class PersonFormView(View):
    form_class = PersonForm
    initial = {'key': 'value'}
    template_name = 'name.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class(initial=self.initial)})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            return HttpResponse(first_name + ' ' + last_name)
        return render(request, self.template_name, {'form': form})
