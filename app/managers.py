from datetime import datetime

from django.db import models


class PostManager[T](models.Manager):

    def get_most_recent(self) -> models.QuerySet[T]:
        return self.filter(
            models.Q(post_date__lte=datetime.today())
            | models.Q(post_modified_date__lte=datetime.today())
            | models.Q(post_status="recent")
        )
