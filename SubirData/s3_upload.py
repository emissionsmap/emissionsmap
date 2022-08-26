from http import client
import boto3
from authe import ACCESS_KEY, SECRET_KEY
import os
import io
import glob

def push():
    client = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                    aws_secret_access_key=SECRET_KEY)

    response = client.list_buckets()
    if "archivoslimpios" not in response:
        client.create_bucket(Bucket="archivoslimpios")

    ficheros = glob.glob('./Normalizados/*')
    n = 0  
    s3 = boto3.resource("s3")
    for i in ficheros:
        direc = os.path.basename(i)
        s3.meta.client.upload_file(i, "archivoslimpios", direc)
        n += 1
        print("{} Archivos subidos".format(n))


def pushS3():
    client = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                    aws_secret_access_key=SECRET_KEY)

    client.create_bucket(Bucket="archivossucios")

    ficheros = glob.glob('./dags/archivosPrueba/*')
    n=0
    s3 = boto3.resource("s3")
    for i in ficheros:
        Key = os.path.basename(i)
        s3.meta.client.upload_file(i, "archivossucios", Key)
        n += 1
        print("{} Archivos subidos".format(n))
    print("Todos los archivos fueron subidos")

if __name__ == "__main__":
    pushS3()
    push()