from email_checker import email_checker

def test_email_checker():
    assert email_checker('juju@gmail.com')
    assert email_checker('juju@gmail@.com')
