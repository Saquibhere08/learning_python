#Simple LinkedList

head={
    "value":11,
    "next":{
        "value":7,
        "next":{
                "value":4,
                "next":None
            }
        }
}
print(head['next']['next']['value'])