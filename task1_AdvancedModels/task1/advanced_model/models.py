from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    Company_Choice_type =(
    ('1','One'),
    ('2','Two'),
    ('3','Three'),
    )
    name = models.CharField(max_length=200)
    company_type = models.CharField(max_length=3 ,choices =Company_Choice_type)

    companies = models.Manager()

    class Meta:
        verbose_name = "company"
        verbose_name_plural = "companies"

    def get_absolute_url(self):
        return reverse('company_details',kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
class Employee(models.Model):
    first_name=models.CharField(max_length=300)
    last_name =models.CharField(max_length=200)
    company =models.ForeignKey('Company',on_delete=models.CASCADE
                                ,related_name='employees',
                                related_query_name='person')
    # def company_display(self):
    #     return ' '.join([ company.name for company in self.company])
    #
    # company_display.short_description ='company'

    def get_absolute_url(self):
        return reverse('employee_details',kwargs={'pk':self.pk})
    def get_employee_company(self):
        return Company.companies.filter(person__first_name='mmg')
    def __str__(self):
        return self.first_name
