from DEBUG import DEBUG
from POST_URL import URL as POST_URL
from TEST_URL import URL as TEST_URL



DEBUG_MODE = DEBUG
DEBUG_DELIVERY_SEND_TO_TEST = True

def get_posting_url():
    if DEBUG_MODE and DEBUG_DELIVERY_SEND_TO_TEST:
        posting_url = TEST_URL
    else:
        posting_url = POST_URL
    return posting_url