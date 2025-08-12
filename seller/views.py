from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from seller.models import PDFDocument


from django.db.models import Q
from .models import PDFDocument

def index(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    pdfs = PDFDocument.objects.all()

    if query:
        pdfs = pdfs.filter(Q(title__icontains=query) | Q(author__icontains=query))
    
    if category:
        pdfs = pdfs.filter(category__iexact=category)

    # Get unique categories for dropdown
    categories = PDFDocument.objects.values_list('category', flat=True).distinct()

    return render(request, 'index.html', {
        'pdfs': pdfs,
        'categories': categories,
        'selected_category': category,
        'query': query,
    })





@login_required(login_url='/account/login/')
def view_pdf_page(request, pk):
    pdf = get_object_or_404(PDFDocument, pk=pk)
    pdf_url = request.build_absolute_uri(pdf.pdf_file.url)  # Add this line
    return render(request, 'view_pdf_page.html', {'pdf': pdf, 'pdf_url': pdf_url})

# views.py
def index(request):
    selected = request.GET.get('category')
    if selected:
        pdfs = PDFDocument.objects.filter(category__iexact=selected)
    else:
        pdfs = PDFDocument.objects.all()
    
    categories = PDFDocument.objects.values_list('category', flat=True).distinct()
    return render(request, 'index.html', {
        'pdfs': pdfs,
        'categories': categories,
        'selected_category': selected
    })

