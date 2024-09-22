from django.forms import ModelForm
from .models import RecordDisplay

class IncomeForm(ModelForm):
    class Meta:
        model = RecordDisplay
        fields = ['income','other_income']

class ExpensesForm(ModelForm):
    class Meta:
        model = RecordDisplay
        fields = ['food_expenses','rent_utilities','entertainment_transportation','clothing','other_expenses']
        

class DateForm(ModelForm):
    class Meta:
        model = RecordDisplay
        fields = ['page_date']