from django.db import models

class Award(models.Model):  # 荣誉模型
    description = models.TextField(max_length=500,
                               blank=True,
                               null=True,
                               verbose_name='荣誉描述')
    photo = models.ImageField(upload_to='Award/',
                            blank=True,
                            verbose_name='荣誉照片')

    class Meta:
        verbose_name = '获奖和荣誉'
        verbose_name_plural = '获奖和荣誉' 