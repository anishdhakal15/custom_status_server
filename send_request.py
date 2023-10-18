import urllib.request
import urllib.parse
import base64
import json

# function to send post request
def post_request(url, data, username, password):
    data = json.dumps(data).encode('utf-8') 
    request = urllib.request.Request(url, data=data, method='POST')
    credentials = f"{username}:{password}"
    base64_credentials = base64.b64encode(credentials.encode()).decode()
    request.add_header("Authorization", f"Basic {base64_credentials}")
    response = urllib.request.urlopen(request)
    response_content = response.read().decode("utf-8")
    return response_content

if __name__ == "__main__":
    url = "http://127.0.0.1:8080/secure/sendbatch"
    username = "foo"
    password = "bar"

    # parameters for batchsend
    baseParams2 = {
        "batch_config": {
            "callback_url": "http://127.0.0.1:5000/api/success",
            "errback_url": "http://127.0.0.1:5000/api/error",
        },
        "messages": [
            {
                "to": [
                    "55555551",
                    "55555552",
                    "55555553"
                ],
                "content": "Hello world !"
            },
            {
                "to": "7777771",
                "content": "Holà !"
            },
            {
                "to": "invalid-number",
                "content": "Invalid message"
            }
        ]
    }

    response_content = post_request(url, baseParams2, username, password)
    print(response_content)
