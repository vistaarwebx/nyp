from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from youth.models import *
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from nyp.settings import EMAIL_HOST_USER
from nyp.settings import account_sid,auth_token,my_twilio
from twilio.rest import Client
import datetime


def LOGIN(request):
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['user']
        p = d['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = True
    d = {'error': error}
    return render(request, "login.html", d)

def LOGOUT(request):
    logout(request)
    return redirect('home')


def Home(request):
    images  = Facebook.objects.all().order_by('-id')
    img = images[:6]
    campsfi = Posts.objects.all().order_by('-id')
    camps = campsfi[:4]
    books = Books.objects.all().order_by('-id')
    book = books[:4]
    pros = Press.objects.all().order_by('-id')
    pr = pros[:4]
    if request.method == "POST":
        if 'facebook' in request.POST:
            c = request.POST
            img = c['image']
            Facebook.objects.create(image=img)
            return redirect('home')
        
    d= {"img":img,"camps":camps,"book":book,"pr":pr}
    return render(request,'index.html',d)

def TERMS_COND(request):
    if request.method == "POST":
        d = request.POST
        value = d['val']
        request.session['val']=value
        return redirect('unitregistration')
    return render(request,'termsNYP.html')   

def Email(request):
    li =[]
    em1 = Member.objects.all()
    em2 = Groupadmin.objects.all()
    for i in em1:
        li.append(i.memEmail)
    for i in em2:
        li.append(i.Email)

    if request.method == "POST":
        d= request.POST
        subject = d['sub']
        content = d['msg']
        email = li
        msg = EmailMultiAlternatives(subject, content, EMAIL_HOST_USER,email)
        msg.send()
    return render(request,'email.html')

def Unitregistration(request):
    error = False
    aot = request.session['val']
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    li =  []
    for i in a:
        if int(aot) >= i:
            li.append(i)
    if request.method == "POST":
        d = request.POST
        n = d['tname']
        na = d['adname']
        sur = d['qadsur']
        mo = d['areacod']+d['admob']
        em = d['ademail']
        add = d['adadd']
        ci = d['adcity']
        add2 = d['addr2']
        sta = d['state']
        pin = d['block']
        coun = d['count']
        age = d['age']
        grpimg = d['imagegrp']
        amimg = d['adminimg']

        #age validation#
        s = 'age = ', age, 'senior citizen'
        j = 'age = ', age, 'junior citizen'
        arr = []
        if int(age) >= 30:
            arr.append(s)
        else:
            arr.append(j)
        ##age boundation end##
            ##  no repeat block ##
        if Groupadmin.objects.filter(Block=pin).exists():
            error = True
            ##  no repeat block end ##
        else:
            grp = Group.objects.create(name=n,image=grpimg)
            g_admin = Groupadmin.objects.create(Block=pin, State=sta, Address2=add2, grpsurname=sur, group=grp, grpName=na,
                                                Mobile=mo, Email=em, Address=add, City=ci, Country=coun, age=arr,image=amimg,)
            for i in li:
                memnam = request.POST['membername' + str(i)]
                po = request.POST['position' + str(i)]
                ag = request.POST['Age' + str(i)]
                edu = request.POST['Education' + str(i)]
                occ = request.POST['Occupation' + str(i)]
                mobil = request.POST['Mobile' + str(i)]
                ma = request.POST['mail' + str(i)]
                email = request.POST['mail' + str(i)]
                subject = "successfully registred to national youth project "
                content = "Congurlation you have successfully registred for the National youth project "
                msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
                msg.send()
               
                Member.objects.create(group_admin=g_admin, memName=memnam, memAge=ag, memMobile=mobil, memEmail=ma,
                                      memeducation=edu, memoccupation=occ, memposition=po)

        my_cell = mo
        client = Client(account_sid, auth_token)
        my_msg = "Congurlations you are successfully registred"
        message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
        email = em
        subject = "successfully registred to national youth project "
        content = "Congurlation", na, "you and your group", n, "has successfully registred for the National youth project Download your certificate "
        msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
        d = {'name': na, 'gname': n}
        html = get_template('certificate.html').render(d)
        msg.attach_alternative(html, 'text/html/css/js')
        msg.send()
        return redirect('home')
    dic = {'li': li,'error':error}
    return render(request,'unitregistration.html',dic)

def Video(request):
    return render(request, 'videos.html')

def Media(request):
    if request.method == "POST":
        d = request.POST
        tit = d['title']
        Videos.objects.create(video=tit)
    vid =  Videos.objects.all()
    d = {"vid":vid}
    return render(request, 'MEDIA.html',d)


def POST(request,po_id):
    pot = Posts.objects.get(id=po_id)
    d ={"pot":pot}
    return render(request, 'post.html',d)

def BOOK(request):
    if request.method == "POST":
        d = request.POST
        tit = d['title']
        aut = d['author']
        dat = d['date']
        img = d['image']
        par = d['para']
        Books.objects.create(title=tit, author=aut, image=img, para=par,date=dat)
    books =  Books.objects.all().order_by('-id')
    d ={"books":books}
    return render(request, 'booksfull.html',d)

def SingleBook(request,bu_id):
    buk =  Books.objects.get(id= bu_id)
    d ={"buk":buk}
    return render(request, 'booksingle.html',d)

def CAMPS(request):
    if request.method == "POST":
        d = request.POST
        tit = d['title']
        dat = d['date']
        img = d['image']
        par = d['para']
        Posts.objects.create(title=tit, image=img, para=par,date=dat)
    post =  Posts.objects.all().order_by('-id')
    d ={"post":post}
    return render(request, 'allcamp.html',d)

def PRESS(request):
    if request.method == "POST":
        d = request.POST
        tit = d['title']
        dat = d['date']
        img = d['image']
        par = d['para']
        Press.objects.create(title=tit, image=img, para=par,date=dat)
    post =  Press.objects.all().order_by('-id')
    d ={"post":post}
    return render(request, 'allpress.html',d)

def PRESS_single(request,pr_id):
    pot = Press.objects.get(id=pr_id)
    d ={"pot":pot}
    return render(request, 'singlepress.html',d)

def NYP_SINGLE(request,nys_id):
    nypob = Group.objects.get(id=nys_id)
    grpadmin = Groupadmin.objects.filter(group= nypob).first()
    member = Member.objects.filter(group_admin = grpadmin)
    d ={"nypob":nypob,"grpadmin":grpadmin,"member":member}
    return render(request, 'single_page_nyp.html',d)
def VOLUNTEER_SINGLE(request,vos_id):
    volsingle = VOLUNTEERS.objects.get(id=vos_id)
    d ={"volsingle":volsingle}
    return render(request, 'single_page_volunteer.html',d)
def JOB_SINGLE(request,jos_id):
    jobsingle = JOBINTERNSHIP.objects.get(id=jos_id)
    d ={"jobsingle":jobsingle}
    return render(request, 'single_page_job.html',d)            


def CONTACT(request):
    if request.method == "POST":
        d = request.POST
        NAMEE = d['name']
        EMAI = d['mail']
        Subj = d['sub']
        MESSAH = d['msg']
        contact.objects.create(name=NAMEE,subject=Subj,message=MESSAH,Email=EMAI)
    return render(request, 'contact.html')


def GALLERY(request):
    if request.method == "POST":
        d = request.POST
        tit = d['title']
        img = d['image']
        Gallery.objects.create(title=tit,image=img)
    post =  Gallery.objects.all().order_by('-id')
    d = {"post": post}
    return render(request, 'gallery.html',d)

def ABOUTDR(request):
    return render(request,'about_dr_subbarao.html')  
def WHOWEARE(request):
    return render(request,'who_we_are.html') 
def OURTEAM(request):
    return render(request,'our_team.html') 
def VISIONMISSION(request):
    return render(request,'vision_mission.html')               

def ADINDEX(request):
    contc = contact.objects.all().order_by('-id')
    volfal = VOLUNTEERS.objects.filter(is_published='deactivated')
    volunteer = VOLUNTEERS.objects.filter(is_published='activated')
    jobde = JOBINTERNSHIP.objects.filter(is_published='deactivated')
    jobactivate = JOBINTERNSHIP.objects.filter(is_published='activated')
    nypactive = Group.objects.filter(is_published='activated')
    nypdeactive = Group.objects.filter(is_published='deactivated')
    d = {"contc":contc,"volunteer":volunteer,"volfal":volfal,"jobde":jobde,"jobactivate":jobactivate,"nypactive":nypactive,"nypdeactive":nypdeactive}
    return render(request, 'admin_index.html',d)

def VOLUNTEER_ACTIVATE(request, pk):
    published_item = get_object_or_404(VOLUNTEERS,pk=pk)
    datte = get_object_or_404(VOLUNTEERS,pk=pk)
    dat = datetime.date.today()
    datte.activatedate= dat
    published_item.is_published = 'activated' if published_item.is_published == 'deactivated' else 'deactivated'
    published_item.save(update_fields=['is_published'])
    datte.save(update_fields= ['activatedate'])
    return redirect('admin_index')

def JOB_ACTIVATE(request,pk):
    published_item = get_object_or_404(JOBINTERNSHIP,pk=pk)
    datte = get_object_or_404(JOBINTERNSHIP,pk=pk)
    dat = datetime.date.today()
    datte.activatedate= dat
    published_item.is_published = 'activated' if published_item.is_published == 'deactivated' else 'deactivated'
    published_item.save(update_fields=['is_published'])
    datte.save(update_fields= ['activatedate'])
    return redirect('admin_index')

def NYP_ACTIVATE(request,pk):
    published_item = get_object_or_404(Group,pk=pk)
    datte = get_object_or_404(Group,pk=pk)
    dat = datetime.date.today()
    datte.activatedate= dat
    published_item.is_published = 'activated' if published_item.is_published == 'deactivated' else 'deactivated'
    published_item.save(update_fields=['is_published'])
    datte.save(update_fields= ['activatedate'])
    return redirect('admin_index')


def BOOK_delete(request,fb_id):
    po = Books.objects.get(id=fb_id).delete()
    return redirect("book")
def CAMP_delete(request,ca_id):
    po = Posts.objects.get(id=ca_id).delete()
    return redirect("camps")
def PRESS_delete(request,pr_id):
    po = Press.objects.get(id=pr_id).delete()
    return redirect("press")    
def MEDIA_delete(request,me_id):
    po = Videos.objects.get(id=me_id).delete()
    return redirect("media") 
def GALLERY_delete(request,ga_id):
    po = Gallery.objects.get(id=ga_id).delete()
    return redirect("gallery")  
def VOLUNTEER_delete(request,vo_id):
    po = VOLUNTEERS.objects.get(id=vo_id).delete()
    return redirect("admin_index")      
def JOB_delete(request,jd_id):
    po = JOBINTERNSHIP.objects.get(id=jd_id).delete()
    return redirect("admin_index")  
def NYP_delete(request,ny_id):
    po = Group.objects.get(id=ny_id).delete()
    return redirect("admin_index") 

def JOB_INTERNSHIP(request):
    if request.method == "POST":
        d = request.POST
        area = d['area']
        desired = d['desired']
        starting = d['starting']
        brief = d['brief']
        first = d['first']
        last = d['last']
        ema = d['ema']
        Mobile = d['Mobile']
        adhar = d['adhar']
        gend = d['gend']
        dob = d['dob']
        add1 = d['add1']
        addres2 = d['addd2']
        cit = d['cit']
        sta = d['sta']
        blo = d['blo']
        count = d['count']
        about = d['about']
        cvv = d['RESUME']
        imageeff = d['img']
        JOBINTERNSHIP.objects.create(area_of_intrest=area,desired_duration=desired,starting_month=starting,brief_detail=brief,first_name=first,last_name=last,email=ema,Mobile_no=Mobile,adhar_no=adhar,gender=gend,date_of_birth=dob,address1=add1,address2=addres2,city=cit,state=sta,block=blo,country=count,about_you=about,resume=cvv,image=imageeff,)
        return redirect('home')
    return render(request,'job_internship.html') 
def VOLUNTEER(request):
    if request.method == "POST":
        d = request.POST
        first = d['first']
        last = d['last']
        ema = d['ema']
        Mobile = d['Mobile']
        adhar = d['adhar']
        gend = d['gend']
        dob = d['dob']
        edu = d['EDUC']
        add1 = d['add1']
        addres2 = d['addd2']
        cit = d['cit']
        sta = d['sta']
        blo = d['blo']
        count = d['count']
        org = d['anyorgin']
        camp = d['nypcamp']
        about = d['about']
        upimg = d['img']
        VOLUNTEERS.objects.create(first_name=first,last_name=last,email=ema,Mobile_no=Mobile,adhar_no=adhar,gender=gend,date_of_birth=dob,education=edu,address1=add1,address2=addres2,city=cit,state=sta,block=blo,country=count,any_organization=org,nyp_camp=camp,image=upimg,about_you=about,)
        return redirect('home')
    return render(request,'volunteer.html')  

def UNIT_REQUEST(request):
    EXPIRED1 = Group.objects.filter(activatedate__lte=datetime.date.today()-datetime.timedelta(days=365))
    for i in EXPIRED1:
        i.is_published='deactivated'
        i.save()
    nypdeactive = Group.objects.filter(is_published='deactivated')
    return render(request,'unit_request.html',{"nypdeactive":nypdeactive})  
def ACTIVE_UNITS(request):
    nypactive = Group.objects.filter(is_published='activated')
    return render(request,'active_units.html',{"nypactive":nypactive})   
def VOLUNTEER_REQUEST(request):
    volfal = VOLUNTEERS.objects.filter(is_published='deactivated')
    return render(request,'volunteer_request.html',{"volfal":volfal})  
def ACTIVE_VOLUNTEER(request):
    volunteer = VOLUNTEERS.objects.filter(is_published='activated')
    return render(request,'active_volunteers.html',{"volunteer":volunteer}) 
def JOB_REQUEST(request):
    jobde = JOBINTERNSHIP.objects.filter(is_published='deactivated')
    return render(request,'jobss_request.html',{"jobde":jobde})  
def ACTIVE_JOB(request):
    jobactivate = JOBINTERNSHIP.objects.filter(is_published='activated')
    return render(request,'active_jobss.html',{"jobactivate":jobactivate})                         