from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
# Password Reset Requirements
from django.contrib.auth.views import PasswordResetView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse_lazy

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('site:index')
    else:
        form = AuthenticationForm()

    return render(request, 'account/login.html', {"form": form})


@login_required()
def profile_view(request):
    return render(request, 'account/profile.html')


def logout_view(request):
    logout(request)

    return redirect('site:index')

# Custom PasswordResetView
class MyPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'account/password_reset_subject.txt'
    success_url = reverse_lazy('account:password_reset_done')

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        subject = render_to_string("account/password_reset_subject.txt", context)
        html_message = render_to_string("account/password_reset_email.html", context)
        plain_message = render_to_string("account/password_reset_email.html", context)

        msg = EmailMultiAlternatives(subject, plain_message, from_email, [to_email])
        msg.attach_alternative(html_message, "text/html")
        msg.send()

    def get_context_data_for_email(self, user):
        return {
            "email": user.email,
            "domain": self.request.get_host(),
            "site_name": "QAM Courses",
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "user": user,
            "token": default_token_generator.make_token(user),
            "protocol": "https" if self.request.is_secure() else "http",
        }

    def form_valid(self, form):
        email = form.cleaned_data["email"]

        users = User.objects.filter(email=email)

        for user in users:
            context = self.get_context_data_for_email(user)
            self.send_mail(
                self.subject_template_name,
                self.email_template_name,
                context,
                settings.DEFAULT_FROM_EMAIL,
                user.email
            )
        # return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)
