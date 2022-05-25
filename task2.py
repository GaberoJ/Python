import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for i in range(15):
        raw = f.readline()

        REMOTE_ADDR_RE = re.compile(r'\d*\.\d*\.\d*\.\d*')
        REQUEST_DATETIME_RE = re.compile(r'\w*/\w*/\w*:\d*:\d*:\d* \+\d{4}')
        REQUEST_TYPE_RE = re.compile(r'GET')
        REQUESTED_RESOURCE_RE = re.compile(r'/\w*/\w*_\d*.\w*/\d*.\d*')
        RESPONSE_CODE_RE = re.compile(r'\s\d{3}\s')
        RESPONSE_SIZE_RE = re.compile(r'\d*\s"-"')

        remote_addr = re.search(REMOTE_ADDR_RE, raw)
        request_datetime = re.search(REQUEST_DATETIME_RE, raw)
        request_type = re.search(REQUEST_TYPE_RE, raw)
        requested_resource = re.search(REQUESTED_RESOURCE_RE, raw)
        response_code = re.search(RESPONSE_CODE_RE, raw)
        response_size = re.search(RESPONSE_SIZE_RE, raw)

        parsed_raw = (remote_addr[0], request_datetime[0], request_type[0], requested_resource[0], response_code[0],
                      response_size[0].split(' ')[0])
        print(f'\n{raw}{parsed_raw}')


