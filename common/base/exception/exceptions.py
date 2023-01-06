class DefaultException(Exception):
    def __init__(self, message=None, code=None, status=500):
        if message is None:
            self.message = '서버에 오류가 있습니다'
        else:
            self.message = message
        if code is None:
            self.code = 'CE00'
        else:
            self.code = code
        self.status = status

    def __str__(self):
        return self.message


class ParameterException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='필수 파라미터가 누락되었습니다', code='CE01')
        else:
            super().__init__(message=message, code='CE02')


class SameObjectExistException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='동일 객체가 이미 존재합니다', code='CE02')
        else:
            super().__init__(message=message, code='CE02')


class DoesNotHavePermissionException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='해당 동작 권한이 없습니다', code='CE03')
        else:
            super().__init__(message=message, code='CE03')


class DoesNotExistException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='해당 객체가 없습니다', code='CE04', status=404)
        else:
            super().__init__(message=message, code='CE04', status=404)


class CannotCreateDueToIntegrityErrorException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='무결성 에러가 발생 했습니다. 이미 존재 하거나 기타의 이유로 생성 할 수 없습니다.', code='CE05', status=404)
        else:
            super().__init__(message=message, code='CE05', status=404)
