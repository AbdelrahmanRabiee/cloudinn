import requests
import json

from celery.decorators import task

from empires.models import Cost, Unit

@task(name="hello_world")
def hello():
    return 'Hello World'

@task(name="store_units")
def store_units():
    """
    - retrieve data from api
    - store unit data in DB
    - if cost data has keys ['Wood', 'Food', 'Stone', 'Gold'] then create cost object and 
        link it to unit object
    """
    res = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/units')
    json_data = res.json()
    for obj in json_data['units']:
        result =  any(elem in ['Wood', 'Food', 'Stone', 'Gold']  for elem in obj['cost'].keys()) 
        if result:  
            cost = Cost.objects.create(**obj['cost'])
            obj['cost'] = cost
        obj['cost'] = None    
        Unit.objects.create(**obj)
