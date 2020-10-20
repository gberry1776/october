from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
from .forms import SuForm
from django.views import generic
from django import forms
from django.http import HttpResponse
from django.urls import reverse_lazy,reverse

# Create your views here.
class SudokuSolve(TemplateView):
    template_name = 'sudoku/sudoku.html'


def injection(request):
    my_dict= {'insert_me':"im from def injection"}
    return render(request,'index.html',context=my_dict)

class FillBoard(TemplateView):
    template_name= 'sudoku/test_form.html'

    def get(self, request):
        form = SuForm()
        return render(request, self.template_name, {'form':form})


    def post(self, request):
        form = SuForm(request.POST)
        if form.is_valid():
            one = [form.cleaned_data["post1"],[1,2,3,4,5,6,7,8,9,11]]
            two = [form.cleaned_data["post2"],[1,2,3,4,5,6,7,8,9,12]]
            three = [form.cleaned_data["post3"],[1,2,3,4,5,6,7,8,9,13]]
            four = [form.cleaned_data["post4"],[1,2,3,4,5,6,7,8,9,14]]
            five = [form.cleaned_data["post5"],[1,2,3,4,5,6,7,8,9,15]]
            six = [form.cleaned_data["post6"],[1,2,3,4,5,6,7,8,9,16]]
            seven = [form.cleaned_data["post7"],[1,2,3,4,5,6,7,8,9,17]]
            eight = [form.cleaned_data["post8"],[1,2,3,4,5,6,7,8,9,18]]
            nine = [form.cleaned_data["post9"],[1,2,3,4,5,6,7,8,9,19]]
            ten = [form.cleaned_data["post10"],[1,2,3,4,5,6,7,8,9,110]]
            eleven = [form.cleaned_data["post11"],[1,2,3,4,5,6,7,8,9,111]]
            twelve = [form.cleaned_data["post12"],[1,2,3,4,5,6,7,8,9,112]]
            thirteen = [form.cleaned_data["post13"],[1,2,3,4,5,6,7,8,9,113]]
            fourteen = [form.cleaned_data["post14"],[1,2,3,4,5,6,7,8,9,114]]
            fifteen = [form.cleaned_data["post15"],[1,2,3,4,5,6,7,8,9,115]]
            sixteen = [form.cleaned_data["post16"],[1,2,3,4,5,6,7,8,9,116]]
            seventeen = [form.cleaned_data["post17"],[1,2,3,4,5,6,7,8,9,117]]
            eighteen = [form.cleaned_data["post18"],[1,2,3,4,5,6,7,8,9,118]]
            nineteen = [form.cleaned_data["post19"],[1,2,3,4,5,6,7,8,9,119]]
            twenty = [form.cleaned_data["post20"],[1,2,3,4,5,6,7,8,9,120]]
            twentyone = [form.cleaned_data["post21"],[1,2,3,4,5,6,7,8,9,121]]
            twentytwo = [form.cleaned_data["post22"],[1,2,3,4,5,6,7,8,9,122]]
            twentythree = [form.cleaned_data["post23"],[1,2,3,4,5,6,7,8,9,123]]
            twentyfour = [form.cleaned_data["post24"],[1,2,3,4,5,6,7,8,9,124]]
            twentyfive = [form.cleaned_data["post25"],[1,2,3,4,5,6,7,8,9,125]]
            twentysix = [form.cleaned_data["post26"],[1,2,3,4,5,6,7,8,9,126]]
            twentyseven = [form.cleaned_data["post27"],[1,2,3,4,5,6,7,8,9,127]]
            twentyeight = [form.cleaned_data["post28"],[1,2,3,4,5,6,7,8,9,128]]
            twentynine = [form.cleaned_data["post29"],[1,2,3,4,5,6,7,8,9,129]]
            thirty = [form.cleaned_data["post30"],[1,2,3,4,5,6,7,8,9,130]]
            thirtyone = [form.cleaned_data["post31"],[1,2,3,4,5,6,7,8,9,131]]
            thirtytwo = [form.cleaned_data["post32"],[1,2,3,4,5,6,7,8,9,132]]
            thirtythree = [form.cleaned_data["post33"],[1,2,3,4,5,6,7,8,9,133]]
            thirtyfour = [form.cleaned_data["post34"],[1,2,3,4,5,6,7,8,9,134]]
            thirtyfive = [form.cleaned_data["post35"],[1,2,3,4,5,6,7,8,9,135]]
            thirtysix = [form.cleaned_data["post36"],[1,2,3,4,5,6,7,8,9,136]]
            thirtyseven = [form.cleaned_data["post37"],[1,2,3,4,5,6,7,8,9,137]]
            thirtyeight = [form.cleaned_data["post38"],[1,2,3,4,5,6,7,8,9,138]]
            thirtynine = [form.cleaned_data["post39"],[1,2,3,4,5,6,7,8,9,139]]
            fourty = [form.cleaned_data["post40"],[1,2,3,4,5,6,7,8,9,140]]
            fourtyone = [form.cleaned_data["post41"],[1,2,3,4,5,6,7,8,9,141]]
            fourtytwo = [form.cleaned_data["post42"],[1,2,3,4,5,6,7,8,9,142]]
            fourtythree = [form.cleaned_data["post43"],[1,2,3,4,5,6,7,8,9,143]]
            fourtyfour = [form.cleaned_data["post44"],[1,2,3,4,5,6,7,8,9,144]]
            fourtyfive = [form.cleaned_data["post45"],[1,2,3,4,5,6,7,8,9,145]]
            fourtysix = [form.cleaned_data["post46"],[1,2,3,4,5,6,7,8,9,146]]
            fourtyseven = [form.cleaned_data["post47"],[1,2,3,4,5,6,7,8,9,147]]
            fourtyeight = [form.cleaned_data["post48"],[1,2,3,4,5,6,7,8,9,148]]
            fourtynine = [form.cleaned_data["post49"],[1,2,3,4,5,6,7,8,9,149]]
            fifty = [form.cleaned_data["post50"],[1,2,3,4,5,6,7,8,9,150]]
            fiftyone = [form.cleaned_data["post51"],[1,2,3,4,5,6,7,8,9,151]]
            fiftytwo = [form.cleaned_data["post52"],[1,2,3,4,5,6,7,8,9,152]]
            fiftythree = [form.cleaned_data["post53"],[1,2,3,4,5,6,7,8,9,153]]
            fiftyfour = [form.cleaned_data["post54"],[1,2,3,4,5,6,7,8,9,154]]
            fiftyfive = [form.cleaned_data["post55"],[1,2,3,4,5,6,7,8,9,155]]
            fiftysix = [form.cleaned_data["post56"],[1,2,3,4,5,6,7,8,9,156]]
            fiftyseven = [form.cleaned_data["post57"],[1,2,3,4,5,6,7,8,9,157]]
            fiftyeight = [form.cleaned_data["post58"],[1,2,3,4,5,6,7,8,9,158]]
            fiftynine = [form.cleaned_data["post59"],[1,2,3,4,5,6,7,8,9,159]]
            sixty = [form.cleaned_data["post60"],[1,2,3,4,5,6,7,8,9,160]]
            sixtyone = [form.cleaned_data["post61"],[1,2,3,4,5,6,7,8,9,161]]
            sixtytwo = [form.cleaned_data["post62"],[1,2,3,4,5,6,7,8,9,162]]
            sixtythree = [form.cleaned_data["post63"],[1,2,3,4,5,6,7,8,9,163]]
            sixtyfour = [form.cleaned_data["post64"],[1,2,3,4,5,6,7,8,9,164]]
            sixtyfive = [form.cleaned_data["post65"],[1,2,3,4,5,6,7,8,9,165]]
            sixtysix = [form.cleaned_data["post66"],[1,2,3,4,5,6,7,8,9,166]]
            sixtyseven = [form.cleaned_data["post67"],[1,2,3,4,5,6,7,8,9,167]]
            sixtyeight = [form.cleaned_data["post68"],[1,2,3,4,5,6,7,8,9,168]]
            sixtynine = [form.cleaned_data["post69"],[1,2,3,4,5,6,7,8,9,169]]
            seventy = [form.cleaned_data["post70"],[1,2,3,4,5,6,7,8,9,170]]
            seventyone = [form.cleaned_data["post71"],[1,2,3,4,5,6,7,8,9,171]]
            seventytwo = [form.cleaned_data["post72"],[1,2,3,4,5,6,7,8,9,172]]
            seventythree = [form.cleaned_data["post73"],[1,2,3,4,5,6,7,8,9,173]]
            seventyfour = [form.cleaned_data["post74"],[1,2,3,4,5,6,7,8,9,174]]
            seventyfive = [form.cleaned_data["post75"],[1,2,3,4,5,6,7,8,9,175]]
            seventysix = [form.cleaned_data["post76"],[1,2,3,4,5,6,7,8,9,176]]
            seventyseven = [form.cleaned_data["post77"],[1,2,3,4,5,6,7,8,9,177]]
            seventyeight = [form.cleaned_data["post78"],[1,2,3,4,5,6,7,8,9,178]]
            seventynine = [form.cleaned_data["post79"],[1,2,3,4,5,6,7,8,9,179]]
            eighty = [form.cleaned_data["post80"],[1,2,3,4,5,6,7,8,9,180]]
            eightyone = [form.cleaned_data["post81"],[1,2,3,4,5,6,7,8,9,181]]

            cells=[one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty,thirtyone,thirtytwo,thirtythree,thirtyfour,thirtyfive,thirtysix,thirtyseven,thirtyeight,thirtynine,fourty,fourtyone,
            fourtytwo,fourtythree,fourtyfour,fourtyfive,fourtysix,fourtyseven,fourtyeight,fourtynine,fifty,fiftyone,fiftytwo,fiftythree,fiftyfour,fiftyfive,fiftysix,fiftyseven,fiftyeight,fiftynine,sixty,sixtyone,sixtytwo,sixtythree,sixtyfour,sixtyfive,sixtysix,sixtyseven,sixtyeight,sixtynine,seventy,seventyone,seventytwo,seventythree,seventyfour,seventyfive,seventysix,seventyseven,seventyeight,seventynine,eighty,eightyone]

            firstrow= [one,two,three,four,five,six,seven,eight,nine]
            secondrow=[ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen]
            thirdrow=[nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven]
            fourthrow=[twentyeight,twentynine,thirty,thirtyone,thirtytwo,thirtythree,thirtyfour,thirtyfive,thirtysix]
            fidthrow=[thirtyseven,thirtyeight,thirtynine,fourty,fourtyone,fourtytwo,fourtythree,fourtyfour,fourtyfive]
            sixthrow=[fourtysix,fourtyseven,fourtyeight,fourtynine,fifty,fiftyone,fiftytwo,fiftythree,fiftyfour]
            seventhrow=[fiftyfive,fiftysix,fiftyseven,fiftyeight,fiftynine,sixty,sixtyone,sixtytwo,sixtythree]
            eigthrow=[sixtyfour,sixtyfive,sixtysix,sixtyseven,sixtyeight,sixtynine,seventy,seventyone,seventytwo]
            ninthrow=[seventythree,seventyfour,seventyfive,seventysix,seventyseven,seventyeight,seventynine,eighty,eightyone]

            rows=[firstrow,secondrow,thirdrow,fourthrow,fidthrow,sixthrow,seventhrow,eigthrow,ninthrow]

            columnone=[one,ten,nineteen,twentyeight,thirtyseven,fourtysix,fiftyfive,sixtyfour,seventythree]
            columntwo=[two,eleven,twenty,twentynine,thirtyeight,fourtyseven,fiftysix,sixtyfive,seventyfour]
            columnthree=[three,twelve,twentyone,thirty,thirtynine,fourtyeight,fiftyseven,sixtysix,seventyfive]
            columnfour=[four,thirteen,twentytwo,thirtyone,fourty,fourtynine,fiftyeight,sixtyseven,seventysix]
            columnfive=[five,fourteen,twentythree,thirtytwo,fourtyone,fifty,fiftynine,sixtyeight,seventyseven]
            columnsix=[six,fifteen,twentyfour,thirtythree,fourtytwo,fiftyone,sixty,sixtynine,seventyeight]
            columnseven=[seven,sixteen,twentyfive,thirtyfour,fourtythree,fiftytwo,sixtyone,seventy,seventynine]
            columneight=[eight,seventeen,twentysix,thirtyfive,fourtyfour,fiftythree,sixtytwo,seventyone,eighty]
            columnnine=[nine,eighteen,twentyseven,thirtysix,fourtyfive,fiftyfour,sixtythree,seventytwo,eightyone]

            columns=[columnone,columntwo,columnthree,columnfour,columnfive,columnsix,columnseven,columneight,columnnine]

            box1=[one,two,three,ten,eleven,twelve,nineteen,twenty,twentyone]
            box2=[four,five,six,thirteen,fourteen,fifteen,twentytwo,twentythree,twentyfour]
            box3=[seven,eight,nine,sixteen,seventeen,eighteen,twentyfive,twentysix,twentyseven,]
            box4=[twentyeight,twentynine,thirty,thirtyseven,thirtyeight,thirtynine,fourtysix,fourtyseven,fourtyeight]
            box5=[thirtyone,thirtytwo,thirtythree,fourty,fourtyone,fourtytwo,fourtynine,fifty,fiftyone]
            box6=[thirtyfour,thirtyfive,thirtysix,fourtythree,fourtyfour,fourtyfive,fiftytwo,fiftythree,fiftyfour]
            box7=[fiftyfive,fiftysix,fiftyseven,sixtyfour,sixtyfive,sixtysix,seventythree,seventyfour,seventyfive]
            box8=[fiftyeight,fiftynine,sixty,sixtyseven,sixtyeight,sixtynine,seventysix,seventyseven,seventyeight]
            box9=[sixtyone,sixtytwo,sixtythree,seventy,seventyone,seventytwo,seventynine,eighty,eightyone,]

            boxes=[box1,box2,box3,box4,box5,box6,box7,box8,box9]


            def rowcheck(www):
                for rowie in rows:
                    if www in rowie:
                        for cellv in rowie:
                            if cellv[0] !='':
                                if int(cellv[0]) in www[1]:
                                    www[1].remove(int(cellv[0]))
                if len(www[1])==2:
                    www[0]=str(www[1][0])

            def columncheck(www):
                for x in columns:
                    if www in x:
                        for y in x:
                            if y[0] !='':
                                if int(y[0]) in www[1]:
                                    www[1].remove(int(y[0]))
                if len(www[1])==2:
                    www[0]=str(www[1][0])

            def boxcheck(www):
                for x in boxes:
                    if www in x:
                        for y in x:
                            if y[0] !='':
                                if int(y[0]) in www[1]:
                                    www[1].remove(int(y[0]))
                if len(www[1])==2:
                    www[0]=str(www[1][0])

            def solve9(num):
                temprows=[[],[],[],[],[],[],[],[],[]]
                tempcolumns=[[],[],[],[],[],[],[],[],[]]
                tempboxes=[[],[],[],[],[],[],[],[],[]]

                rowcounter=0
                for listob in temprows:
                    for allinrow in rows[rowcounter]:
                        temprows[rowcounter].append(allinrow)
                    rowcounter=(rowcounter+1)

                colcounter=0
                for listob in tempcolumns:
                    for allincol in columns[colcounter]:
                        tempcolumns[colcounter].append(allincol)
                    colcounter=(colcounter+1)

                boxcounter=0
                for listob in tempboxes:
                    for allinbox in boxes[boxcounter]:
                        tempboxes[boxcounter].append(allinbox)
                    boxcounter=(boxcounter+1)

                for cell in cells:
                    if cell[0]==num:
                        for everyrow in temprows:
                            if cell in everyrow:
                                for everything in reversed(everyrow):
                                    for everycolumn in tempcolumns:
                                        if everything[0] != num:
                                            if everything in everycolumn:
                                                everycolumn.remove(everything)
                                    for everybox in tempboxes:
                                        if everything[0] != num:
                                            if everything in everybox:
                                                everybox.remove(everything)
                                    if everything[0] !=num:
                                        everyrow.remove(everything)

                        for everycolumn in tempcolumns:
                            if cell in everycolumn:
                                for everything in reversed(everycolumn):
                                    for everyrow in temprows:
                                        if everything[0] != num:
                                            if everything in everyrow:
                                                everyrow.remove(everything)
                                    for everybox in tempboxes:
                                        if everything[0] != num:
                                            if everything in everybox:
                                                everybox.remove(everything)
                                    if everything[0] !=num:
                                        everycolumn.remove(everything)

                        for everybox in tempboxes:
                            if cell in everybox:
                                for item in reversed(everybox):
                                    for everyrow in temprows:
                                        if item[0] != num:
                                            if item in everyrow:
                                                everyrow.remove(item)
                                    for everycolumn in tempcolumns:
                                        if item[0] != num:
                                            if item in everycolumn:
                                                everycolumn.remove(item)
                                    if item[0] !=num:
                                        everybox.remove(item)


                for row in temprows:
                    temp9=0
                    tempE=0
                    for number in row:
                        if number[0]==num:
                            temp9=(temp9+1)
                        if number[0]=='':
                            tempE=(tempE+1)
                    if temp9==0 and tempE==1:
                        for value in row:
                            if value[0]=='':
                                for thing in cells:
                                    if thing==value:
                                        thing[1]=[int(num),111]
                                        thing[0]=num
                                        break

                for column in tempcolumns:
                    temp9=0
                    tempE=0
                    for number in column:
                        if number[0]==num:
                            temp9=(temp9+1)
                        if number[0]=='':
                            tempE=(tempE+1)
                    if temp9==0 and tempE==1:
                        for value in column:
                            if value[0]=='':
                                for thing in cells:
                                    if thing==value:
                                        thing[1]=[int(num),222]
                                        thing[0]=num
                                        break


                for box in tempboxes:
                    temp9=0
                    tempE=0
                    for number in box:
                        if number[0]==num:
                            temp9=(temp9+1)
                        if number[0]=='':
                            tempE=(tempE+1)
                    if temp9==0 and tempE==1:
                        for value in box:
                            if value[0]=='':
                                for thing in cells:
                                    if thing==value:
                                        thing[0]=num
                                        thing[1]=[int(num),333]
                                        break


            def sudokusolve():
                check=0
                doublecheck=0
                for cell in cells:
                    if cell[0]=='':
                        check=(check+1)
                print(check)

                while check>doublecheck:

                    check=0
                    for cell in cells:
                        if cell[0]=='':
                            check=(check+1)


                    for cell in cells:
                        if cell[0]=='':
                            rowcheck(cell)
                        if cell[0]=='':
                            columncheck(cell)
                        if cell[0]=='':
                            boxcheck(cell)


                    solve9('9')
                    solve9('8')
                    solve9('7')
                    solve9('6')
                    solve9('5')
                    solve9('4')
                    solve9('3')
                    solve9('2')
                    solve9('1')
                    doublecheck=0

                    for cell in cells:
                        if cell[0]=='':
                            doublecheck=(doublecheck+1)
                    print(doublecheck)


        sudokusolve()



        args = {'form':form,"one":one[0],"two":two[0],"three":three[0],"four":four[0],"five":five[0],"six":six[0],"seven":seven[0],"eight":eight[0],"nine":nine[0],"ten":ten[0],"eleven":eleven[0],"twelve":twelve[0],"thirteen":thirteen[0],"fourteen":fourteen[0],"fifteen":fifteen[0],"sixteen":sixteen[0],"seventeen":seventeen[0],"eighteen":eighteen[0],"nineteen":nineteen[0],"twenty":twenty[0],"twentyone":twentyone[0],"twentytwo":twentytwo[0],"twentythree":twentythree[0],"twentyfour":twentyfour[0],"twentyfive":twentyfive[0],"twentysix":twentysix[0],"twentyseven":twentyseven[0],"twentyeight":twentyeight[0],"twentynine":twentynine[0],"thirty":thirty[0],"thirtyone":thirtyone[0],"thirtytwo":thirtytwo[0],"thirtythree":thirtythree[0],"thirtyfour":thirtyfour[0],"thirtyfive":thirtyfive[0],"thirtysix":thirtysix[0],"thirtyseven":thirtyseven[0],"thirtyeight":thirtyeight[0],"thirtynine":thirtynine[0],"fourty":fourty[0],"fourtyone":fourtyone[0],"fourtytwo":fourtytwo[0],"fourtythree":fourtythree[0],"fourtyfour":fourtyfour[0],"fourtyfive":fourtyfive[0],"fourtysix":fourtysix[0],"fourtyseven":fourtyseven[0],"fourtyeight":fourtyeight[0],"fourtynine":fourtynine[0],"fifty":fifty[0],"fiftyone":fiftyone[0],"fiftytwo":fiftytwo[0],"fiftythree":fiftythree[0],"fiftyfour":fiftyfour[0],"fiftyfive":fiftyfive[0],"fiftysix":fiftysix[0],"fiftyseven":fiftyseven[0],"fiftyeight":fiftyeight[0],"fiftynine":fiftynine[0],"sixty":sixty[0],"sixtyone":sixtyone[0],"sixtytwo":sixtytwo[0],"sixtythree":sixtythree[0],"sixtyfour":sixtyfour[0],"sixtyfive":sixtyfive[0],"sixtysix":sixtysix[0],"sixtyseven":sixtyseven[0],"sixtyeight":sixtyeight[0],"sixtynine":sixtynine[0],"seventy":seventy[0],"seventyone":seventyone[0],"seventytwo":seventytwo[0],"seventythree":seventythree[0],"seventyfour":seventyfour[0],"seventyfive":seventyfive[0],"seventysix":seventysix[0],"seventyseven":seventyseven[0],"seventyeight":seventyeight[0],"seventynine":seventynine[0],"eighty":eighty[0],"eightyone":eightyone[0]}
        return render(request, self.template_name, args)
#
# class solution(request):
#     if request.method == 'POST':
#         print('hello')
