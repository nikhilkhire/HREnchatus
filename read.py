#read or file storage

from google.cloud import storage

bucket_name = 'dbwizards_files'
blob_name = 'doc_1.txt'

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(blob_name)

with blob.open("r") as f:
    print(f.read())
