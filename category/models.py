from django.db import models


class TrackableDateModel(models.Model):
    """Abstract model to Track the creation/updated date for a model."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category1(TrackableDateModel):
    label = models.TextField(max_length=2000, null=True)


class Category2(TrackableDateModel):
    main_category = models.ForeignKey(Category1, related_name='children',
                                      null=True, blank=True, on_delete=models.CASCADE)
    label = models.TextField(max_length=2000, null=True)

    def __unicode__(self):
        return self.label
