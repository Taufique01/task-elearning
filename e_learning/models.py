from django.db import models
from elearning import settings
# Create your models here.
class Course(models.Model):

    educator=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='course',on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Enrollment(models.Model):

    learner=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='enrollment',on_delete=models.CASCADE)
    course=models.ForeignKey(Course,related_name='enrollment',on_delete=models.CASCADE)

    class Meta:
        unique_together=('learner','course')

    def __str__(self):
        return str(self.course)
