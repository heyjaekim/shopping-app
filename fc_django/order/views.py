from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm

# Create your views here.

class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

