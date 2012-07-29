from django.db.models import Manager

class RestaurantManager(Manager):
    
    def all(self):
        """Returns all Restaurants on-file."""
        return self.get_query_set()
        
    def active(self):
            """Returns all active Restaurants."""
            return self.get_query_set().filter(active=True)