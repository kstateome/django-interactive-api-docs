from django.db.models.query import QuerySet
from django.db.models import Manager

class APIMethodQuerySet(QuerySet):
    def published(self):
        return self.filter(published=True)

class APIMethodManager(Manager):
    def get_query_set(self):
        return APIMethodQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_query_set().published()
