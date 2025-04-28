# videos/views.py
from django.shortcuts import render, redirect
from .forms import VideoUploadForm, UserRegistrationForm
from .models import Video
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login as auth_login
from django.core.paginator import Paginator


from django.shortcuts import get_object_or_404, redirect
from .models import Video
from django.contrib.auth import logout

from .models import Video, Comment
# def video_list(request):
#     videos = Video.objects.all()
#     return render(request, 'videos/video_list.html', {'videos': videos})

def video_list(request):
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 5)  # Показывать 5 видео на странице

    page_number = request.GET.get('page')
    videos = paginator.get_page(page_number)

    return render(request, 'videos/video_list.html', {'videos': videos})

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            messages.success(request, 'Видео успешно загружено!')
            return redirect('video_list')
    else:
        form = VideoUploadForm()
    return render(request, 'videos/upload.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()  # Сохраняем пользователя
#             auth_login(request, user)  # Автоматически входим в систему
#             return redirect('home')  # Перенаправление на домашнюю страницу
#         else:
#             messages.error(request, 'Ошибка при регистрации. Проверьте введенные данные.')
#     else:
#         form = UserRegistrationForm()
    
#     return render(request, 'registration/register.html', {'form': form})



def register(request):
    if request.method == 'POST':
        print("POST request received")  # Отладочное сообщение
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем пользователя
            auth_login(request, user)  # Автоматически входим в систему
            print("User  registered and logged in")  # Отладочное сообщение
            return redirect('home')  # Перенаправление на домашнюю страницу
        else:
            messages.error(request, 'Ошибка при регистрации. Проверьте введенные данные.')
            print("Form is not valid")  # Отладочное сообщение
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def home(request):
    return render(request, 'registration/home.html')

def login_view1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'registration/login_view.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Используйте get
        password = request.POST.get('password')  # Используйте get
        
        if username is None or password is None:
            messages.error(request, 'Имя пользователя и пароль обязательны.')
            return render(request, 'registration/login_view.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    
    return render(request, 'registration/login_view.html')


# def delete_video(request, video_id):
#     video = get_object_or_404(Video, id=video_id)
#     if request.method == 'POST':
#         video.delete()
#         return redirect('video_list')  # Замените 'video_list' на имя вашего маршрута
#     return render(request, 'confirm_delete.html', {'video': video})


def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.delete()
        messages.success(request, 'Видео успешно удалено!')
        return redirect('video_list')  # Замените 'video_list' на имя вашего маршрута
    return render(request, 'confirm_delete.html', {'video': video})

@login_required
def add_comment(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        comment = Comment(video=video, user=request.user, text=text)
        comment.save()
        messages.success(request, 'Комментарий успешно добавлен!')
        return redirect('video_list')
    return redirect('video_list')

def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы.')
    return redirect('home')  # Перенаправление на главную страницу после выхода

