from django import forms
from myapp.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields= [
            'student',
            'course',
            'levels',
            'order_date'
        ]
    student= forms.RadioSelect()
    order_date= forms.DateField(widget=forms.SelectDateWidget)


class InterestForm(forms.Form):
    interested = forms.ChoiceField(widget=forms.RadioSelect(),choices=[('1','Yes'),('0','No')])
    levels = forms.IntegerField(initial=1)
    comments = forms.CharField(widget=forms.Textarea, label='Additional Comments')

class loginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())