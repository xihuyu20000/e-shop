def ok(msg, data):
    return {
        "meta":{
            "msg":msg,
            "status":200
        },
        "data":data
    }
def fail(status_code, msg):
    return {
        "meta":{
            "msg":msg,
            "status":status_code
        },
        "data":{}
    }