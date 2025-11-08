
uri=input("Enter website URL:")
try:
  response=requests.get(url)
  if reaponse.status_code==200:      
     print("website is UP")
  else:
     print ("website returned error:",response.status_code)
except:
    print("website is DOWN or unreachable")
    
       
