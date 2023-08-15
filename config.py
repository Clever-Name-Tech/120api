posting_url = ""
testing_url = "https://hook.us1.make.com/f98l2se8e4kx7ag5c09aaxsjyxuel6j1"

DEBUG_MODE = True
DEBUG_DELIVERY_DO_NOT_SEND = False
DEBUG_DELIVERY_SEND_TO_TEST = True

if DEBUG_MODE and DEBUG_DELIVERY_SEND_TO_TEST:
    posting_url = testing_url