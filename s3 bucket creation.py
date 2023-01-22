import os
import boto3
from configparser import ConfigParser
configur = ConfigParser()
print(configur.read('config/main_config.ini'))
print(os.getcwd())

class s3Ops:
    def __init__(self):
        self.session = self.createSession()
        self.s3connection = self.session.resource("s3")
    def createSession(self):
        id = configur.get('AWS','id')
        secret =configur.get('AWS','secret')
        session = boto3.Session(id,secret)
        return session

    def bucketCreation(self, bucketName):
        bucket = self.s3connection.Bucket(bucketName)
        response = bucket.create(
            ACL = 'public-read',
            CreateBucketConfiguration = {"LocationConstraint" : 'eu-central-1'}
        )
        print(response)

    def listAllBuckets(self):
        allBuckets = self.s3connection.buckets.all()
        print(list(allBuckets))

    def insertIntoBucket(self, bucketName,file, text):
        fileObj = self.s3connection.Object(bucketName,text)
        fileObj.put(Body=open(file, 'rb'))

if __name__ == '__main__':
    # bucketCreation()
    # listAllBuckets()
    obj = s3Ops()
    # obj.bucketCreation('bucketsss091')
    # file  = 'C:\\Users\\Udit\\Downloads\\TereNaam2003SalmanKhan_archive.torrent'
    # text = 'tere_naam.torrent'
    # obj.insertIntoBucket('bucketsss091',file,text)
    