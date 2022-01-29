from django.shortcuts import render

# Create your views here.

def upload_file_view(request):
    return render(request, 'csvs/upload.html', {})