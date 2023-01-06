from common.base.exception.exceptions import DefaultException


class CodeNotAvailableException(DefaultException):
    def __init__(self):
        super().__init__(message='유효한 코드가 아닙니다', code='AE01')


class PasswordValidationException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='비밀번호가 형식에 맞지 않습니다', code='AE02')
        else:
            super().__init__(message=message, code='AE02')


class IsNotCertifiedUserException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='미인증 유저 입니다', code='AE03')
        else:
            super().__init__(message=message, code='AE03')


class UserDoesNotExistException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='존재하지 않는 유저 입니다', code='AE04')
        else:
            super().__init__(message=message, code='AE04')


class PasswordNotMatchingException(DefaultException):
    def __init__(self):
        super().__init__(message='비밀번호가 다릅니다', code='AE05')


class CanNotCertifyException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='인증 과정에 오류가 발생했습니다', code='AE06')
        else:
            super().__init__(message=message, code='AE06')

class NiceDecryptException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='인코딩 데이터에 문제가 있습니다', code='AE07')
        else:
            super().__init__(message=message, code='AE07')