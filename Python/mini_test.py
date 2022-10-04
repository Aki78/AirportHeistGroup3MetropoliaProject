def return_sth():
    return None

sth = return_sth()

if sth is None:
    print("Got nothing")
elif sth is not None:
    print("Got sth")