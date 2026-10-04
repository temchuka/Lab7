from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Lease


def archive(request):
    return render(request, 'archive.html', {"posts": Lease.objects.all()})


def get_lease(request, lease_id):
    try:
        post = Lease.objects.get(id=lease_id)
        return render(request, 'lease.html', {"post": post})
    except Lease.DoesNotExist:
        raise Http404


def create_lease(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # в словаре form хранится информация, введенная пользователем
            form = {
                'contract': request.POST["contract"],
                'outlet': request.POST["outlet"],
                'floor': request.POST["floor"],
                'area': request.POST["area"],
                'conditioner': request.POST.get("conditioner") == "on",
                'day_price': request.POST["day_price"],
                'tenant': request.POST["tenant"],
                'contact': request.POST["contact"],
                'contract_date': request.POST["contract_date"],
                'start_date': request.POST["start_date"],
                'end_date': request.POST["end_date"],
                'text': request.POST["text"],
            }
            required = ['contract', 'outlet', 'floor', 'area', 'day_price', 'tenant',
                        'contact', 'contract_date', 'start_date', 'end_date', 'text']
            if all(form[name] for name in required):
                # проверка уникальности номера договора
                if Lease.objects.filter(contract=form["contract"]).exists():
                    form['errors'] = "Договор с таким номером уже существует"
                    return render(request, 'create_lease.html', {'form': form})
                try:
                    # если поля заполнены без ошибок, создается новая запись
                    lease = Lease.objects.create(
                        contract=form["contract"],
                        outlet=form["outlet"],
                        floor=form["floor"],
                        area=form["area"],
                        conditioner=form["conditioner"],
                        day_price=form["day_price"],
                        tenant=form["tenant"],
                        contact=form["contact"],
                        contract_date=form["contract_date"],
                        start_date=form["start_date"],
                        end_date=form["end_date"],
                        text=form["text"],
                        author=request.user
                    )
                except (ValueError, ValidationError):
                    form['errors'] = "Проверьте правильность чисел и дат"
                    return render(request, 'create_lease.html', {'form': form})
                # переход на страницу созданной записи
                return redirect('get_lease', lease_id=lease.id)
            else:
                # если введенные данные некорректны
                form['errors'] = "Не все поля заполнены"
                return render(request, 'create_lease.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_lease.html', {})
    else:
        raise Http404


def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'email': request.POST["email"],
            'password': request.POST["password"],
        }
        if form["username"] and form["email"] and form["password"]:
            try:
                User.objects.get(username=form["username"])
                # если пользователь существует, то ошибки не произойдет
                form['errors'] = "Пользователь с таким именем уже есть"
            except User.DoesNotExist:
                # логин свободен - регистрируем нового пользователя
                User.objects.create_user(form["username"], form["email"], form["password"])
                return redirect('login')
        else:
            form['errors'] = "Не все поля заполнены"
        return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {})


def user_login(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'password': request.POST["password"],
        }
        if form["username"] and form["password"]:
            user = authenticate(username=form["username"], password=form["password"])
            if user is not None:
                # аутентификация прошла успешно - авторизуем пользователя
                login(request, user)
                return redirect('archive')
            else:
                form['errors'] = "Нет аккаунта с таким сочетанием никнейма и пароля"
        else:
            form['errors'] = "Не все поля заполнены"
        return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {})
