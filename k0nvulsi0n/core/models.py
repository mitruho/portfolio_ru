from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/', default='portfolio/default.png')
    gif = models.ImageField(upload_to='portfolio/gifs/', default='portfolio/default.png')
    body = models.TextField()
    website = models.URLField(blank=False)

    def __str__(self):
        return self.title
    
class ContactSubmission(models.Model):
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15, blank=True)  # Optional
    project_title = models.CharField(max_length=100)
    project_description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project_title} - {self.contact_email}"
