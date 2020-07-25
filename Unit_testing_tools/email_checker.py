def email_checker(email):
    if email.count('@') ==1 and email.count('.') == 1:
        return True
    return False
