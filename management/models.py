from django.db import models
import uuid

class RecordDisplay(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4,editable=False,verbose_name="ID"
    )
    income = models.IntegerField(default=0,null=True,blank=True,verbose_name="収入")
    other_income = models.IntegerField(default=0,null=True,blank=True,verbose_name="その他の収入")
    food_expenses = models.IntegerField(default=0,null=True,blank=True,verbose_name="食費")
    rent_utilities = models.IntegerField(default=0,null=True,blank=True,verbose_name="家賃＋光熱費")
    entertainment_transportation = models.IntegerField(default=0,null=True,blank=True,verbose_name="娯楽費＋交通費")
    clothing = models.IntegerField(default=0,null=True,blank=True,verbose_name="衣服")
    other_expenses = models.IntegerField(default=0,null=True,blank=True,verbose_name="その他の支出")
    page_date = models.DateField(null=True,verbose_name="日付")

    
    
    def __str__(self):
        return str(self.page_date)