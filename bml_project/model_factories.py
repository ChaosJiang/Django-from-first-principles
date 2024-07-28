from random import randint

import factory
from blogs.models import Blog, BlogPost
from faker import Faker

fake = Faker()


def get_title() -> str:
    return " ".join(fake.words()).title()


def get_description() -> str:
    return fake.sentence(nb_words=10)


def get_body() -> str:
    paragraphs = [fake.paragraph(randint(5, 10)) for _ in range(randint(3, 25))]
    return "\n\n".join(paragraphs)


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.LazyFunction(get_title)
    description = factory.LazyFunction(get_description)


class BlogPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = factory.LazyFunction(get_title)
    body = factory.LazyFunction(get_body)
    blog = factory.Iterator(Blog.objects.all())
