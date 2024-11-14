from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home,name='home'), # Главная страница
    path('gallery/', views.property_gallery,name='property_gallery'), # Галлерея недвижимости
    path('contacts/', views.contacts,name='contacts'), # Контакты
    path('add-review/', views.add_review,name='add_review'), # Добавить отзыв
    path('faq/', views.faq_view,name='faq'), # Частые вопросы
    path('property/<int:pk>/', views.property_detail, name='property_detail'), #Детальный обзор недвижимости
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)