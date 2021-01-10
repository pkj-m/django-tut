from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):

    # POST request is made to the form when the form is submitted
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        # instantiate the form with request.POST to make sure the updated data is also contained within the form
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # request.FILES is needed for image transfer
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # save information if both the forms are valid

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account information updated successfully!')

            # redirect is important here as it sends a GET request instead of the POST request outside the if - else
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
