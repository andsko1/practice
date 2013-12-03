from django.db import models
from django import forms

class SearchBookForm(forms.Form):
	book_name = forms.CharField(max_length=128, required=False)
	ISBN = forms.CharField(max_length=12, required=False)
	
	def save(self):
	        data = self.cleaned_data	
	
# Create your models here.
