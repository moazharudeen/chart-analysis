from django import forms

chartcoices =(
    ("column2d", "column2d"),
    ("column3d", "column3d"),
)
  
class charttypeform(forms.Form):
    chart_title = forms.ChoiceField(choices = chartcoices)
   

class column2d(forms.Form):
    chart_title = forms.CharField(max_length=255)
    chart_sub_title = forms.CharField(max_length=255)
    x_axis_name = forms.CharField(max_length=255)
    y_axis_name = forms.CharField(max_length=255)
    number_suffix = forms.CharField(max_length=255)
    labels = forms.CharField(max_length=255, required=True)
    values =  forms.CharField(max_length=255, required=True)
