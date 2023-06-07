from google.cloud import storage

client = storage.Client()
# create a new storage bucket
new_bucket = client.create_bucket("warehouse-paul-mazu-1")

# create blob(file)
new_blob = new_bucket.blob("test-folder/manage.py")

new_blob.upload_from_filename(filename="manage.py")