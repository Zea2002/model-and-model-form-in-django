from django.shortcuts import render
from app1.forms import StudntForm

# Create your views here.
def home(request):
    if request.method== 'POST':
        form=StudntForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        
    else:
        form=StudntForm()
    return render(request,'home.html',{'form':form})


