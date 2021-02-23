from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
# from django.utils.text import slugify
# from ckeditor.fields import models.TextField

class CourseCategory(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class Course(models.Model):
    # slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='Thumbnail')
    course_name = models.CharField(max_length=100)
    course_category = models.ManyToManyField(CourseCategory)
    description = models.TextField()
    course_type = models.ForeignKey('Membership', on_delete=models.SET_NULL, null=True)
    certification = models.TextField()
    learning_outcome = models.TextField()
    instructor_name = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)

    # def super(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.course_name)
        
    #     return super(Course, self).save(*args, *kwargs)

    def __str__(self):
        return self.course_name

def pdf_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.course_name, filename)

class Lessons(models.Model):
    # slug = models.SlugField()
    lesson_title = models.CharField(max_length=100)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = EmbedVideoField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True, upload_to=pdf_directory_path)


    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    # def super(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.lesson_title)
        
    #     return super(Lessons, self).save(*args, **kwargs)

    def __str__(self):
        return self.lesson_title + " of " + str(self.course_name)

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.user.username

class Membership(models.Model):
    membership_type = models.CharField(max_length=20)

    def __str__(self):
        return self.membership_type
