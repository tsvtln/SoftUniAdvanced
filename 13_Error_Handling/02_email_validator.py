class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


class EmailValidator:
    @staticmethod
    def check_length(email):
        if len(email.split("@")[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 letters.")

    @staticmethod
    def check_at_symbol(email):
        if '@' not in email:
            raise MustContainAtSymbolError("Email must contain @")

    @staticmethod
    def check_domains(email):
        valid_domains = ['com', 'bg', 'org', 'net']
        get_domain = email.split('.')
        if get_domain[-1] not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


email = ''

while email != 'End':
    email = input()
    if email == 'End':
        continue
    try:
        EmailValidator.check_length(email)
        EmailValidator.check_at_symbol(email)
        EmailValidator.check_domains(email)
    except EmailValidationError as e:
        print({e})
