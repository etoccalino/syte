from django.db import models


class Demo (models.Model):
    name = models.CharField(max_length=255)
    repo = models.URLField(blank=True)

    # NOTE: The slug will be used to match the demo template
    slug = models.SlugField()

    @models.permalink
    def get_absolute_url(self):
        return ('demos.views.demo', (self.slug,))

    def to_dict(self):
        return {
            'name': self.name,
            'slug': self.slug,
            'repo': self.repo,
            'article': self.get_absolute_url()
        }
