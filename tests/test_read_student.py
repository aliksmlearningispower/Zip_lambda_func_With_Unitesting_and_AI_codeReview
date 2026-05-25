from read_student.lambda_function import lambda_handler


def test_read_student():

    response = lambda_handler({}, {})

    assert response["statusCode"] == 200
    assert response["body"] == "Student Details"