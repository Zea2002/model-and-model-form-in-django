from django import forms
from app1.models import StudentModel

class StudntForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : "Student Roll",
            'age' : "Student age",
            'father_name' : "Student father_name",
        }

        widgets  = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : "Write your full name",
            'roll' : "Write your roll please",
            'age' : "Write your age",
            'father_name' : "Write your father name please",
        }
        
        error_messages = {
            'name' : {'required' : 'Your name is required'},
            'roll' : {'required' : 'Your roll is required'},
        }
