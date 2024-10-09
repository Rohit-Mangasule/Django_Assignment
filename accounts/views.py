from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm , PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView



class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class profile_view(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "registration/profile.html"
    context_object_name = "user"

    def get_object(self):
        return self.request.user
    
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'


