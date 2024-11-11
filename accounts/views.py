from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login,get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render,resolve_url
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import SignUpForm,UserUpdateForm
from .models import User
 

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        self.object = user
        return redirect('management:index')

#自分しかあくせすできないようにするMixin
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True
    
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk']

class MyPage(OnlyYouMixin,generic.DetailView):
    #date_all = RecordDisplay.objects.all()
    #for i in date_all:
    #    income_int += int(i.income)
    #    other_icome_int += int(i.other_income)
    #    food_expenses_int += int(i.food_expenses)
    #    rent_utilities_int += int(i.rent_utilities)
    #    entertainment_transportation_int += int(i.entertainment_transportation)
    #    clothing_int += int(i.clothing)
    #    other_expenses_int += int(i.other_expenses)
    model = User
    template_name = 'accounts/my_page.html'

class UserUpdate():
    pass
    
signup = SignUpView.as_view()
my_page = MyPage.as_view()