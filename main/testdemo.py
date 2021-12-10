#
# headers = {
#             "cookie": "Path=/; Path=/; Path=/",
#             "content-type": "application/json"
#         }
# headers['a'] = 1
# print(headers)
# print(type(headers))
headers = {
            "device-model": "1",
            "client-type": "1",
            "content-type": "application/x-www-form-urlencoded"
        }
headers['content-type'] = 'json'
print(headers)