from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def connect_to_astra(secure_connect_path):
    """
    Connects to an Astra DB using the secure connect bundle.

    :param secure_connect_path: Path to the secure connect bundle ZIP file.
    :return: Session object connected to the database.
    """
    
    auth_provider = PlainTextAuthProvider(
        username=None,
        password=None,
        secure_connect_bundle=secure_connect_path,
    )
    cluster = Cluster(cloud={'secure_connect_bundle': secure_connect_path}, auth_provider=auth_provider)
    session = cluster.connect()

    
    session.set_keyspace('your_keyspace')
    
    return session

if __name__ == "__main__":
    
    secure_connect_path = "secure-connect-database_name.zip"

    try:
        session = connect_to_astra(secure_connect_path)
        print("Connected to Astra DB!")
        
        rows = session.execute("SELECT release_version FROM system.local")
        for row in rows:
            print(f"Cassandra Release Version: {row.release_version}")
    except Exception as e:
        print(f"An error occurred: {e}")
