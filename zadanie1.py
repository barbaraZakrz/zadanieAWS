import boto3

#s3 = boto3.client("s3")
#s3.create_bucket(Bucket="my-hosted-content-zadania")

s3 = boto3.client("s3")

s3.upload_file(
    Filename="daneEconomist.csv",
    Bucket="my-hosted-content-zadania",
    Key="daneEconomist.csv",
)



