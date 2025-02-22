from django.shortcuts import render

# Create your views here.
def chinhsach(request):
    return render(request,'chinhsach.html')


def data_deletion(request):
    return render(request, 'data_deletion.html')