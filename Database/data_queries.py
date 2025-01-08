import uuid
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def connect_to_astra(secure_connect_path, keyspace):
    """
    Connects to an Astra DB using the secure connect bundle.
    """
    auth_provider = PlainTextAuthProvider(secure_connect_bundle=secure_connect_path)
    cluster = Cluster(cloud={'secure_connect_bundle': secure_connect_path}, auth_provider=auth_provider)
    session = cluster.connect()
    session.set_keyspace(keyspace)
    return session

def create_table(session):
    """
    Creates a table in the database to store scraped data.
    """
    session.execute("""
        CREATE TABLE IF NOT EXISTS scraped_data (
            id UUID PRIMARY KEY,
            platform TEXT,
            username TEXT,
            timestamp TEXT,
            content TEXT
        )
    """)

def insert_data(session, platform, username, data):
    """
    Inserts scraped data into the database.
    
    :param session: Astra DB session.
    :param platform: Name of the platform (e.g., Instagram, Twitter).
    :param username: Username of the profile.
    :param data: List of dictionaries containing post data.
    """
    for item in data:
        session.execute("""
            INSERT INTO scraped_data (id, platform, username, timestamp, content)
            VALUES (%s, %s, %s, %s, %s)
        """, (uuid.uuid4(), platform, username, item.get('timestamp', 'N/A'), item.get('content', '')))

if __name__ == "__main__":
    
    secure_connect_path = "secure-connect-database_name.zip"
    keyspace = "your_keyspace"

   
    example_data = [
        {"timestamp": "2025-01-01T12:34:56", "content": "Happy New Year!"},
        {"timestamp": "2025-01-02T15:20:00", "content": "Another day, another post."}
    ]

    try:

        session = connect_to_astra(secure_connect_path, keyspace)
        print("Connected to Astra DB!")

        
        create_table(session)
        print("Table created successfully!")

        
        platform = "Twitter"
        username = "example_user"
        insert_data(session, platform, username, example_data)
        print("Data inserted successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.shutdown()
