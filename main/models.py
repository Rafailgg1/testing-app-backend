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

class Test(models.Model):
    # question = models.CharField(max_length=255)
    # option1 = models.CharField(max_length=255)
    # option2 = models.CharField(max_length=255)
    # option3 = models.CharField(max_length=255)
    # option4 = models.CharField(max_length=255)
    # correct_answer = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='test_images/', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    question = models.CharField(max_length=500) 

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)  # Текст вопроса

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)  # Текст ответа
    is_correct = models.BooleanField(default=False)  # Правильный ответ

    def __str__(self):
        return self.text