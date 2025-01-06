import enum

class CampaignStatus(enum.Enum):
    INACTIVE = 'Inactive'
    ACTIVE = 'Active'
    PAUSED = 'Paused'
    CLOSED = 'Closed'

    @classmethod
    def name_value_choices(cls):
        return [(status.name,status.value) for status in cls]
