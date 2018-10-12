from django.shortcuts import render
from .forms import ProfileForm


def display(request):
    print('I am in view of handling the form')
    if request.method=='POST':
        form = ProfileForm(data=request.POST)
        print('%%%%%%%%%%%%%',form)
        if form.is_valid():
           print('I am in validation of form')
           a = form.save()
           print(a)
    else:
        form = ProfileForm()
    return render(request, 'index.html', {'form':form})
