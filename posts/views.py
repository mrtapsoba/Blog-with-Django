from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.urls import reverse

items = [
    {"id": 1, "title": "Introduction", "content": "This is the introduction content."},
    {"id": 2, "title": "Chapter 1", "content": "This is the content of chapter 1."},
    {"id": 3, "title": "Conclusion", "content": "This is the conclusion content."}
]
# items = []

# Create your views here.
def home(request):
    html = ""
    for item in items:
        html += f'''
            <div>
                <a href="/posts/{item['id']}">
                    <h1>{item['id']} - {item['title']}</h1>
                    <p>{item['content']}</p>
                </a>
            </div>
        '''
    name = 'TAPS'
    return render(request, 'posts/home.html', {'name': name, 'list': items})

def post(request, id):
    valid_id = False
    for item in items:
        if item['id'] == id:
            item_dict = item
            valid_id = True
            break
    if valid_id :
        html = f'''
            <h1>{item_dict['title']}</h1>
            <p>{item_dict['content']}</p>
        '''
        #return HttpResponse(html)
        return render(request, 'posts/post.html', {'item': item_dict})
    else:
        return HttpResponseNotFound('Page indisponible')

def google(request, id):
    url = reverse('post', args=[id])
    return HttpResponseRedirect(url)