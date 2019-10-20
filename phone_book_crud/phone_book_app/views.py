from django.shortcuts import render, redirect
from phone_book_app.forms import PersonForm
from phone_book_app.models import Person
from django.views.generic import TemplateView, ListView
from django.db.models import Q


# Create your views here.

def new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = PersonForm()
    return render(request,'index.html',{'form':form})


def show(request):
    object_list = Person.objects.all()
    return render(request,"show.html",{'object_list':object_list})


def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request,'edit.html', {'person':person})


def update(request, id):
    person = Person.objects.get(id=id)
    form = PersonForm(request.POST, instance = person)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'person': person})


def destroy(request, id):
    # you can delete contact if co email or phone number
    # return list of contacts
    person = Person.objects.get(id=id)

    try:
        check_mail = Person.objects.filter(pemail='').get(id=id)
        person.delete()
    except:
        pass

    try:
        chek_num_phone = Person.objects.filter(pphone_number='').get(id=id)
        person.delete()
    except:
        pass

    return redirect("/show")


class HomePageView(TemplateView):
    template_name = 'index.html'


class SearchResultsView(ListView):
    model = Person
    template_name = 'show.html'

    def get_queryset(self):
        # search by name or last name or phone number or email
        query = self.request.GET.get('q')
        object_list = Person.objects.filter(
            Q(pfirst_name__icontains=query) |
            Q(plast_name__icontains=query) |
            Q(pphone_number__icontains=query) |
            Q(pemail__icontains=query)
            )
        return object_list
