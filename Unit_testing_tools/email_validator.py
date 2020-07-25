def email_validator(email):
    if email.count('@') != 0 and email.count('.') != 0:
        return True
    return False



email_validator('medi@nett.fi')

print()

email_validator('medi.fi')

print()

email_validator('medi@')

print()

print('medi')
