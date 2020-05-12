import boto3
import json

def lambda_handler(event, context):

    #print(event)
    
    # check that the request has some input body
    if 'body' in event:
        event = json.loads(event["body"])

    # get float "amount"
    text = event["text"]
    print(text)
    client=boto3.client('translate',region_name="us-east-1")
    result= client.translate_text(Text=text,SourceLanguageCode="auto",TargetLanguageCode="ja")
    
    print(result["TranslatedText"])
    
    res = []

    res.append({"Text":text,"TransalateTo":result["TranslatedText"]})
    # format the response as JSON and return the result
    response = {
        "statusCode": "200",
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"res": res})
    }

    return response
