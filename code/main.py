import os

#TEST_AUTHENTICATION = int(os.environ.get('TEST_AUTHENTICATION'))
#TEST_AUTHORIZATION = int(os.environ.get('TEST_AUTHORIZATION'))
#TEST_CONTENT = int(os.environ.get('TEST_CONTENT'))

"""if (TEST_AUTHENTICATION ==1):
    import test_authentication


if (TEST_AUTHORIZATION ==1):
    import test_authorization

if (TEST_CONTENT ==1):
    import test_content"""


int(os.environ.get('TEST_AUTHENTICATION'))

import get_access_token()
#import get_customer_flight_information_on_departures()