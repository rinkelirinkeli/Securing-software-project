from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import sqlite3


def login(request):
    # I will suppose that the request method is POST, just like we did in the exercises. 
    name = request.POST.get('username')
    passw = request.POST.get('password')

    user = User.objects.get(username=name)
    # FLAW 4: Cryptographic Flaw
    passwrd = user.password

    # FLAW 3: Identification and Authentication Failures
        # It is more secure to use Django's built-in features. This one allows brute force attacks. 
    if name==user and passw==passwrd:
        return HttpResponse("Login successful")
    else:
        # FLAW 5: Security Lonning and Monitoring Failures
            # The failed (possibly malicious) logs are not stored. 
            FailedLogins.objects.create(user=user, tried_passw=passwrd)
        return HttpResponse("Invalid username or password")




@login_required
def your_information(request):
    username = request.POST.get('username')
    conn = sqlite3.connect("arbitrary_data_storage_file")
    cursor = conn.cursor()
    #FLAW 2: Broken Access Control
        # We need to make sure that the user is actually authenticated to see the information accessible from the query. 
    # FLAW 1: SQL-injection
        
    # missing if-condition here (for flaw 2)
    response = cursor.execute(f"SELECT * FROM arbitrary_data_storage_file WHERE Username='{username}'").fetchall() 
    return HttpResponse(response)


