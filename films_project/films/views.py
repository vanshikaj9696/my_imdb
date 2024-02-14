from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Film
from .forms import FilmForm

# common settings for other views
def base_view(request):
    model = Film
    fields = '__all__'
    success_url = reverse('films:all')
    return model, fields, success_url

def film_list_view(request):
    model, fields, success_url = base_view(request)
    film_list = model.objects.all()
    # print(film_list)
    return render(request, 'film_list.html', {'film_list': film_list})

def film_detail_view(request, pk):
    model, fields, success_url = base_view(request)
    film = get_object_or_404(model, pk=pk)
    return render(request, 'film_detail.html', {'film': film})

def film_create_view(request):
    model, fields, success_url = base_view(request)
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = FilmForm()
    return render(request, 'film_form.html', {'form': form})

def film_update_view(request, pk):
    model, fields, success_url = base_view(request)
    film = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = FilmForm(instance=film)
    return render(request, 'film_form.html', {'form': form})

def film_delete_view(request, pk):
    model, fields, success_url = base_view(request)
    film = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        film.delete()
        return redirect(success_url)
    return render(request, 'film_confirm_delete.html', {'film': film})
