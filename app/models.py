from django.db import models

class Profile(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    school = models.TextField('学校')
    introduction = models.TextField('自己紹介')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name

class Work(models.Model):
    work_title = models.CharField('作品タイトル', max_length=100, null=True, blank=True)
    youtube_html = models.TextField('youtube動画')
    use_language = models.TextField('使用言語')
    discription = models.TextField('説明')
    details = models.TextField('URL', null=True, blank=True)
    github = models.CharField('github', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.work_title