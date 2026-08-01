import urllib.request
import urllib.error

routes = [
    ("Home", "https://wordpress-1644135-6589363.cloudwaysapps.com/"),
    ("About", "https://wordpress-1644135-6589363.cloudwaysapps.com/index.php?pagename=about"),
    ("Services", "https://wordpress-1644135-6589363.cloudwaysapps.com/index.php?pagename=services"),
    ("Portfolio", "https://wordpress-1644135-6589363.cloudwaysapps.com/index.php?pagename=portfolio"),
    ("Contact", "https://wordpress-1644135-6589363.cloudwaysapps.com/index.php?pagename=contact")
]

def verify():
    print("Verifying deployed WordPress page routes...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    for name, url in routes:
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=5) as res:
                print(f"  {name}: {res.status} OK (URL: {url})")
        except urllib.error.HTTPError as e:
            print(f"  {name}: HTTP Error {e.code} (URL: {url})")
        except Exception as e:
            print(f"  {name}: Connection Error {e} (URL: {url})")

if __name__ == "__main__":
    verify()
