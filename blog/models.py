from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

'''
所有以 或 开头的行都是从其他文件添加一些位的行。因此，与其在每个文件中复制和粘贴相同的内容，不如使用 .fromimportfrom ... import ...

class Post(models.Model):—— 这条线定义了我们的模型（它是一个 ）。object

class是一个特殊关键字，表示我们正在定义一个对象。
Post是我们模型的名称。我们可以给它起一个不同的名字（但我们必须避免特殊字符和空格）。类名始终以大写字母开头。
models.Model意味着 Post 是一个 Django 模型，所以 Django 知道它应该保存在数据库中。
现在我们定义我们讨论的属性：、、 、 和 。为此，我们需要定义每个字段的类型（是文本吗？一个数字？约会？与另一个对象（如 User）的关系？titletextcreated_datepublished_dateauthor

models.CharField– 这是定义字符数量有限的文本的方式。
models.TextField– 这适用于没有限制的长文本。听起来很适合博客文章内容，对吧？
models.DateTimeField– 这是一个日期和时间。
models.ForeignKey– 这是指向另一个模型的链接。
我们不会在这里解释每一段代码，因为这会花费太多时间。如果你想了解更多关于 Model fields 以及如何定义上述内容以外的内容（https://docs.djangoproject.com/en/5.1/ref/models/fields/#field-types），你应该看看 Django 的文档。
'''