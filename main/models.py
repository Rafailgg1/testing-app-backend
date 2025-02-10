from django.db import models

class Application(models.Model):
    class Type(models.IntegerChoices):
        REFERENCE = 0
        IMAGE = 1
        VIDEO = 2
        
    FOLDER_Name = 'uploads'
    Upload_path = models.FileField(
        null=True, blank=True,
        upload_to = "uploads/%Y/%m/%d/",
    )
    
    application_type = models.IntegerField(
        choices=Type.choices,
        null=False, blank=True,
        # upload_to = Upload.path
    )
    application_file = models.FileField(
    null=True, blank=True,
    upload_to = "uploads/%Y/%m/%d/",
    )

    
    class Meta:
        verbose_name = "Приложение"
        verbose_name_plural = "Приложения"


class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title