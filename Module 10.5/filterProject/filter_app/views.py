from django.shortcuts import render
import datetime

# Create your views here.

def geeksforgeeks(request):
    d = {
        'num' : 18,
        'st'  : "I'm Jai",
        'st2' : "jai",
        'st3' : "Jai",
        'st4' : "String with spaces.",
        'st5' : 'my FIRST post',
        'dateTime' : datetime.datetime.now(),
        'st6' : "",
        'dict' : [
                    {'name': 'zed', 'age': 19},
                    {'name': 'amy', 'age': 22},
                    {'name': 'joe', 'age': 31},
                ],
        'num2' : 21,
        'fileSize' : 123456789,
        'list1' : ['a', 'b', 'c'],
        'st7' : 'one\ntwo\nthree',
        'st8' : ' My Name is Jai',
        'st9' : 'Naveen',
        'st10' : ' Jai_/ is a slug ',
        'blog_date' : '12:00 1, June 2006',
        'comment_date' : '08:00, 1 June 2006',
        'list2' :  ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
        
        
    }
    return render(request, 'geeksforgeeks.html', context=d)

def earthly(request):
    d = {
        'list1' : ['a', 'b', 'c'],
        'list2' : ['python', 'is', 'fun'],
        'list3' : ['Monday', 'Tuesday', 'Wednesday'],
        'dateTimeStr' : datetime.datetime.now(),
        'emptyStr' : "",
        'num' : 10,
        'list4' : [1, 2, 3],
        'st1' : 'earthly',
        'st2' : 'django',
        'st3' : 'Python is Fun',
        'st4' : 'January - February - March',
        'list5' : [
                    {'name': 'Josh', 'age': 19},
                    {'name': 'Dave', 'age': 22},
                    {'name': 'Joe', 'age': 31},
                  ],
        'htmlStr' : '<p>You are <em>pretty</em> smart!</p>',
        'publication_date' : datetime.datetime(year = 2024, month = 7, day = 1, hour = 0, minute = 0, second = 0),
        'comment_date' : datetime.datetime(year = 2024, month = 7, day = 1, hour = 9, minute = 9, second = 0),
        'st5' : 'Moe is a slug',
        'st6' : 'Moe is a cat',
        'st7' : 'You can build web apps with python and Django',
        
        
    }
    return render(request, 'earthly.html', context=d)
