from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
# def index(responce, name):
#     ls = ToDoList.objects.get(name=name)
#     item = ls.item_set.get(id=1)
#     return HttpResponse("<h1>%s</h1><br><p>%s</p>" %(ls.name, str(item.text)))

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():

        if response.method == "POST":
            # {"save": ["name"], "c1": ["clicked"]}
            print(response.POST)
            if response.POST.get("save"): # name of the form
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) >2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid")    

        return render(response, "main/view.html", {})
    else:
        render()

    

    

def v1(response):
    return HttpResponse("View 1")

def home(response):
    return render(response, "main/home.html", {"name": "test"})

def create(response):
    if response.method == "POST":
        print("post method")
        form = CreateNewList(response.POST)

        # this is needed because we import from forms
        if form.is_valid():
            print("method is valid")
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
            return HttpResponseRedirect("/%i" %t.id)    

        
    
    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})

def view(response):
    return render(response, "main/view.html", {})
    

# use post for secret info or change in database
# get is just to retrieve info
