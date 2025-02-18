from enum import Enum

class DonationStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

    @classmethod
    def name_value_choices(cls):
        return [(status.name, status.value) for status in cls]

class TransactionStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

    @classmethod
    def name_value_choices(cls):
        return [(status.name, status.value) for status in cls]
