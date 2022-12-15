from enum import Enum

# mempool api docs: https://mempool.space/docs/api/rest#get-sizes-weights
# can be any of the following: 24h, 3d, 1w, 1m, 3m...
class TimeRange(Enum):
    ONE_DAY = "24h"
    THREE_DAYS = "3d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1m"
    THREE_MONTHS = "3m"
