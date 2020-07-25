from email_validator import email_validator

def test_email_validator():
    assert email_validator('juju@gmail.com')
    assert email_validator('juju@gmail@.com')
