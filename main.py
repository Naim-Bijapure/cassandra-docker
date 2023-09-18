from cassandra.cluster import Cluster

cluster = Cluster(['0.0.0.0'])
session = cluster.connect('killrvideo')


rows = session.execute('SELECT *  FROM videos')
for user_row in rows:
    print(user_row)
