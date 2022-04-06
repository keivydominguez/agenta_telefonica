from django.db import models

# Numero telefonico


class PhoneNumber(models.Model):
    # Catalogo de etiquetas para los numeros
    class Etiqueta(models.TextChoices):
        MOVIL = "movil", "Movil"
        HOME = "home", "Casa"
        OTHER = "other", "Otro"

    phone = models.IntegerField(
        db_column='telefono',
        null=True, blank=True,
        verbose_name='Telefono'
    )
    etiqueta = models.CharField(
        max_length=6,
        choices=Etiqueta.choices,
        db_column='etiqueta',
        null=True,
        blank=True,
        verbose_name='Etiqueta'
    )

    class Meta:
        db_table = 'numero_telefonico'
        verbose_name = 'Numero Telefonico'

    def __str__(self):
        return str(self.phone)


# Agenda Telefonica
class Phonebook(models.Model):
    # Catalogo de persona relacionada
    class Relationship(models.TextChoices):
        ASSISTANT = "assistant", "Asistente"
        BROTHER_SISTER = "brother_sister", "Hermana/Hermano"
        MOTHER_FATHER = "mother_father", "Madre/Padre"
        AUNT_UNLCE = "aunt_uncle", "Tia/Tio"
        GRANT = "grant", "Abuela/Abuelo"
        WIFE_HUSBAND = "wife_husband", "Esposa/Esposo"

    name = models.CharField(
        max_length=50,
        db_column='nombre',
        verbose_name='Nombre'
    )
    last_name = models.CharField(
        max_length=80,
        db_column='apellido',
        null=True, blank=True,
        verbose_name='Apellidos'
    )
    nickname = models.CharField(
        max_length=20,
        db_column='apodo',
        null=True,
        blank=True,
        verbose_name='Apodo'
    )
    phone = models.ForeignKey(
        PhoneNumber,
        db_column='telefono',
        verbose_name='Telefono',
        on_delete=models.CASCADE
    )
    email = models.EmailField(
        max_length=200,
        db_column='email',
        unique=True,
        null=True, blank=True,
        verbose_name='Correo electrónico'
    )
    relationship = models.CharField(
        max_length=16,
        choices=Relationship.choices,
        db_column='relacion',
        null=True,
        blank=True,
        verbose_name='Persona relacionada'
    )

    class Meta:
        db_table = 'agenda'
        verbose_name = 'Agenda'

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'

    def __str__(self):
        return self.name
