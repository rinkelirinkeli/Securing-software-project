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
    passwrd = User.objects.get(password=passw)

    # FLAW 3: Identification and authentication failures
        # It is more secure to use Django's built-in features. 
    if name==user and passw==passwrd:
        return HttpResponse("Login successful")
    else:
        return HttpResponse("Invalid username or password")




@login_required
def information(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        conn = sqlite3.connect("arbitrary_data_storage_file")
        cursor = conn.cursor()
        #FLAW 2: Broken Access Control
            # We need to make sure that the user is actually authenticated to see the information accessible from the query. 
        # FLAW 1: SQL-injection
            
        # missing if-condition here (for flaw 2)
        response = cursor.execute(f"SELECT * FROM arbitrary_data_storage_file WHERE Username='{username}'").fetchall() 
        return HttpResponse(response)
    return 


