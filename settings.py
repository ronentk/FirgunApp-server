

# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27010

# Skip these if your db has no auth. But it really should.
#MONGO_USERNAME = '<your username>'
#MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'apitest'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE','PATCH']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


schema1 = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.

    # 'category' is a list, and can only contain values from 'allowed'.
    'category': {
        'type': 'string',
        'required': True,
        'allowed': ["eco", "people", "sight"],
    },
    'longitude':{
        'type':'string',
        'required': True,
    },
    'latitude':{
        'type':'string',
        'required': True,
    },
    'description': {
        'type': 'string',
        'minlength': 0,
        'maxlength': 15,
        'required': False,
        'unique': False,
    },
    'date': {
    },
    'username':{
        'type': 'string',
        'minlength': 8,
        'maxlength':16,
        'required': True,
        'unique': True,
    },
}


schema2 = {
    'username':{
        'type': 'string',
        'minlength': 8,
        'maxlength':16,
        'required': True,
        'unique': True,
    },
    'userpic':{
        'type': 'media'
    },
    'longitude':{
        'type':'string',
        'required': True,
    },
    'latitude':{
        'type':'string',
        'required': True,
    },
}

firguns = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'firgun',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema1
}

users = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'users',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema2
}

    
DOMAIN = {
    'firguns': firguns,
    'users': users
}