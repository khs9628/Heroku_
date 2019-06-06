from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    image = models.ImageField(upload_to='image/', blank=True)
    

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    Blog_pk = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name ="comments")
    comment_text = models.CharField(max_length=50)

    def __str__(self):
        return self.comment_text