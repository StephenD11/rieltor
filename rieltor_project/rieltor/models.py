from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    city = models.CharField(max_length=20, verbose_name='Город', blank=True)
    email = models.EmailField(blank=True, verbose_name='Почта')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    #Связываем клиента с недвижкой
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='clients', null=True, blank=True, verbose_name='Недвижимость')

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ваше имя')
    email = models.EmailField(blank=True, verbose_name='Ваша почта')
    rating = models.IntegerField(verbose_name='Ваша оценка', validators=[MinValueValidator(1), MaxValueValidator(5)],
                                 default=0)
    comment = models.TextField(max_length=250, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.created_at}'

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"


class Property(models.Model):

    ROOMS = [
        ('Изолированные', 'Изолированные'),
        ('Смежные', 'Смежные'),
    ]

    BATHROOM = [
        ('Совмещенный', 'Совмещенный'),
        ('раздельный', 'раздельный'),
    ]

    REPAIR = [
        ('Косметический', 'Косметический'),
        ('Евро', 'Евро'),
        ('Новострой', 'Новострой'),
    ]

    adress = models.CharField(max_length=200, verbose_name='Адресс',default='')
    square = models.CharField(max_length=25, verbose_name='Площадь',blank=True)
    floor = models.CharField(max_length=3, verbose_name='Этаж')
    price = models.IntegerField(verbose_name='Цена', blank=True, null=True)
    rooms = models.CharField(max_length=2, verbose_name='Колличесто комнат',blank=True)
    living_area = models.CharField(max_length=10, verbose_name='Жилая площадь',blank=True)
    bathroom = models.CharField(max_length=50,choices=BATHROOM, verbose_name='Санузел',default='',blank=True)
    kitchen_area = models.CharField(max_length=10, verbose_name='Площадь Кухни',blank=True)
    city = models.CharField(max_length=25, verbose_name='Город', default='',blank=True)
    type_of_rooms = models.CharField(max_length=25, choices=ROOMS, verbose_name='Тип комнат', default='',blank=True)
    repair = models.CharField(max_length=25, choices=REPAIR, verbose_name='Ремонт', default='',blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    map_link = models.TextField(blank=True, verbose_name='Ссылка на карту')
    image = models.ImageField(upload_to='property_images/', blank=True, null=True, verbose_name='Фото')
    updated_at = models.DateTimeField(auto_now=True)  # Поле для времени последнего обновления

    def get_absolute_url(self):
        return reverse('property_detail', args=[str(self.pk)])

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img = img.convert('RGB')
            img.thumbnail((512, 512))
            img.save(self.image.path, quality=90)
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.adress} {self.price}'

    class Meta:
        verbose_name = "Недвижимость"
        verbose_name_plural = "Недвижимость"

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название компании")
    address = models.CharField(max_length=300, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    whatsup = models.URLField(blank=True, null=True, verbose_name="Ссылка на WhatsUp")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Информация о компании"
        verbose_name_plural = "Информация о компании"


class FAQ(models.Model):
    question = models.CharField(max_length=500, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Часто задаваемый вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"