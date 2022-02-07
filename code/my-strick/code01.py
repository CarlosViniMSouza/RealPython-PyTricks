# Customizing responses to a request

# pip install requests (it's a libray python that could be installed)
import requests

# use the GitHub API how to example:
resp = requests.get("https://api.github.com")

switch = {
    100: "continue the requesition",
    101: "swithing protcols necessary",
    200: "ok, proceed"
}

resp_switch = switch.get(resp.status_code)

print("Result: ", resp_switch)
