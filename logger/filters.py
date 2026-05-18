import logging
import re


class SecurityMaskingFilter(logging.Filter):
    JWT_PATTERN = re.compile(r'eyJhbGciOi[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+')
    PASSWORD_PATTERN = re.compile(r'("password"\s*:\s*")[^"]+(")')

    def filter(self, record: logging.LogRecord) -> bool:
        if isinstance(record.msg, str):
            record.msg = self.JWT_PATTERN.sub("[MASKED_JWT]", record.msg)
            record.msg = self.PASSWORD_PATTERN.sub(r'\1***\2', record.msg)
        return True
