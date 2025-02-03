import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact

    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []
    HONORIFIC_PREFIXES = ['Sra.', 'Sr.', 'Dr.', 'Dra.', 'Prof.', 'Mestre',
                          'Srta.']

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        nomex = profile['name']

        # Verifique se o nome é uma string
        if isinstance(nomex, str):
            # Inicialize first_name e last_name
            first_name, last_name = '', ''

            # Verifique se o nome começa com um prefixo
            for prefix in HONORIFIC_PREFIXES:
                if nomex.startswith(prefix + ' '):  # Se o nome começa com o prefixo
                    # Inclua o prefixo no primeiro nome
                    first_name = prefix + ' ' + nomex[len(prefix) + 1:].split(' ', 1)[0]
                    last_name = nomex[len(prefix) + len(first_name.split(' ', 1)[0]) + 1:].strip()  # Pega o resto como sobrenome
                    break
            else:
                # Caso não tenha prefixo, divide normalmente
                first_name, last_name = nomex.split(' ', 1) if ' ' in nomex else (nomex, '')
        else:
            # Caso o nome não seja uma string, trate de forma padrão
            first_name = str(nomex)
            last_name = ''

        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)
