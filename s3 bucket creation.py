import boto3
s3connection = boto3.resource("s3")
def bucketCreation():
    bucket = s3connection.Bucket("emfreak22s3bucket")
    response = bucket.create(
        ACL = 'public-read',
        CreateBucketConfiguration = {"LocationConstraint" : 'eu-central-1'}
    )

    print(response)

def listAllBuckets():
    allBuckets = s3connection.buckets.all()
    print(list(allBuckets))


if __name__ == '__main__':
    # bucketCreation()
    listAllBuckets()