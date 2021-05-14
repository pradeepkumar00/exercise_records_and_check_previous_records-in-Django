from django.shortcuts import render
from .models import exer
# Create your views here.

user_name=''
user_age=''
user_weight=''
def index(request):
    global user_age
    global user_weight
    global user_name
    if user_name == '':
        return render(request, 'get_pr.html')
    return render(request, 'index.html',{'name': user_name,'age': user_age, 'wt': user_weight})
def calculate(request):
    global user_age
    global user_weight
    global user_name
    if request.method == "POST":
        name = request.POST.get('name','')
        age = request.POST.get('age', '')
        wt = request.POST.get('wt', '')
        user_name = name
        user_age = age
        user_weight = wt
        return render(request, 'index.html', {'name': user_name, 'age': user_age, 'wt': user_weight})
    if user_name == '':
        return render(request, 'get_pr.html')
    return render(request, 'index.html', {'name': user_name, 'age': user_age, 'wt': user_weight})
def insert(request):
    global user_age
    global user_weight
    global user_name
    if request.method == "POST":
        ex = request.POST.get('ex', '')
        c = int(ex)
        try:
            d = int(user_weight)
        except:
            return render(request, 'index.html', {'name': user_name, 'age': user_age, 'wt': user_weight})
        if  d == 130:
            if c==1:
                ene = 472
            elif c==2:
                ene = 531
            elif c==3:
                ene = 590
            elif c==4:
                ene = 649
            elif c==5:
                ene = 679
            elif c==6:
                ene = 738
            elif c==7:
                ene = 797
            elif c==8:
                ene = 826
            elif c==9:
                ene = 885
            elif c==10:
                ene = 944
            elif c==11:
                ene = 1062
            elif c==12:
                ene = 531
            elif c==13:
                ene = 472
            elif c==14:
                ene = 590
            elif c==15:
                ene = 885
            elif c==16:
                ene = 236
            elif c==17:
                ene = 354
            else:
                ene = 590
        elif d == 155:
            if c==1:
                ene = 563
            elif c==2:
                ene = 633
            elif c==3:
                ene = 704
            elif c==4:
                ene = 774
            elif c==5:
                ene = 809
            elif c==6:
                ene = 880
            elif c==7:
                ene = 950
            elif c==8:
                ene = 985
            elif c==9:
                ene = 1056
            elif c==10:
                ene = 1126
            elif c==11:
                ene = 1267
            elif c==12:
                ene = 633
            elif c==13:
                ene = 563
            elif c==14:
                ene = 704
            elif c==15:
                ene = 1056
            elif c==16:
                ene = 281
            elif c==17:
                ene = 422
            else:
                ene = 704
        elif d == 180:
            if c==1:
                ene = 654
            elif c==2:
                ene = 735
            elif c==3:
                ene = 817
            elif c==4:
                ene = 899
            elif c==5:
                ene = 940
            elif c==6:
                ene = 1022
            elif c==7:
                ene = 1103
            elif c==8:
                ene = 1144
            elif c==9:
                ene = 1226
            elif c==10:
                ene = 1308
            elif c==11:
                ene = 1471
            elif c==12:
                ene = 735
            elif c==13:
                ene = 654
            elif c==14:
                ene = 817
            elif c==15:
                ene = 1226
            elif c==16:
                ene = 327
            elif c==17:
                ene = 490
            else:
                ene = 817
        else:
            if c==1:
                ene = 745
            elif c==2:
                ene = 838
            elif c==3:
                ene = 931
            elif c==4:
                ene = 1024
            elif c==5:
                ene = 1070
            elif c==6:
                ene = 1163
            elif c==7:
                ene = 1256
            elif c==8:
                ene = 1303
            elif c==9:
                ene = 1396
            elif c==10:
                ene = 1489
            elif c==11:
                ene = 1675
            elif c==12:
                ene = 838
            elif c==13:
                ene = 745
            elif c==14:
                ene = 931
            elif c==15:
                ene = 1396
            elif c==16:
                ene = 372
            elif c==17:
                ene = 558
            else:
                ene = 931
        import datetime
        time  = datetime.datetime.now()
        date = str(time.strftime("%d"))
        mm = str(time.strftime("%m"))
        year = str(time.strftime("%Y"))
        cred = exer(name=user_name, age=user_age, wt=user_weight, energy=ene, date=date, mm=mm, year=year)
        cred.save()
        return render(request, 'insert.html',{'name': user_name, 'age': user_age, 'wt': user_weight, 'ene': ene})
    if user_name == '':
        return render(request, 'get_pr.html')
    return render(request, 'index.html', {'name': user_name, 'age': user_age, 'wt': user_weight})
def new(request):
    global user_age
    global user_weight
    global user_name
    if request.method == "POST":
        st = request.POST.get('sd')
        ed = request.POST.get('ed')
        sy = int(st[:4])
        ey = int(ed[:4])
        sm = int(st[5:7])
        em = int(ed[5:7])
        sd = int(st[8:10])
        sf = int(ed[8:10])
        all_data = exer.objects.all()
        list = []
        for item in all_data:
            y=int(item.year)
            m=int(item.mm)
            if item.name == user_name:
                if y>sy and y<ey:
                    s = item.energy
                    m = str(y) + '  ' + str(m) + '  ' +item.date + '  ' + s
                    list.append(m)
                elif y==sy and y==ey:
                    if m>=sm and m<=em:
                        s = item.energy
                        m = str(y) + '  ' + str(m) + '  ' + item.date + '  ' + s
                        list.append(m)
                elif y==sy and y<ey:
                    if m>=sm:
                        s = item.energy
                        m = str(y) + '  ' + str(m) + '  ' + item.date + '  ' + s
                        list.append(m)
                elif y>sy and y==ey:
                    if m<=em:
                        s = item.energy
                        m = str(y) + '  ' + str(m) + '  ' + item.date + '  ' + s
                        list.append(m)
        param = {'list': list,'name': user_name, 'age': user_age, 'wt': user_weight}
        user_name =''
        user_age=''
        user_weight=''
        return render(request, 'new.html', param)
    return render(request,'get_pr.html')
