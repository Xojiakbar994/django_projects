from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def WeekdaysEn(request):
    WeekEn = """
<h1>Days of Week</h1>
<ul> 
<li>Monday</li>      
<li>Tuesday</li>
<li>Wednesday</li>
<li>Thursday</li>
<li>Friday</li>
<li>Saturday</li>
<li>Sunday</li>
</ul>
"""
    return HttpResponse(WeekEn)


def WeekdaysUz(request):
    WeekUz = """
<h1>Hafta kunlari</h1>
<ul> 
<li>Dushanba</li>      
<li>Seshanba</li>
<li>Chorshanba</li>
<li>Payshanba</li>
<li>Juma</li>
<li>Shanba</li>
<li>Yakshanba</li>
</ul>
"""
    return HttpResponse(WeekUz)


def WeekdaysRu(request):
    WeekRu = """
<h1>Дни недели</h1>
<ul>
<li>Понедельник</li>      
<li>Вторник</li>
<li>Среда</li>
<li>Четверг</li>
<li>Пятница</li>
<li>Суббота</li>
<li>Воскресенье</li>
</ul>
"""
    return HttpResponse(WeekRu)