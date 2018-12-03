from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.views import View

# Create your views here.


def check_if_int(number):
    try:
        return int(number)
    except Exception:
        return None



class AddPerson(View):
    def get(self, request):
        return render(request, "my_contacts/add_person.html")

    def post(self, request):
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        description = request.POST.get("description")
        new_person= Person.objects.create(name=name, surname=surname, description=description)
        return redirect("show/%s" % new_person.id)


class EditPerson(View):
    def get(self, request, id):
        id = check_if_int(id)
        person = Person.objects.get(pk=id)
        context = {'person': person, 'mails': person.mail_set.all(), 'telephons': person.telephon_set.all(), 'groups': Group.objects.filter(person=id)}
        return render(request, "my_contacts/edit_person.html", context)

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        person.name = request.POST.get("name")
        person.surname = request.POST.get("surname")
        person.description = request.POST.get("description")
        person.save()
        return redirect("../show/%s" % id)


class DeletePerson(View):
    def get(self,request, id):
        id = check_if_int(id)
        context = {'person': Person.objects.get(pk=id)}
        return render(request, "my_contacts/delete_person.html", context)

    def post(self, request, id):
        if request.POST.get('decision') == 'yes':
            person = Person.objects.get(pk=id)
            person.delete()
        return redirect("/")


class ShowPerson(View):
    def get(self, request, id):
        id = check_if_int(id)
        person = Person.objects.get(pk=id)
        context = {'person': person, 'mails': person.mail_set.all(), 'telephons': person.telephon_set.all(), 'groups': Group.objects.filter(person=id)}
        return render(request, "my_contacts/show_person.html", context)
    def post(self, request, id):
        person = Person.objects.get(pk=id)
        return redirect("../modify/%s" % person.id)


class ShowAllPerson(View):
    def get(self, request):
        persons = Person.objects.all().order_by("surname")
        context = {'persons':persons}
        return render(request, "my_contacts/show_all_person.html", context)


class AddAddress(View):
    def get(self, request, id):
        id = check_if_int(id)
        person = Person.objects.get(pk=id)
        context = {'person': person}
        return render(request, "my_contacts/add_address.html", context)

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        city = request.POST.get('city')
        street = request.POST.get('street')
        house_number = request.POST.get('house_number')
        apartment_number = request.POST.get('apartment_number')
        if Address.objects.filter(city= city, street=street, house_number=house_number, apartment_number=apartment_number).exists():
            person.address = Address.objects.get(city= city, street=street, house_number=house_number, apartment_number=apartment_number)
        else:
            new_address = Address.objects.create(city=city, street=street, house_number=house_number, apartment_number=apartment_number)
            person.address = new_address
        person.save()
        return redirect("../show/%s" % id)


class DeleteAddress(View):
    def get(self, request, id):
        id = check_if_int(id)
        person = Person.objects.get(pk=id)
        adres_id = person.address.id
        context = {'address': Address.objects.get(pk=adres_id)}
        print(context)
        return render(request, "my_contacts/delete_address.html", context)

    def post(self, request, id):
        if request.POST.get('decision') == 'yes':
            person = Person.objects.get(pk=id)
            adres_id = person.address.id
            address = Address.objects.get(pk=adres_id)
            address.person_set.remove(person)
        return redirect("../show/%s" % id)


class AddTelephon(View):
    def get(self, request, id):
        id = check_if_int(id)
        person = Person.objects.get(pk=id)
        context = {'person': person}
        return render(request, "my_contacts/add_telephon.html", context)

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        number = request.POST.get('number')
        type_number = request.POST.get('type_number')
        Telephon.objects.create(number=number, type_number=type_number, person=person)
        return redirect("../show/%s" % id)



class DeleteTelephon(View):
    def get(self, request, id):
        id = check_if_int(id)
        person = Person.objects.get(pk=id)
        context = {'telephons': person.telephon_set.all()}
        print(context)
        return render(request, "my_contacts/delete_telephon.html", context)

    def post(self, request, id):
        if request.POST.get('decision') == 'yes':
            id_number = request.POST.get('number')
            telephon = Telephon.objects.get(pk=id_number)
            telephon.delete()
        return redirect("../show/%s" % id)



class AddMail(View):
    def get(self, request, id):
        id = check_if_int(id)
        person = Person.objects.get(pk=id)
        context = {'person': person}
        return render(request, "my_contacts/add_mail.html", context)

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        mail = request.POST.get('mail')
        mail_type = request.POST.get('mail_type')
        Mail.objects.create(mail=mail, mail_type=mail_type, person=person)
        return redirect("../show/%s" % id)


class DeleteMail(View):
    def get(self, request, id):
        id = check_if_int(id)
        person = Person.objects.get(pk=id)
        context = {'mails': person.mail_set.all()}
        print(context)
        return render(request, "my_contacts/delete_mail.html", context)

    def post(self, request, id):
        if request.POST.get('decision') == 'yes':
            id_mail = request.POST.get('mail')
            mail = Mail.objects.get(pk=id_mail)
            mail.delete()
        return redirect("../show/%s" % id)


class ShowAllGroups(View):
    def get(self, request):
        groups = Group.objects.all()
        context = {'groups': groups}
        return render(request, "my_contacts/show_all_groups.html", context)


class AddGroup(View):
    def get(self, request):
        return render(request, "my_contacts/add_group.html")

    def post(self, request):
        name = request.POST.get("name")
        new_group= Group.objects.create(name=name)
        return redirect("../group/%s" % new_group.id)


class GroupDetails(View):
    def get(self, request, id):
        id = check_if_int(id)
        group = Group.objects.get(pk=id)
        context = {'group': group, 'persons': group.person.all()}
        return render(request, "my_contacts/group_details.html", context)

    def post(self, request, id):
        return redirect("%s/addMembers" % id)


class AddMembersToGroup(View):
    def get(self, request, id):
        group = Group.objects.get(pk=id)
        context ={'group': group, 'persons': group.person.all(), 'all_person': Person.objects.all()}
        return render(request, "my_contacts/add_members.html", context)

    def post(self, request, id):
        try:
            member = str(request.POST.get("member"))
            group = Group.objects.get(pk=id)
            group.person.add(member)
            return redirect("../%s" % id)
        except:
            return HttpResponse("Ta osoba już jest zapisana do tej grupy")


class Search(View):
    def get(self, request, id):
        context= {'group': Group.objects.get(pk=id)}
        return render(request, "my_contacts/search.html", context)

    def post(self, request, id):
        group = Group.objects.get(pk=id)
        search = request.POST.get('search')
        try:
            if group.person.filter(name = search):
                result = group.person.filter(name=search)
            elif group.person.filter(surname = search):
                result = group.person.filter(surname=search)
            context = {'group': Group.objects.get(pk=id), 'result': result}
            return render(request, "my_contacts/search.html", context)
        except:
            return HttpResponse("Ta osoba nie należy do tej grupy")





