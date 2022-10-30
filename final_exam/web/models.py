from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2
    USERNAME_MIN_LEN_VALIDATION_MESSAGE = 'The username must be a minimum of 2 chars'

    AGE_MIN_VALUE = 18

    PASSWORD_MAX_LEN = 30

    FIRST_NAME_MAX_LEN = 30

    LAST_NAME_MAX_LEN = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[
            MinLengthValidator(USERNAME_MIN_LEN, USERNAME_MIN_LEN_VALIDATION_MESSAGE),
        ]
    )

    email = models.EmailField(
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(AGE_MIN_VALUE),
        ]
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=FIRST_NAME_MAX_LEN,
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=LAST_NAME_MAX_LEN,
    )

    picture = models.URLField(
        blank=True,
        null=True,
    )


class Car(models.Model):
    TYPE_CHOICES = [
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other')
    ]

    TYPE_MAX_LEN = max([len(car_type[1]) for car_type in TYPE_CHOICES])

    MODEL_MAX_LEN = 30
    MODEL_MIN_LEN = 2

    YEAR_MIN_VALUE = 1980
    YEAR_MAX_VALUE = 2049
    YEAR_VALIDATION_MESSAGE = 'Year must be between 1980 and 2049'

    PRICE_MIN_VALUE = 1

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        choices=TYPE_CHOICES,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LEN,
        validators=[
            MinLengthValidator(MODEL_MIN_LEN)
        ]
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(YEAR_MIN_VALUE, YEAR_VALIDATION_MESSAGE),
            MaxValueValidator(YEAR_MAX_VALUE, YEAR_VALIDATION_MESSAGE),
        ]
    )

    image_url = models.URLField(
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(PRICE_MIN_VALUE),
        ]
    )

















