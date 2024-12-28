from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Folder
from .forms import FolderForm, FolderRenameForm, UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            root_folder = Folder.objects.create(
                name="Root Folder",
                parent=None,
                owner=user
            )
            login(request, user)
            return redirect('folder_list', folder_id=root_folder.id)
        else:
            return render(request, 'drive/register.html', {'form': form, 'error': 'Invalid data'})
    else:
        form = UserRegistrationForm()
    
    return render(request, 'drive/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            folder = get_object_or_404(Folder, owner=user, parent=None)
            next_url = request.POST.get('next', f'/folder/list/{folder.id}/')
            return redirect(next_url)
        else:
            return render(request, 'drive/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()

    return render(request, 'drive/login.html', {'form': form})

@login_required
def folder_list(request, folder_id=None):
    folder = get_object_or_404(Folder, id=folder_id) if folder_id else None
    subfolders = Folder.objects.filter(parent=folder)
    return render(request, 'drive/folder_list.html', {
        'folder': folder,
        'subfolders': subfolders,
        'folder_form': FolderForm()
    })

@login_required
def create_folder(request, parent_id):
    if request.method == 'POST':
        form = FolderForm(request.POST, user=request.user)
        parent_folder = get_object_or_404(Folder, id=parent_id)

        if form.is_valid():
            folder = form.save(commit=False)
            folder.parent = parent_folder
            folder.owner = request.user
            try:
                folder.save()
                return redirect('folder_list', folder_id=parent_folder.id)
            except IntegrityError:
                form.add_error('name', 'A folder with this name already exists in this parent folder.')
                return render(request, 'drive/create_folder.html', {'form': form, 'error': form.errors})
        else:
            return render(request, 'drive/create_folder.html', {'form': form, 'error': form.errors})
    else:
        form = FolderForm()

    return render(request, 'drive/create_folder.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def rename_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)

    if folder.owner == request.user:
        if request.method == 'POST':
            form = FolderRenameForm(request.POST, instance=folder)
            if form.is_valid():
                form.save()
                return redirect('folder_list', folder_id=folder.parent.id)
        else:
            form = FolderRenameForm(instance=folder)

        return render(request, 'drive/rename_folder.html', {
            'form': form,
            'folder': folder
        })
    else:
        return render(request, 'drive/folder_list.html', {
            'folder': folder,
            'error_message': 'You are not the owner of this folder and cannot rename it.'
        })

@login_required
def delete_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)

    if folder.owner == request.user:
        parent_folder = folder.parent
        folder.delete()
        return redirect('folder_list', folder_id=parent_folder.id)
    else:
        return render(request, 'drive/folder_list.html', {
            'folder': folder,
            'error_message': 'You are not the owner of this folder, and cannot delete it.'
        })
