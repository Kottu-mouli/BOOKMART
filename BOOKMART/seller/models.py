from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PDFDocument(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)  # Add this if not present
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title


