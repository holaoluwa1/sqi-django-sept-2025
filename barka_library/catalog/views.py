from django.shortcuts import render, HttpResponse

# Create your views here.

def book_list(request):
    return HttpResponse('''<li>Half of a Yellow Sun</li>
                        <li>Things Fall Apart</li>
                       <li> Beloved</li>
                       <li> Life of Pi</li>
                       <li> The Kite Runner</li>''')
