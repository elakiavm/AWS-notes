import json 

print('Lambda Function')

def lambda_handler(event,context):
    int transactionId      = event['queryStringParameters']['transactionId']
    var transactiontype    = event['queryStringParameters']['type']
    int transactionAmount  = event['queryStringParameters']['amount']

    print('transactionId =' + transactionId )
    print('transactiontype  =' + transactiontype )
    print('transactionAmount =' + transactionAmount )

    transactionRespose = {}
    transactionRespose['transactionId'] = transactionId
    transactionRespose['type']          = transactiontype
    transactionRespose['amount']        = transactionAmount
    transactionRespose['message']       = "Hello form lambda "

    responseObject = {}
    responseObject["statusCode"] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] ='application/json'
    responseObject['body'] = json.dump(transactionRespose)

    return responseObject

    https://8y0dcmnhi1.execute-api.ap-southeast-1.amazonaws.com/test/transactions?transactionId=5&type=PURCHASE&amount=500