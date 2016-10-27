# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
import datetime
db.define_table('tel',
                Field('name', 'text'),
                Field('ra', 'text'),
                Field('decl', 'text'),
                Field('rad', 'text'),
                Field('cat', requires=IS_IN_SET(['GSC', 'NOMAD', 'UCAC'])),
                )

