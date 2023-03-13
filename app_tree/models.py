from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Workers(MPTTModel):
    name = models.CharField(max_length=32, null=False)
    job_title = models.CharField(max_length=32)
    employment_date = models.DateTimeField(auto_now_add=True)
    salary = models.PositiveIntegerField()
    parent = TreeForeignKey('self', related_name='children',
                            on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='workers_images', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['employment_date']

    def __str__(self):
        return f' Name: {self.name} | Job-Title: {self.job_title} | Salary: {self.salary} $'
