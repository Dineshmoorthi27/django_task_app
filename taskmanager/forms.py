from django import forms
from django.forms import modelformset_factory
from taskmanager.models import Task, Screenshot

class TaskForm(forms.ModelForm):
    screenshot = forms.ImageField(required=False) 
    class Meta:
        model = Task
        fields = "__all__"
class EditTaskForm(forms.ModelForm):
    task_id = forms.CharField(disabled=True)
    assigned_by = forms.CharField(disabled=True)
    screenshot = forms.ImageField(required=False) 
    class Meta:
        model = Task
        fields = ['task_id','task_name','assigned_by','assigned_to','description','status','priority','screenshot']
class DescriptionForm(forms.ModelForm):
    description = forms.CharField(disabled=True)
    class Meta:
        model = Task
        fields = ['description']

