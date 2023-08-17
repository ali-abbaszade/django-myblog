import factory
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from factory.faker import faker

from .models import Post

FAKE = faker.Faker()

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=10)
    slug = factory.Faker("slug")
    author = User.objects.get_or_create(username="admin@email.com")[0]
    status = "published"
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 1024, "height": 768}),
            "example.jpg",
        )
    )

    @factory.lazy_attribute
    def body(self):
        para = ""
        for _ in range(0, 5):
            para += "\n" + FAKE.paragraph(nb_sentences=30)

        return para

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.tags.add(tag)
        else:
            self.tags.add(
                "techblog",
                "technews",
                "technology",
                "tech",
                "techblogger",
                "gadgets",
                "techworld",
                "techlover",
                "technologynews",
                "techgeek",
                "techupdates",
            )
