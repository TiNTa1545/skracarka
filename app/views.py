from django.shortcuts import render, redirect

# Create your views here.
from app.models import Link

def index(request):
    if request.method == 'POST':
        link = request.POST['link']
        shortened = Link.objects.create(target=link)
        return render(
            request,
            'shortened.html',
            {"short_link": f"http://localhost:8000/{shortened.id}/"}
        )
        # Zapisz URL i zwróć skrócony
    else:
        return render(request, 'index.html')

def przekierowanko(request, link_id):
    link = Link.objects.get(id=link_id)
    link.count += 1
    link.save()
    return redirect(link.target)


def list_of_links(request):
    return render(request, 'list.html', { 'links': Link.objects.all() })