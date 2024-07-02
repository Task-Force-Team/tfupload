import requests
import sys

def get_gofile_server():
    url = "https://api.gofile.io/getServer"
    try:
        response = requests.get(url, timeout=10)  # 10 seconds timeout
        if response.status_code == 200:
            data = response.json()
            if data["status"] == "ok":
                return data["data"]["server"]
    except requests.Timeout:
        print("Request to Gofile API timed out", file=sys.stderr)
    except requests.RequestException as e:
        print(f"Request to Gofile API failed: {e}", file=sys.stderr)
    return None

if __name__ == "__main__":
    server = get_gofile_server()
    if server:
        print(server)
    else:
        print("Failed to get server from Gofile API", file=sys.stderr)
        sys.exit(1)
