from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.db.models import Q

# Create your views here.
def index(request):

    if(request.method=='POST'):
        if(request.POST.get('searchbtn')== 'search'):
            bg = request.POST.get('search')
            var1 = CustomUser.objects.filter(Q(bloodgroup1 = bg)| Q(bloodgroup2= bg) | Q(bloodgroup3= bg) | Q(bloodgroup4= bg) | Q(bloodgroup5= bg) | Q(bloodgroup6= bg) | Q(bloodgroup7= bg) | Q(bloodgroup8= bg))
            return render(request,'index.html',{'var1':var1,})

    return render(request,'index.html')

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
