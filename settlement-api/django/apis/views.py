from django.shortcuts import render

import requests, json, base64, time

# Create your views here.
def index(request):
  return render(
    request,
    'apis/index.html',
  )

def settlements(request):
  startDate = "2022-07-01"
  endDate = "2022-07-29"
  page = ""
  size = 100  
  search = "?startDate=%s&endDate=%s&page=%s&size=%s" % (startDate, endDate, page, size)

  url = "https://api.tosspayments.com/v1/settlements"
  secertkey = "test_sk_D4yKeq5bgrpKRd0JYbLVGX0lzW6Y"
  userpass = secertkey + ':'
  encoded_u = base64.b64encode(userpass.encode()).decode()
  
  headers = {
    "Authorization" : "Basic %s" % encoded_u,
    "Content-Type": "application/json"
  }
  
  res = requests.get(url+search, headers=headers)
  resjson = res.json()
  pretty = json.dumps(resjson, indent=4, ensure_ascii=False)

  return render(
    request,
    'apis/settlements.html',
    {
      "res" : pretty,
    }
  )