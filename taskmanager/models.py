from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Onprocess', 'Onprocess'),
        ('Completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    task_id=models.CharField(max_length=20)
    task_name=models.CharField(max_length=100)
    assigned_by=models.CharField(max_length=100)
    assigned_to=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES )
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.task_name 
class Screenshot(models.Model):
    task=models.ForeignKey(Task, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='screenshots/',blank=True,null=True)

    def __str__(self):
        return f'screenshot for {self.task.task_name}'
