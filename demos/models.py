from django.db import models


class Demo (models.Model):
    # The slug will be used to match the demo template
    slug = models.SlugField()

    # Brief name and description of the project
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

    # The repository where the related code lives
    repo = models.URLField(blank=True)

    # The URL to the article within the webpage
    article = models.URLField(blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('demos.views.demo', (self.slug,))

    def to_dict(self):
        return {
            'slug': self.slug,
            'name': self.name,
            'repo': self.repo,
            'article': self.article,
            'self': self.get_absolute_url(),
            'description': self.description,
        }
