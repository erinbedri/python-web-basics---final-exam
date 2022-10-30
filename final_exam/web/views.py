from django.shortcuts import render, redirect, get_object_or_404

from final_exam.web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm, \
    DeleteProfileForm
from final_exam.web.models import Profile, Car


def get_profile():
    profile = Profile.objects.all().first()
    return profile


def homepage(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def show_catalogue(request):
    profile = get_profile()
    cars = Car.objects.all()
    cars_count = cars.count()

    context = {
        'profile': profile,
        'cars': cars,
        'cars_count': cars_count,
    }

    return render(request, 'catalogue.html', context)


def create_car(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')
    else:
        form = CreateCarForm()

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'car-create.html', context)


def show_car(request, pk):
    profile = get_profile()
    car = get_object_or_404(Car, pk=pk)

    context = {
        'car': car,
        'profile': profile,
    }

    return render(request, 'car-details.html', context)


def edit_car(request, pk):
    profile = get_profile()
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')
    else:
        form = EditCarForm(instance=car)

    context = {
        'profile': profile,
        'form': form,
        'car': car,
    }

    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    profile = get_profile()
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'GET':
        context = {
            'profile': profile,
            'car': car,
            'form': DeleteCarForm(instance=car),
        }
        return render(request, 'car-delete.html', context)

    car.delete()
    return redirect('show catalogue')


def create_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')
    else:
        form = CreateProfileForm()

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-create.html', context)


def show_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_price_cars = sum(car.price for car in cars)

    context = {
        'profile': profile,
        'total_price_cars': total_price_cars,
    }

    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    cars = Car.objects.all()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            cars.delete()
            profile.delete()
            return redirect('homepage')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-delete.html', context)

