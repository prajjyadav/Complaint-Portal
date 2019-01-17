from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views import generic
from comportal.models import Complain
from .admin import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib import messages

class UserFormView(generic.View):
    form_class = UserCreationForm
    template_name = 'comportal/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'Your account has been created and you are loged in')
                    return redirect('comportal:index')

        return render(request, self.template_name, {'form':form}) 


# class UserUpdateFormView(LoginRequiredMixin, generic.edit.UpdateView):
#     form_class = UserChangeForm
#     template_name = 'comportal/registration_form.html'

#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form':form})

#     def post(self, request):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()

#         return render(request, self.template_name, {'form':form}) 


class UserUpdateFormView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    fields = ['email','name', 'mobile','gender','registration_number','image']
    template_name = 'comportal/registration_form.html'

    def form_valid(self, form):
        form.instance.by = str(self.request.user)
        messages.success(self.request, f'Your account has been updated!')
        return super().form_valid(form)

    def test_func(self):
        customUser = str(self.get_object())
        user = str(self.request.user)
        if user == customUser:
            return True
        return False

@login_required(login_url='/accounts/login')
def profile(request):
    complains = Complain.objects.filter(by=request.user)
    return render(request, 'users_auth/complains.html', {'complain_list': complains, 'user':request.user, 'allow':True})


@login_required
def clear(request):
    # user = get_object_or_404(CustomUser, id=pk)
    user = request.user
    user.noti_messages = ''
    user.notifications = 0
    user.save()
    messages.success(request, f'All notifications cleared')
    return HttpResponseRedirect(reverse('users_auth:user-profile'))                

# class LoginFormView(generic.View):
    
#     template_name = 'comportal/registration_form.html'

#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form':form})

#     def post(self, request):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             user = form.save(commit=False)
#             print(user)
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user.set_password(password)
#             user.save()

#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('comportal:index')

#         return render(request, self.template_name, {'form':form}) 


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active: 
            login(request, user)
            messages.success(request, f'Hello'+username)
            return redirect('users_auth:user-profile')





    