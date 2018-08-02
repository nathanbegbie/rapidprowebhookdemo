import json
import random
import maya
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    name = random.choice(['Samantha', "Judy", "Bob", "Vaughn"])
    description = random.choice(['1 Dollhouse', '3 bikes', '4 toothbrushes', '9 chairs', '1 car battery'])

    ship_date = maya.now().subtract(days=random.randint(1,5)).slang_date()
    delivery_date = maya.now().add(days=random.randint(1,5)).slang_date()
    cancel_date = maya.now().subtract(days=random.randint(1,10)).slang_date()

    resp_shipped = {
        'name': name,
        'description': description,
        'status': "Shipped",
        'ship_date': ship_date,
        'delivery_date': delivery_date,
    }

    resp_pending = {
        'name': name,
        'description': description,
        'status': "Pending",
        'ship_date': ship_date,
        'delivery_date': delivery_date
    }

    resp_cancelled = {
        'name': name,
        'description': description,
        'status': "Cancelled",
        'cancel_date': cancel_date
    }
    return json.dumps(random.choice([resp_shipped, resp_pending, resp_cancelled]))

    '''
    if order_num == "A123":
        return json.dumps(resp_shipped)
    elif order_num == "B123":
        return json.dumps(resp_pending)
    elif order_num == "C123":
        return json.dumps(resp_cancelled)
    '''


