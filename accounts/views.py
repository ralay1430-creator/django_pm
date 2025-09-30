from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm , ProfileForm
from django.contrib.auth import login
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    # success_url = reverse_lazy('login')  # ممكن تلغيها لو تستخدم get_success_url

    def form_valid(self, form):
        # نسجل المستخدم مباشرة بعد الإنشاء
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

    def get_success_url(self):
        return reverse_lazy('project_list')  # انتبه لحروف الاسم لازم نفس اللي في urls.py
  
@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {
        'form': form
    })