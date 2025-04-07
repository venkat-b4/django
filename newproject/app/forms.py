from django.forms import ModelForm
from.models import Student,Faculty,user

class.userLoginFrom(ModelForm):
    class.Meta:
        model = user
        fields = ['username','password','email']