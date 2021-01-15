import rethinkdb as r

r.db_create("imgen")
db = r.db("imgen")
db.table_create("keys")
db.table_create("applications")
