from django.shortcuts import render
from django.db import models
from django.views.generic import TemplateView
from django.views import generic
from . import models
from experiment.models import EGroup,InGroup,IsJudge
from .forms import GoldForm,JudgeGold
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                    PermissionRequiredMixin)
from django.shortcuts import get_object_or_404
from accounts.models import Account
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth import get_user_model
User= get_user_model()

# Create your views here.

class FirstView(generic.ListView):
    model = models.InGroup
    template_name = 'experiment/first.html'





class CreateGroup(generic.CreateView):
    fields=('name','description')
    model= EGroup

class SingleGroup(generic.DetailView):
    template_name = 'experiment/egroup_detail.html'
    model=EGroup


    def get(self, request, slug,elnamo):
        model=EGroup
        group= get_object_or_404(EGroup,slug=self.kwargs.get('slug'))
        form2 = GoldForm()
        form3= JudgeGold()

        args = {'form':form2,'name':group,'form3':form3}
        return render(request,self.template_name,args)


    def post(self, request,slug,elnamo):
        form = GoldForm(request.POST)
        form3 = JudgeGold(request.POST)
        group= get_object_or_404(EGroup,slug=self.kwargs.get('slug'))
        if form.is_valid():
            name = request.user
            gold = form.cleaned_data["givegold"]
            if name.gold >= gold:
                name.gold=name.gold-gold
                group.goldinroom=group.goldinroom+gold
                name.save()
                group.save()

        if form3.is_valid():
            person=Account.objects.get(username=request.POST.get('name'))
            gold = form3.cleaned_data["jgold"]
            group= get_object_or_404(EGroup,slug=self.kwargs.get('slug'))
            if group.goldinroom >= gold:
                person.gold=person.gold+gold
                group.goldinroom=group.goldinroom-gold
                group.save()
                person.save()

        args = {'form':form,'name':group,'form3':form3}
        return render(request, self.template_name,args)



class ListGroups(generic.ListView):
    model = EGroup

class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('experiment:single1',kwargs={'slug': self.kwargs.get('slug'),'elnamo':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group= get_object_or_404(EGroup,slug=self.kwargs.get('slug'))

        try:
            InGroup.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,'warning already a member!')
        else:
            messages.success(self.request,'Your are now a member')
        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):


    def get_redirect_url(self,*args,**kwargs):
        return reverse('experiment:single1',kwargs={'slug':self.kwargs.get('slug'),'elnamo':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            membership = models.InGroup.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        except models.InGroup.DoesNotExist:
            messages.warning(self.request,'sorry you arent in this group!')

        else:
            membership.delete()
            messages.success(self.request,'you have left the group')

        return super().get(request,*args,**kwargs)

class BecomeJudge(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('experiment:single1',kwargs={'slug': self.kwargs.get('slug'),'elnamo':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group= get_object_or_404(EGroup,slug=self.kwargs.get('slug'))
        person=self.kwargs.get('elnamo')
        try:
            if person != group.slug:
                IsJudge.objects.create(judge1=User.objects.get(email=self.kwargs.get('elnamo')),courtroom=group)
        except IntegrityError:
            messages.warning(self.request,'warning already a member!')
        else:
            messages.success(self.request,'Your are now a judge')
        return super().get(request,*args,**kwargs)

class UnJudge(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('experiment:single1',kwargs={'slug':self.kwargs.get('slug'),'elnamo':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            courtroomjudge = models.IsJudge.objects.filter(
                judge1=User.objects.get(email=self.kwargs.get('elnamo')),
                courtroom__slug=self.kwargs.get('slug')
            ).get()
        except models.IsJudge.DoesNotExist:
            messages.warning(self.request,'sorry you arent in this group!')
        else:
            courtroomjudge.delete()
            messages.success(self.request,'you have left the group')

        return super().get(request,*args,**kwargs)
