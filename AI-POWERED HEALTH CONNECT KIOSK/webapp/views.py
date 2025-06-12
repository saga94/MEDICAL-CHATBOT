from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from .Graphs import viewg


from .models import *
import openpyxl
from .tf import tf

from django.db.models import Q
from .Prediction import Prediction
from .RandomGen import getnum


# Create your views here.
def home(request):
	request.session["bookdoc"]=''
	request.session["di"]=''
	return render(request, 'index.html')

def user(request):
    return render(request, 'user.html', {'b':False})

def usersignup(request):
    return render(request, 'user.html', {'b':True})



def doctor(request):
    return render(request, 'doctor.html', {'b':False})

def doctorsignup(request):
	d=dataset.objects.values('Specialist').distinct()
	l=[]
	for d1 in d:
		l.append(d1['Specialist'])
	return render(request, 'doctor.html', {'b':True, 'data':l})

def usignupaction(request):
    if request.method == 'POST':
        email = request.POST['mail']

        d = users.objects.filter(email__exact=email).count()
        if d > 0:
            return render(request, 'user.html', {'msg': "Email Already Registered"})
        else:

            pass_word = request.POST['pass_word']
            phone = request.POST['phone']
            city = request.POST['city']
            name = request.POST['name']
            age = request.POST['age']
            gen = request.POST['gen']

            d = users(name=name, email=email, pass_word=pass_word, phone=phone, gender=gen, city=city,  age=age)
            d.save()

        return render(request, 'user.html', {'msg': "Register Success, You can Login.."})

    else:
        return render(request, 'user.html')

def dsignupaction(request):
    if request.method == 'POST':
        email = request.POST['mail']

        d = doctors.objects.filter(email__exact=email).count()
        if d > 0:
            return render(request, 'doctor.html', {'msg': "Email Already Registered"})
        else:

            name = request.POST['name']
            pass_word = request.POST['pass_word']
            phone = request.POST['phone']
            qua = request.POST['qua']
            specialist = request.POST['specialist']
    
            d = doctors(name=name, email=email, password=pass_word, contact=phone, qualification=qua, Specialist=specialist)
            d.save()

        return render(request, 'doctor.html', {'msg': "Register Success, You can Login.."})

    else:
        return render(request, 'doctors.html')
    


def userloginaction(request):
    if request.method=='POST':
        uid=request.POST['mail']
        pass_word=request.POST['pass_word']
        d=users.objects.filter(email__exact=uid).filter(pass_word__exact=pass_word).count()
        
        if d>0:
            d=users.objects.filter(email__exact=uid)
            request.session['email']=uid
            request.session['name']=d[0].name
         
         
            return render(request, 'user_home.html',{'data': d[0]})

        else:
            return render(request, 'user.html',{'msg':"Login Fail"})

    else:
        return render(request, 'user.html')
    
def dloginaction(request):
    if request.method=='POST':
        uid=request.POST['mail']
        pass_word=request.POST['pass_word']
        d=doctors.objects.filter(email__exact=uid).filter(password__exact=pass_word).count()
        
        if d>0:
            d=doctors.objects.filter(email__exact=uid)
            request.session['demail']=uid
            request.session['dname']=str('Dr. ')+d[0].name
            doctors.objects.filter(email__exact=uid).update(stz='online')


         
         
            return render(request, 'd_home.html',{'data': d[0]})

        else:
            return render(request, 'doctor.html',{'msg':"Login Fail"})

    else:
        return render(request, 'doctor.html')
    


def userlogoutdef(request):
    try:
        del request.session['email']
    except:
        pass
    return render(request, 'user.html')

def dlogoutdef(request):
    try:
        doctors.objects.filter(email__exact=request.session['demail']).update(stz='offline')
        del request.session['demail']
    except:
        pass
    return render(request, 'doctor.html')


def userhomedef(request):
    if "email" in request.session:
        email=request.session["email"]
        d=users.objects.filter(email__exact=email)

       
        return render(request, 'user_home.html',{'data': d[0]})

    else:
        return redirect('userlogoutdef')


def dhomedef(request):
    if "demail" in request.session:
        demail=request.session["demail"]
        d=doctors.objects.filter(email__exact=demail)

       
        return render(request, 'd_home.html',{'data': d[0]})

    else:
        return redirect('dlogoutdef')


def adminlogin(request):
    return render(request, 'admin.html')


def adminloginaction(request):
    userid=request.POST['aid']
    pwd=request.POST['pwd']
    print(userid, pwd,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    if userid=='admin' and pwd=="admin":
        request.session['adminid']='admin'
        return render(request, 'adminhome.html')
    else:
        err='Your Login Data is wrong !!' 
        return render(request, 'admin.html',{'msg':err})

def adminhome(request):
	d = dataset.objects.filter(Specialist='').delete()
	return render(request, 'adminhome.html')


def adminlogout(request):
    return render(request, 'admin.html')

def upload(request):
    return render(request, 'upload.html')



def training(request):
    return render(request, 'training.html')


def nbtrain(request):
    from .Training import Training
    Training.train('nb')

    return render(request, 'training.html', {'msg':"Naive Bayes Algorithm's training completed"})

def rftrain(request):
    from .Training import Training
    Training.train('rf')
    return render(request, 'training.html', {'msg':"Random Forest Algorithm's training completed"})

def svmtrain(request):
    from .Training import Training
    Training.train('svm')
    return render(request, 'training.html', {'msg':"SVM Algorithm's training completed"})

def nntrain(request):
    from .Training import Training
    Training.train('nn')
    return render(request, 'training.html', {'msg':"Neural Networks Algorithm's training completed"})
def testing(request):
	d=performance.objects.all()
	d.delete()
	from .Testing import Testing
	sc=Testing('nb.sav','Testing.csv')
	d=performance(alg_name='Naive Bayes', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
	d.save()
	sc=Testing('nn.sav','Testing.csv')
	
	d=performance(alg_name='Neural Networks', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
	d.save()
	sc=Testing('svm.sav','Testing.csv')
	d=performance(alg_name='SVM', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
	d.save()
	
	sc=Testing('rf.sav','Testing.csv')
	d=performance(alg_name='Random Forest', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
	d.save()
	return render(request, 'training.html', {'msg':"Testing process completed"})



def viewacc(request):

    d=performance.objects.all()
    val={}
    for d1 in d:
        val[d1.alg_name]=d1.sc1
    viewg(val)
    return render(request, 'viewacc.html', {'data': d})



import csv
def upload1(request):
    if "adminid" in request.session:
        file = request.POST['file']
        file = file
        d = dataset.objects.all().delete()
        with open(file, 'r') as fin:
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin)  # comma is default delimiter
            to_db = [(i['Symptoms'], i['Causes'],i['Disease'],i['Medicine'],i['Specialist']) for i in dr]
            for l in to_db:
                d = dataset(Symptoms=l[0], Causes=l[1], Disease=l[2], Medicine=l[3], Specialist=l[4])
                d.save()
		
		

        return render(request, 'upload.html', {'msg': "Dataset Uploaded Successfully"})

    else:
        return render(request, 'adminlogin.html')


def adddata(request):
    if "adminid" in request.session:
        d = queries.objects.all()
        
        return render(request, 'adddata.html', {'data': d})

    else:
        return render(request, 'admin.html')




def addquery(request):
    q=request.POST['q']
    a=request.POST['a']
    
        
    d=queries(q_n=q,an_s=a)
    d.save()
    
    d = queries.objects.all()
    return render(request, 'adddata.html', {'data': d,'msg':'Query Added.'})





def chatpage(request):
    
    chat.objects.all().delete()
    
    d=chat.objects.filter().all()
    return render(request, 'chat.html',{'data': d})


def chataction(request):
    message=request.POST['message']
    d=chat(name=request.session['name'],email=request.session['name'],message=message)
    d.save()
    message=message.replace('.' ,'') 
    m=message.split(',')


    ans='Sorry, Not Understood' 
    cid=tf.calc(message)
    if cid!=- 1:
        d=queries.objects.filter(id__exact=cid)
        for d1 in d:
            ans=d1.an_s

        d=chat(name='chatbot',email='chatbot',message=ans)
        d.save()

        d=chat.objects.filter().all()
        return render(request, 'chat.html',{'data': d})


    else:

        r=Prediction.do(message)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',r)
        request.session['disease']=r
        ans="Based on your symptoms, expected disease is "+r
        d=chat(name='chatbot',email='chatbot',message=ans)
        d.save()
        ans="Your having this symptoms more than day (Yes or No) "
        d=chat(name='chatbot',email='chatbot',message=ans)
        d.save()

    # d2=dataset.objects.filter(Disease=r)
    # spe=d2[0]

    d=chat.objects.filter().all()

    return render(request, 'chat.html',{'data': d,'bt':True})



def option(request, op):
    print(op,'<<<<<<<<<<<<')
    disease=request.session['disease']
    if op=='yes': 
        d=dataset.objects.filter(Disease=disease)
        spe=d[0].Specialist
        doc=doctors.objects.filter(Specialist=spe).filter(stz='online')
        if len(doc)>0:
            d=chat.objects.filter().all()
            return render(request, 'chat.html',{'data':d,'doc':doc,'bt2':True})
        else:
            ans="There are no '"+spe+"' doctors available at this time."
            d=chat(name='chatbot',email='chatbot',message=ans)
            d.save()
            d=chat.objects.filter().all()
            return render(request, 'chat.html',{'data': d})
    else:
        d=dataset.objects.filter(Disease=disease)
        med=d[0].Medicine
        ans="Take medicine,\n"+med
        print(ans)
        d=chat(name='chatbot',email='chatbot',message=ans)
        d.save()
        d=chat.objects.filter().all()
        return render(request, 'chat.html',{'data' : d})
    


def chatdoctor(request):
    name=request.session['name']
    email=request.session['email']

    docname=request.POST['docname']

    docemail=request.POST['docemail']

    d=docchat(name=name, email=email, chatbw=str(email+'|'+docemail), message='Hello doctor', stz='new' )
    d.save()
    d=chat(name='chatbot',email='chatbot',message="Message sent to doctor !! \nGo for 'Messages' option. ")
    d.save()
    d=chat.objects.filter().all()
    return render(request, 'chat.html',{'data' : d})






def viewdoc(request):
    if "adminid" in request.session:
        d = doctors.objects.all()
        
        return render(request, 'viewdoc.html', {'data': d})

    else:
        return render(request, 'admin.html')





def dchatpage(request):
    dname=request.session['dname']
    demail=request.session['demail']

    combo=docchat.objects.filter(chatbw__icontains=demail).filter(stz='new').values('name', 'email').distinct().exclude(email=demail)
    d=[]
    for c in combo:
        d.append({'name':c['name'], 'email':c['email'] })
    
    return render(request, 'dchatpage.html', {'data': d})
    

def dchat(request):
    pemail=request.GET['pemail']
    demail=request.session['demail']

    c1=pemail+"|"+demail
    c2=demail+"|"+pemail

    #d=docchat.objects.filter(Q(chatbw=c1) | Q(chatbw=c2)).update('stz')

    d=docchat.objects.filter(Q(chatbw=c1) | Q(chatbw=c2))
    

    
    return render(request, 'dchat.html', {'data': d, 'pemail':pemail})
    





def dchataction(request):
    pemail=request.POST['pemail']
    msg=request.POST['message']
    demail=request.session['demail']
    dname=request.session['dname']

    c1=pemail+"|"+demail
    c2=demail+"|"+pemail
    d=docchat(name=dname, email=demail, message=msg, chatbw=c2, stz='new')
    d.save()


    d=docchat.objects.filter(Q(chatbw=c1) | Q(chatbw=c2))

    
    return render(request, 'dchat.html', {'data': d, 'pemail':pemail})
    







def pchatpage(request):
    pname=request.session['name']
    pemail=request.session['email']

    combo=docchat.objects.filter(chatbw__icontains=pemail).filter(stz='new').values('name', 'email').distinct().exclude(email=pemail)
    d=[]
    for c in combo:
        d.append({'name':c['name'], 'email':c['email'] })
    
    return render(request, 'pchatpage.html', {'data': d})
    


def pchat(request):
    demail=request.GET['demail']
    pemail=request.session['email']

    c1=pemail+"|"+demail
    c2=demail+"|"+pemail

    #d=docchat.objects.filter(Q(chatbw=c1) | Q(chatbw=c2)).update('stz')

    d=docchat.objects.filter(Q(chatbw=c1) | Q(chatbw=c2))
    

    
    return render(request, 'pchat.html', {'data': d, 'demail':demail})
    




def pchataction(request):
    demail=request.POST['demail']
    msg=request.POST['message']
    pemail=request.session['email']
    name=request.session['name']

    c1=pemail+"|"+demail
    c2=demail+"|"+pemail
    d=docchat(name=name, email=pemail, message=msg, chatbw=c1, stz='new')
    d.save()


    d=docchat.objects.filter(Q(chatbw=c1) | Q(chatbw=c2))

    
    return render(request, 'pchat.html', {'data': d, 'demail':demail})
    



def getmesg(request):
    from .speech import main
    main('/Users/punnasaiganesh/SAIGANESH/PROJECTS/MAJOR PROJECT/MedicalChatbot/msg.txt')
    return redirect('chatpage2')

def chatpage2(request):  
    f1=open('msg.txt')
    msg=f1.read()
    d=chat.objects.filter().all()
    return render(request, 'chat.html',{'data': d,'msg': msg})



