from common.base.exception.exceptions import DefaultException


class SalesItemDoesNotExistException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='존재하지 않는 상품 입니다', code='SE01')
        else:
            super().__init__(message=message, code='SE01')


class CanNotChangeExceptions(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='판매 준비 단계의 상품만 수정이 가능합니다', code='SE02')
        else:
            super().__init__(message=message, code='SE02')


class CanNotPurchaseException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='구매가 불가능한 상품입니다', code='SE03')
        else:
            super().__init__(message=message, code='SE03')


class NotValidException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='유효하지 않은 결제 입니다.', code='SE04')
        else:
            super().__init__(message=message, code='SE04')


class ImportApiException(DefaultException):
    def __init__(self, message=None):
        if message is None:
            super().__init__(message='아임포트 API 호출에 실패 하였습니다.', code='SE05')
        else:
            super().__init__(message=message, code='SE05')
