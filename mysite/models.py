from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.


class Site(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    languages = models.CharField(max_length=100, choices=[('عربي', 'عربي'), ('إنجليزي', 'إنجليزي'), ('عربي, إنجليزي', 'عربي, إنجليزي')])
    favorites = models.PositiveIntegerField(default=0)
    addedAt = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='sites/', default='placeholders/no_www.png')

    class Meta:
        verbose_name = 'موقع'
        verbose_name_plural = 'مواقع'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('site:site_detail', kwargs={'site_id': self.pk})


class FavoriteSite(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='favorite_by')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")

    class Meta:
        verbose_name = 'المفضلة'
        verbose_name_plural = 'المفضلات'

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.site.name)


class Course(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()
    language = models.CharField(max_length=50)
    category = models.CharField(max_length=150)
    duration = models.FloatField()
    duration_format = models.CharField(max_length=50, choices=[('دقائق', 'دقائق'), ('ساعات', 'ساعات')], default='ساعات')
    author = models.CharField(max_length=150)
    addedAt = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='courses/', default='placeholders/no_learning.png')

    class Meta:
        verbose_name = 'دورة'
        verbose_name_plural = 'دورات'

    def __str__(self):
        return self.name


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default='')
    user_email = models.EmailField()
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.CharField(choices=[('جديد', 'جديد'), ('قيد الإنتظار', 'قيد الإنتظار'),
                                              ('تم حلها', 'تم حلها'), ('مغلق', 'مغلق')], max_length=50, default='جديد')
    category = models.CharField(choices=[('مشكلة تقنية', 'مشكلة تقنية'), ('إقتراح', 'إقتراح'), ('آخرى', 'آخرى')]
                                       , max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'تقرير'
        verbose_name_plural = 'تقارير'

    def __str__(self):
        return self.title


class ReportReply(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_email = models.EmailField()
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'رد'
        verbose_name_plural = 'ردود'

    def __str__(self):
        return 'reply: {}'.format(self.pk)
