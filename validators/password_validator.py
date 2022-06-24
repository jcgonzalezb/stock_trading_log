import re


class PasswordNotValidError(ValueError):
    """Parent class of all exceptions raised by this module."""
    pass


class PasswordLengthError(PasswordNotValidError):
    """Exception raised when a password fails length validation."""
    pass


class PasswordUpperCaseError(PasswordNotValidError):
    """Exception raised when a password fails validation because does not contain an uppercase letter"""
    pass


class PasswordLowerCaseError(PasswordNotValidError):
    """Exception raised when a password fails validation because does not contain a lowercase letter"""
    pass


class PasswordCharacterCaseError(PasswordNotValidError):
    """Exception raised when a password fails validation because does not contain one special character."""
    pass


class Password:

    @staticmethod
    def validate_password(arg):
        validate = False

        if len(arg) < 10:
            raise PasswordLengthError(
                "the password must have at least 10 characters.")
        else:
            validate = Password.validate_requirements(arg)

        return validate

    @staticmethod
    def validate_requirements(arg):
        validate = True

        upper = (re.search(r"[A-Z]", arg))
        if not upper:
            raise PasswordUpperCaseError(
                "the password must have at least one uppercase letter.")

        lower = (re.search(r"[a-z]", arg))
        if not lower:
            raise PasswordLowerCaseError(
                "the password must have at least one lowercase letter.")

        character = (re.search(r"[!@#?\]]", arg))
        if not character:
            raise PasswordCharacterCaseError("the password must have at least one of the following characters !, @, #, "
                                             "? or ].")

        return validate
