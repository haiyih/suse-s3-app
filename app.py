from flask import Flask
import boto3

app = Flask(__name__)
s3 = boto3.client('s3')

@app.route("/")
def home():
    response = s3.list_buckets()
    bucket_names = [bucket['Name'] for bucket in response['Buckets']]
    return f"S3 Buckets: {bucket_names}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
