from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, logout, login


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def register(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['firstName']
        ln = request.POST['lastName']
        e = request.POST['email']
        p = request.POST['password']
        c = request.POST['ContactNo']
        ab = request.POST['About']
        role = "ROLE_USER"

        try:
            user = User.objects.create_user(username=e, password=p, first_name=fn, last_name=ln)
            Signup.objects.create(user=user, ContactNo=c, About=ab, Role=role)
            error = "no"
        except:
            error = "yes"
    return render(request, 'register.html', locals())

def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'user_login.html', locals())

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)
    totalnotes = Notes.objects.filter(signup=signup).count()
    return render(request, 'dashboard.html', locals())

def profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)

    if request.method == "POST":

        fname = request.POST['firstName']
        lname = request.POST['lastName']
        contactNo = request.POST['ContactNo']
        about = request.POST['About']

        signup.user.first_name = fname
        signup.user.last_name = lname
        signup.ContactNo = contactNo
        signup.About = about

        try:
            signup.save()
            signup.user.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'profile.html', locals())

def addNotes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)

    error = ""
    if request.method == "POST":
        ReceivedOn = request.POST['ReceivedOn']
        PONo = request.POST['PONo']
        NameofSupplier = request.POST['NameofSupplier']
        BillNo = request.POST['BillNo']
        BillDate = request.POST['BillDate']
        Species = request.POST['Species']
        QtyinMT = request.POST['QtyinMT']
        BillValue = request.POST['BillValue']
        MIRONo = request.POST['MIRONo']
        GivenPaymentDate = request.POST['GivenPaymentDate']
        ActualPaymentDate = request.POST['ActualPaymentDate']
        AcceptReject = request.POST['AcceptReject']
        Remark = request.POST['Remark']

        try:
            Notes.objects.create(signup=signup, ReceivedOn=ReceivedOn, PONo=PONo, NameofSupplier=NameofSupplier, BillNo=BillNo, BillDate=BillDate, Species=Species, QtyinMT=QtyinMT, BillValue=BillValue, MIRONo=MIRONo, GivenPaymentDate=GivenPaymentDate, ActualPaymentDate=ActualPaymentDate, AcceptReject=AcceptReject, Remark=Remark)
            error = "no"
        except:
            error = "yes"
    return render(request, 'addNotes.html', locals())

def viewNotes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)
    notes = Notes.objects.filter(signup=signup)
    return render(request, 'viewNotes.html', locals())

def editNotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    notes = Notes.objects.get(id=pid)
    if request.method == "POST":
        ReceivedOn = request.POST['ReceivedOn']
        PONo = request.POST['PONo']
        NameofSupplier = request.POST['NameofSupplier']
        BillNo = request.POST['BillNo']
        BillDate = request.POST['BillDate']
        Species = request.POST['Species']
        QtyinMT = request.POST['QtyinMT']
        BillValue = request.POST['BillValue']
        MIRONo = request.POST['MIRONo']
        GivenPaymentDate = request.POST['GivenPaymentDate']
        ActualPaymentDate = request.POST['ActualPaymentDate']
        AcceptReject = request.POST['AcceptReject']
        Remark = request.POST['Remark']

        notes.ReceivedOn = ReceivedOn
        notes.PONo = PONo
        notes.NameofSupplier = NameofSupplier
        notes.BillNo = BillNo
        notes.BillDate = BillDate
        notes.Species = Species
        notes.QtyinMT = QtyinMT
        notes.BillValue = BillValue
        notes.MIRONo = MIRONo
        notes.GivenPaymentDate = GivenPaymentDate
        notes.ActualPaymentDate = ActualPaymentDate
        notes.AcceptReject = AcceptReject
        notes.Remark = Remark
        try:
            notes.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editNotes.html', locals())

def deleteNotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('viewNotes')

def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changePassword.html', locals())

def Logout(request):
    logout(request)
    return redirect('index')
