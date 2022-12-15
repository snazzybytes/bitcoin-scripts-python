import urllib.request
import json
from datetime import datetime, timedelta
from mempool.timerange import TimeRange
import utils.helper as helper
import utils.stringutils as strhelper

config = helper.read_config()["BitcoinHalving"]
BLOCK_HEIGHT_URL = config["blockTipHeightUrl"]
BLOCK_DATA_URL = config["blockDataUrl"]

# BTC halving occurs every "210,000" blocks. Next halving will occur at block-height 840,000.
# ₿-halving calculation: (Halving block - Current height) * Average block time (latest N blocks in the last 3-days)
def estimateHalvingDateTime(timeRange: TimeRange):

    tipHeight = getBlockTipHeight()
    blockData = getBlockTimestamps(timeRange)
    blockTimes = calculateBlockTimes(blockData)
    avgBlockTime = calculateAvgBlockTime(blockTimes)
    halvingDateTime = calculateHalvingDateTime(tipHeight, avgBlockTime)

    printHalvingStats(blockData, halvingDateTime)
    return halvingDateTime


def getBlockTipHeight():
    print(
        "Retrieving current block height(tip)\n",
        strhelper.sanitizeUrls(BLOCK_HEIGHT_URL),
    )
    tipHeightUrl = urllib.request.urlopen(BLOCK_HEIGHT_URL)
    encoding = tipHeightUrl.info().get_content_charset("utf-8")
    body = tipHeightUrl.read()
    tipHeight = body.decode(encoding)
    return tipHeight


def getBlockTimestamps(timeRange: TimeRange):
    print(
        "Retrieving block data to calculate averge-block-time\n",
        strhelper.sanitizeUrls(BLOCK_DATA_URL),
    )
    blockRangeUrl = urllib.request.urlopen(BLOCK_DATA_URL + timeRange.value)
    encoding = blockRangeUrl.info().get_content_charset("utf-8")
    body = blockRangeUrl.read()
    blockData = json.loads(body.decode(encoding))["sizes"]
    return blockData


def calculateBlockTimes(blockData):
    blockTimes = []
    for i in range(len(blockData) - 1):
        blockTimes.append(
            abs(blockData[i + 1]["timestamp"] - blockData[i]["timestamp"])
        )

    print(
        "\nFound %s blocks ✓, calculated %s block times ✓"
        % (len(blockData), len(blockTimes))
    )
    return blockTimes


def calculateAvgBlockTime(blockTimes):
    avgBlockTime = round(sum(blockTimes) / (len(blockTimes)))
    print(
        "\nAverage block time: %s secs / %s mins ✓"
        % (str(avgBlockTime), str(round(avgBlockTime / helper.SECONDS_PER_MINUTE)))
    )
    return avgBlockTime


def calculateHalvingDateTime(tipHeight, avgBlockTime):
    halvingEstimate = round((840000 - int(tipHeight)) * avgBlockTime)

    print(
        '\n⏱ ₿ Halving time remaining ⏱":\n%s secs / %s hours / %s days'
        % (
            str(halvingEstimate),
            str(round(halvingEstimate / helper.SECONDS_PER_HOUR)),
            str(round(halvingEstimate / helper.SECONDS_PER_DAY)),
        )
    )
    print("\nCurrent DateTime: ", datetime.now())
    halvingDateTime = datetime.now() + timedelta(
        days=round(halvingEstimate / helper.SECONDS_PER_DAY)
    )
    return halvingDateTime


def printHalvingStats(blockData, halvingDateTime):
    print("\n🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀")
    print(
        "\nExpected ₿ Halving DateTime (based on last %s blocks): \n\t✅ %s ✅"
        % (
            len(blockData),
            halvingDateTime,
        )
    )
    print("\n🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀")


# run the script
estimateHalvingDateTime(TimeRange.THREE_DAYS)
