"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/about")
    assert b"JC's Travel Blog" in response.data
