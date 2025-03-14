from django.db import models
from django.conf import settings
from PIL import Image
# Create your models here.
class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=100, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    IMAGE_SIZE = (300, 300)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
        
    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_SIZE)
        image.save(self.image.path)


class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    word_count = models.IntegerField(null=True)

    def _get_word_count(self):
        return len(self.content.split(' '))

    def save(self, *args, **kwargs):
        self.word_count = self._get_word_count()
        super().save(*args, **kwargs)