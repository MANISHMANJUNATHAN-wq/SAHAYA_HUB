from django.db import models

class HelpRequest(models.Model):
    CATEGORY_CHOICES = [
        ('Medical Emergency', 'Medical Emergency'),
        ('Food & Rations', 'Food & Rations'),
        ('Elderly Support', 'Elderly Support'),
        ('Community Help', 'Community Help'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Needs Help'),
        ('IN_PROGRESS', 'Volunteer Assigned'),
        ('RESOLVED', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Community Help')
    location = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=15)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.status})"