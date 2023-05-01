#!/usr/bin/python3
"""
This Python script sends a GET request to https://alx-intranet.hbtn.io/status using the urllib.request module and
displays the response content and its type and the decoded utf-8 content.
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content)
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
