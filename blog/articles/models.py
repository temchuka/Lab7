from django.db import models
from django.contrib.auth.models import User


class Lease(models.Model):
    contract = models.CharField("Номер договора", max_length=200)
    outlet = models.CharField("Торговая точка", max_length=200)
    floor = models.IntegerField("Этаж")
    area = models.DecimalField("Площадь, кв. м", max_digits=10, decimal_places=2)
    conditioner = models.BooleanField("Кондиционер", default=False)
    day_price = models.DecimalField("Стоимость аренды в день, руб.", max_digits=10, decimal_places=2)
    tenant = models.CharField("Арендатор", max_length=200)
    contact = models.CharField("Контактное лицо", max_length=200)
    contract_date = models.DateField("Дата заключения договора")
    start_date = models.DateField("Начало аренды")
    end_date = models.DateField("Окончание аренды")
    text = models.TextField("Сведения об арендаторе")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор записи")
    created_date = models.DateField("Дата создания записи", auto_now_add=True)

    class Meta:
        verbose_name = "договор аренды"
        verbose_name_plural = "Договоры аренды"

    def __str__(self):
        return "%s: %s" % (self.contract, self.outlet)

    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text

    def get_days(self):
        # срок аренды в днях (включая первый и последний день)
        return (self.end_date - self.start_date).days + 1

    def get_cost(self):
        # стоимость аренды за весь срок = количество дней * стоимость аренды в день
        return self.get_days() * self.day_price
