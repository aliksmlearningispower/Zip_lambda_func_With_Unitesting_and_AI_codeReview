from create_student.lambda_function import lambda_handler


def test_create_student():

    response = lambda_handler({}, {})

    assert response["statusCode"] == 201
    assert response["body"] == "Student Created"