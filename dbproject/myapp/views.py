from django.shortcuts import render, redirect  
from myapp.forms import ThesisForm  
from myapp.models import Thesis  
 
def addnew(request):  
    if request.method == "POST":  
        form = ThesisForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = ThesisForm()  
    return render(request,'index.html',{'form':form})  
 
def index(request):  
    thesiss = Thesis.objects.all()  
    return render(request,"show.html",{'thesiss':thesiss})  
 
def edit(request, id):  
    thesis = Thesis.objects.get(id=id)  
    return render(request,'edit.html', {'thesis':thesis})  
 
def update(request, id):
    thesis = Thesis.objects.get(id=id)
    if request.method == 'POST':
        form = ThesisForm(request.POST, instance=thesis)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ThesisForm(instance=thesis)
    return render(request, 'edit.html', {'form': form, 'thesis': thesis})

     
def destroy(request, id):  
    thesis = Thesis.objects.get(id=id)  
    thesis.delete()  
    return redirect("/")  