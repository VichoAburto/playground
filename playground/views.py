from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Character, Equipement

def index(request):
    return render(request, 'playground/index.html')

def character_list(request):
    characters = Character.objects.all()
    return render(request, 'playground/character_list.html', {'characters': characters})

# def character_detail(request, id_character):
#     character = get_object_or_404(Character, id_character=id_character)
#     form=MoveForm()
#     print("Im here")
#     if form.is_valid():
#         print("Im here2")
#         ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
#         ancien_lieu.disponibilite = "libre"
#         ancien_lieu.save()
#         form.save(commit=False) 
#         nouveau_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
#         nouveau_lieu.disponibilite = "occupé"
#         nouveau_lieu.save()
#         return redirect('character_detail', id_character=id_character)
#     else:
#         print("Im here3")
#         form = MoveForm()
#         lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
#         return render(request,
#                   'playground/character_detail.html',
#                   {'character': character, 'lieu': lieu, 'form': form})

def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    if request.method == 'POST':
        form = MoveForm(request.POST)
        if form.is_valid():
            ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
            ancien_lieu.disponibilite = "libre"
            ancien_lieu.save()
            updated_character = form.save(commit=False)
            nouveau_lieu = get_object_or_404(Equipement, id_equip=updated_character.lieu.id_equip)
            if nouveau_lieu.disponibilite == "occupé":
                message = "The selected place is occupied. Please choose another."
                print("Im here4")
                return render(request, 'playground/character_detail.html', {
                    'character': character,
                    'lieu': ancien_lieu,
                    'form': form,
                    'message': message,
                })
            nouveau_lieu.disponibilite = "occupé"
            nouveau_lieu.save()
            character.lieu = updated_character.lieu
            character.save()
            return redirect('character_detail', id_character=id_character)
    else:
        form = MoveForm()
    lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
    return render(request, 'playground/character_detail.html', {
        'character': character,
        'lieu': lieu,
        'form': form,
    })

def equipement_list(request):
    equipements = Equipement.objects.all()
    return render(request, 'playground/equipement_list.html', {'equipements': equipements})

def equipement_detail(request, pk):
    equipement = get_object_or_404(Equipement, pk=pk)
    return render(request, 'playground/equipement_detail.html', {'equipement': equipement})
