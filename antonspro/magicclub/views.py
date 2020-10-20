from django.shortcuts import render
from django.views.generic import TemplateView
from magicclub.models import Tournament
from django.urls import reverse
from django.views import generic
from .forms import NameForm,PairNow,APoints,DropForm,ClubForm,SaveForm,LoadForm,ClearForm,ClubMemberPoints
from django.shortcuts import get_object_or_404
import random
import operator
from random import shuffle
from operator import itemgetter, attrgetter, methodcaller
import pickle

# Create your views here.


class Homepage(TemplateView):
    template_name= 'magicclub/home.html'

class CreateGroup(generic.CreateView):
    fields=('name','description')
    model= Tournament

class SingleGroup(generic.DetailView):
    template_name = 'magicclub/tournament_detail.html'
    model=Tournament

    def get(self, request, slug):
        model=Tournament
        group= get_object_or_404(Tournament,slug=self.kwargs.get('slug'))
        form1 = NameForm()
        form2= DropForm()
        form3= ClubForm()
        form4= SaveForm()
        form5= LoadForm()
        form6= ClearForm()


        dill1=open('magicclub/tournamentdata/clubmembers.pickle','rb')
        clubpeeps=pickle.load(dill1)
        dill1.close()

        if len(group.clubmembers)==0:
            for person in clubpeeps:
                group.clubmembers.append(person[0])



        args = {'form1':form1,'group':group,'form2':form2,'form4':form4,'form5':form5,'form6':form6}
        return render(request,self.template_name,args)


    def post(self, request,slug):
        model=Tournament
        form1 = NameForm(request.POST)
        form2= DropForm(request.POST)
        form3= ClubForm(request.POST)
        form4= SaveForm(request.POST)
        form5= LoadForm(request.POST)
        form6= ClearForm(request.POST)
        group= get_object_or_404(Tournament,slug=self.kwargs.get('slug'))
        clubpeeps= group.clubmembers



        if form1.is_valid():
            if form1.cleaned_data["playername"]:
                name = form1.cleaned_data["playername"]

                if name not in group.tempplayers:
                    group.tempplayers.append(name)
                    group.players.append([name,0,0,0,[]])
                    group.save()
                else:
                    group.tempplayers.remove(name)
                    for person in group.players:
                        if name==person[0]:
                            group.players.remove(person)

        if form2.is_valid():
            if form2.cleaned_data["drop"]:
                todrop= form2.cleaned_data["drop"]
                for name in group.players:
                    if name[0].lower() == todrop.lower():
                        group.tempplayers.remove(name[0])
                        group.players.remove(name)
                        group.drop.append(name)
                        group.save()


        if form4.is_valid():
            if form4.cleaned_data["update1"]:
                try:
                    dill1=open('magicclub/tournamentdata/{}.pickle'.format(group.name),'ab')
                    pickle.dump(group.players,dill)
                    dill1.close()
                except:
                    dill1= open('magicclub/tournamentdata/{}.pickle'.format(group.name),'wb')
                    pickle.dump(group.players,dill1)
                    dill1.close()

        if form5.is_valid():
            if form5.cleaned_data["load1"]:
                group.players.clear()
                pickedin=open('magicclub/tournamentdata/{}.pickle'.format(group.name),'rb')
                picklelist=pickle.load(pickedin)
                for person in picklelist:
                    group.players.append(person)
                    group.save()
                pickedin.close()

        if form6.is_valid():
            if form6.cleaned_data["clearit"]:
                group.players.clear()
                group.drop.clear()
                group.tempplayers.clear()
                group.save()



        clubboy=request.POST.get('name')
        if str(clubboy) != 'None':
            group.players.append([clubboy,0,0,0,[]])
            group.tempplayers.append(clubboy)
            group.save()


        args = {'form1':form1,'group':group,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'form6':form6}
        return render(request, self.template_name,args)

class PairGroup(generic.DetailView):
    template_name = 'magicclub/pairings.html'
    model=Tournament

    def get(self, request, slug):
        model=Tournament
        group= get_object_or_404(Tournament,slug=self.kwargs.get('slug'))
        form1= PairNow()
        form2= APoints()
        table=group.table
        args = {'group':group,'form1':form1,'table':table,'form2':form2}
        return render(request,self.template_name,args)

    def post(self, request, slug):
        model=Tournament
        form1= PairNow(request.POST)
        form2= APoints(request.POST)
        group= get_object_or_404(Tournament,slug=self.kwargs.get('slug'))
        playerpoints=group.players
        nlist=[]
        ulist=[]
        bye=[]
        table=group.table
        if form1.is_valid():
            if len(table)==0:
                random.shuffle(playerpoints)
                playerpoints=sorted(playerpoints,key=itemgetter(1), reverse=False)

                if len(playerpoints)%2==1: #bye handling, will have to edit later
                    for person in playerpoints:
                        if 'bye' in person[4]:
                            None
                        else:
                            bye.append(person)
                            playerpoints.remove(person)
                            for name in group.players:
                                if name[0]==bye[0][0]:
                                    name[1]=name[1]+3
                                    name[2]=name[2]+2
                                    name[4].append('bye')
                            break

                tablenum=1
                templist=[]
                playerpoints=sorted(playerpoints,key=itemgetter(1), reverse=True)

                while len(playerpoints)>0: #pairings
                    if playerpoints[1][0] in playerpoints[0][4]:
                        if len(playerpoints)==2:
                            templist.append([playerpoints[0],playerpoints[1]])
                            table.append([playerpoints[0][0],playerpoints[1][0],'table '+str(tablenum)])
                            playerpoints.pop(0)
                            playerpoints.pop(0)
                            tablenum+=1

                        else:
                            for n in playerpoints[1::]:
                                if n[0] not in playerpoints[0][4]:
                                    templist.append([playerpoints[0],n])
                                    table.append([playerpoints[0][0],n[0],'table '+str(tablenum)])
                                    playerpoints.remove(n)
                                    playerpoints.pop(0)
                                    tablenum+=1
                                    break
                    else:
                        templist.append([playerpoints[0],playerpoints[1]])
                        table.append([playerpoints[0][0],playerpoints[1][0],'table '+str(tablenum)])
                        playerpoints.pop(0)
                        playerpoints.pop(0)
                        tablenum+=1

                for n in templist:
                    for g in n:
                        playerpoints.append(g)



        if form2.is_valid():
            pone = int(form2.cleaned_data["p1"])
            ptwo = int(form2.cleaned_data["p2"])
            table1=request.POST.get('name')
            for thing in table:
                if thing[2]==table1:
                    for name in group.players:
                        if name[0]==thing[0]:
                            if pone>ptwo:
                                name[1]=name[1]+3
                            name[2]=name[2]+pone
                            name[3]=name[3]+ptwo
                            name[4].append(thing[1])
                            if pone==ptwo:
                                name[1]=name[1]+1
                            group.save()

                    for name in group.players:
                        if name[0]==thing[1]:
                            if ptwo>pone:
                                name[1]=name[1]+3
                            name[2]=name[2]+ptwo
                            name[3]=name[3]+pone
                            name[4].append(thing[0])
                            if pone==ptwo:
                                name[1]=name[1]+1
                            group.save()
                    group.table.remove(thing)





        args = {'group':group,'table':table,'form2':form2,'bye':bye}
        return render(request,self.template_name,args)


class ListGroups(generic.ListView):
    model = Tournament

class StandingsGroup(generic.DetailView):
    template_name = 'magicclub/standings.html'
    model=Tournament

    def get(self, request, slug):
        model=Tournament
        group= get_object_or_404(Tournament,slug=self.kwargs.get('slug'))
        playerpoints=group.players
        recordclub=ClubMemberPoints()

        # global droplist
        standings1=[]
        for name in group.drop:
            playerpoints.append(name)
        for n in playerpoints:
            breakers=[0,0,0]
            try:
                if n[2]/(n[2]+n[3])>32:
                    breakers[1]=n[2]/(n[2]+n[3]) #T2
                else:
                    breakers[1]=33
            except:
                ZeroDivisionError
                breakers[1]=0
            for player in n[4]:
                for sameplayer in playerpoints:
                    if sameplayer[0]==player:
                        breakers[0]=breakers[0]+((sameplayer[1]/3)/len(sameplayer[4])) #T1 the 1 has to be replaced by number of rounds
                        breakers[2]=breakers[2]+(sameplayer[2]/(sameplayer[2]+sameplayer[3])) #T3
            templist=[]
            templist.append(n[0])
            templist.append(n[1])
            try:
                if breakers[0]/len(n[4]) > 33:
                    templist.append("{0:.2f}".format(breakers[0]/len(n[4])))
                else:
                    templist.append("{0:.2f}".format(33))
            except:
                ZeroDivisionError
                templist.append("{0:.2f}".format(0))
            try:
                templist.append("{0:.2f}".format(breakers[1]))
            except:
                ZeroDivisionError
                templist.append("{0:.2f}".format(0))
            try:
                if breakers[2]/len(n[4]) > 33:
                    templist.append("{0:.2f}".format(breakers[2]/len(n[4])))
                else:
                    templist.append("{0:.2f}".format(33))
            except:
                ZeroDivisionError
                templist.append("{0:.2f}".format(0))
            standings1.append(templist)

        for name in group.drop:
            for name2 in standings1:
                if name2[0]==name[0]:
                    standings1.remove(name2)



        standings1=sorted(standings1,key=itemgetter(1,2,3,4), reverse=True)



        args = {'standings1':standings1,'group':group,'recordclub':recordclub}
        return render(request,self.template_name,args)

    def post(self, request, slug):
        model=Tournament
        form1= ClubMemberPoints(request.POST)
        group= get_object_or_404(Tournament,slug=self.kwargs.get('slug'))

        if form1.is_valid:
            if form1.cleaned_data["format"]:
                tourneyname = form2.cleaned_data["format"]
                pickedin=open('magicclub/tournamentdata/{}.pickle'.format(group.name),'wb')
                clubmemberlist=pickle.load(pickedin)
                testlist=group.players
                testlist.sort(key=lambda player: player[1],reverse=True)
                onlyname=['Gary','Roman','Simu']

                for player in testlist:
                    if player[0] in onlyname:
                        for member in clubmemberlist:
                            if player[0]==member[0]:
                                member[1]=member[1]+player[1]
                                member[2]=member[2]+player[2]
                                member[3]=member[3]+player[3]
                                for opponent in player[4]:
                                    member[4].append(opponent)
                                member[5].append([tourneyname,testlist.index(player)+1])

                pickle.dump(clubmemberlist,pickedin)
                pickedin.close()

        args = {'standings1':standings1,'group':group,'recordclub':'Points recorded to club sucessfully'}
        return render(request,self.template_name,args)
