from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import RecordDisplay
from .forms import IncomeForm,ExpensesForm,DateForm

class BudgetView(View):
    def get(self,request):
        #'food_expenses','rent_utilities','entertainment_transportation','clothing','other_expenses'
        income_int = 0
        other_icome_int = 0
        food_expenses_int = 0
        rent_utilities_int = 0
        entertainment_transportation_int = 0
        clothing_int = 0
        other_expenses_int = 0
        #incomes = RecordDisplay.objects.values_list("income",flat=True)
        #for i in incomes:
        #    income_int += int(i)
        #
        #income = str(income_int)
        date_all = RecordDisplay.objects.all()
        for i in date_all:
            income_int += int(i.income)
            other_icome_int += int(i.other_income)
            food_expenses_int += int(i.food_expenses)
            rent_utilities_int += int(i.rent_utilities)
            entertainment_transportation_int += int(i.entertainment_transportation)
            clothing_int += int(i.clothing)
            other_expenses_int += int(i.other_expenses)

 
        income = str(income_int)
        other_icome = str(other_icome_int)
        sum_income = str(income_int + other_icome_int)
        
        food_expenses = str(food_expenses_int)
        rent_utilities = str(rent_utilities_int)
        entertainment_transportation = str(entertainment_transportation_int)
        clothing = str(clothing_int)
        other_expenses = str(other_expenses_int)
        sum_expenses = str(food_expenses_int + rent_utilities_int + entertainment_transportation_int + clothing_int + other_expenses_int)
        
        
        return render(request,"management/index.html",
                      {'income':income,'other_income':other_icome,'sum_income':sum_income,'food_expenses':food_expenses,
                       'rent_utilities':rent_utilities,'entertainment_transportation':entertainment_transportation,
                       'clothing':clothing,'other_expenses':other_expenses,'sum_expenses':sum_expenses})

class Add(View):
    def get(self,request):
        incomeform = IncomeForm()
        exoensesform = ExpensesForm()
        dateform = DateForm()
        return render(request,"management/budget_form.html",{'incomeform':incomeform,'exoensesform':exoensesform,'dateform':dateform})
    
    def post(self,request):
        incomeform = IncomeForm(request.POST)
        exoensesform = ExpensesForm(request.POST)
        dateform = DateForm(request.POST)
        if incomeform.is_valid() and exoensesform.is_valid() and dateform.is_valid():
            #incomeform.save()
            #exoensesform.save()
            #dateform.save()
            obj = RecordDisplay()
            obj.income = incomeform.cleaned_data['income']
            obj.other_income = incomeform.cleaned_data['other_income']
            obj.food_expenses = exoensesform.cleaned_data['food_expenses']
            obj.rent_utilities = exoensesform.cleaned_data['rent_utilities']
            obj.entertainment_transportation = exoensesform.cleaned_data['entertainment_transportation']
            obj.clothing = exoensesform.cleaned_data['clothing']
            obj.other_expenses = exoensesform.cleaned_data['other_expenses']
            obj.page_date = dateform.cleaned_data['page_date']
            obj.save()
            return redirect("management:index")
        return render(request,"management/budget_form.html",{'incomeform':incomeform,'exoensesform':exoensesform,'dateform':dateform})

class BudgetLog(View):
    def get(self,request):
        log_list = RecordDisplay.objects.order_by("page_date")
        return render(request,"management/budget_log.html",{"log_list":log_list})

class LogDetail(View):
    def get(self,request,id):
        detail = get_object_or_404(RecordDisplay, id=id)
        return render(request,"management/log_detail.html",{"detail":detail})

index = BudgetView.as_view()
budget_add = Add.as_view()
budget_log = BudgetLog.as_view()
log_detail = LogDetail.as_view()


