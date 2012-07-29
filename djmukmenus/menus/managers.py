from django.db.models import Manager

class MenuManager(Manager):
    
    def all(self):
        """Returns all Menus on-file."""
        return self.get_query_set()
        