import openpyxl
from django.contrib.auth.models import User , auth
from samplepro.models import Document

def clean_data(request):
    user = User.objects.all()
    doc = Document.objects.all()
print(doc)



