# used for logging to prevent local network urls from being exposed
def sanitizeUrls(url: str):
    if "http" and ".local" in url:
        # sanitize and return
        slashIndex = url.index("://")
        localIndex = url.index(".local")
        unmasked = url[slashIndex + 3 : localIndex]
        return url.replace(unmasked, "##########")
    else:
        return url


# mask input string by replacing characters with "#"
def maskify(cc):
    masked = "#" * (len(cc))
    return masked
