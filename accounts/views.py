from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,'accounts/index.html')

@login_required
def home(request):
    return render(request,'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # 入力された値からUserインスタンスを作成
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            # フォームの入力値が認証できればユーザーオブジェクト、できなければNoneを返す
            new_user = authenticate(username = input_username, password = input_password)
            # 認証成功時のみ、ユーザーをログインさせる
            if new_user is not None:
                login(request, new_user)
                return redirect('accounts:index')
            return render(request,'registration/signup.html',{'form':form})
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})