import os
host=input("Enterhost to ping:")
response=os.system(f"ping-c2{host}")
if response==0:
   print("Host is rechable")
else:
    print("Host is not reachable")
