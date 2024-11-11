from django import forms
from django.forms import ModelForm
from .models import RecordDisplay
from django.utils import timezone

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


class DateSearchForm(forms.Form):
    """履歴検索フォーム"""

    # 年の選択肢を動的に作る
    start_year = 2010  # 家計簿の登録を始めた年
    end_year = timezone.now().year + 1  # 現在の年＋１年
    years = [(year, f'{year}年') for year in reversed(range(start_year, end_year + 1))] #reversed:逆順にする
    years.insert(0, (0, ''))  # 空白の選択を追加 insert(挿入ヵ所,挿入する値){リストの最初に(0,'')を挿入}
    YEAR_CHOICES = tuple(years)

    # 月の選択肢を動的に作る
    months = [(month, f'{month}月') for month in range(1, 13)]
    months.insert(0, (0, ''))
    MONTH_CHOICES = tuple(months)
    
    # 年の選択
    year = forms.ChoiceField(
        label='年での絞り込み',
        required=False,
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={'class': 'form'})
    )

    # 月の選択
    month = forms.ChoiceField(
        label='月での絞り込み',
        required=False,
        choices=MONTH_CHOICES,
        widget=forms.Select(attrs={'class': 'form'})
    )