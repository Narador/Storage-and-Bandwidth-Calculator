'''
Models for the calculator app
These models determine what fields are
used in showing server and camera fields
'''

from django.db import models

class Server(models.Model):
    ''' Server class to show server info on homepage and 
    the ability to add cameras to an instance of a Server
    '''

    server_name = models.CharField(max_length=50)

    total_space = models.PositiveIntegerField()

    ''' TODO

    # of cameras = #

    min # of days -- this could be the minimum # of days any camera has
    '''

    def __str__(self):
        return self.server_name
