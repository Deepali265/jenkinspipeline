from Reqres import SendRequest


def test_Reqres_respone_code():
    var_test = SendRequest()
    var_test.sendrequest()
    #checks for the correct response code
    assert var_test.sample.status_code == 200


def test_Reqres_respone_content_type():
    var_test = SendRequest()
    var_test.sendrequest()
    #checks for the content type received, whic is Json in this context
    assert var_test.sample.headers["Content-Type"] == "application/json; charset=utf-8"


def test_Reqres():
    var_test = SendRequest()
    var_test.sendrequest()
    var_response = var_test.sample.json()
    #checks if the data of all the 6 users is received
    assert len(var_response["data"]) == 6







