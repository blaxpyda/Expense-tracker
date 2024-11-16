from django import forms

class ExpenseForm(forms.Form):
    amount = forms.CharField(required=False)
    category = forms.CharField(required=False)
