import urllib.request
import urllib.error
import json
import base64
import re
import os

# Configuration
site_url = "https://wordpress-1644135-6589363.cloudwaysapps.com"
username = "admin"
app_password = "hPQz 4D2N SXEG 4MRm Iazu PJkI"
github_pages_assets_base = "https://daystardigitalllc.github.io/jd-lawncare"

# Setup authentication
credentials = f"{username}:{app_password}"
token = base64.b64encode(credentials.encode()).decode()
headers = {
    'Authorization': f'Basic {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Antigravity-WP-Deployer/1.0'
}

def make_request(endpoint, method="GET", data=None):
    url = f"{site_url}/index.php?rest_route={endpoint}"
    req_data = json.dumps(data).encode('utf-8') if data else None
    
    req = urllib.request.Request(url, data=req_data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.status, json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8')
        print(f"HTTP Error {e.code} for {method} {endpoint}: {e.reason}")
        return e.code, None
    except Exception as e:
        print(f"Network error for {method} {endpoint}: {e}")
        return None, None

def get_page_by_slug(slug):
    status, pages = make_request(f"/wp/v2/pages&slug={slug}&status=publish,draft")
    if status == 200 and pages and len(pages) > 0:
        return pages[0]
    return None

def deploy_page(title, slug, html_content, wp_page_id=None):
    payload = {
        'title': title,
        'slug': slug,
        'content': html_content,
        'status': 'publish',
        'template': 'elementor_canvas'
    }
    
    if wp_page_id:
        print(f"Updating existing page ID {wp_page_id} ('{title}', /{slug}/)...")
        status, res = make_request(f"/wp/v2/pages/{wp_page_id}", method="POST", data=payload)
    else:
        existing = get_page_by_slug(slug)
        if existing:
            print(f"Page with slug /{slug}/ already exists (ID: {existing['id']}). Updating it...")
            status, res = make_request(f"/wp/v2/pages/{existing['id']}", method="POST", data=payload)
        else:
            print(f"Creating new page '{title}' (/{slug}/)...")
            status, res = make_request("/wp/v2/pages", method="POST", data=payload)
            
    if status in (200, 201) and res:
        print(f"SUCCESS: Page '{title}' deployed! URL: {res.get('link')}")
        return res.get('id')
    else:
        print(f"FAILED: Page '{title}' deployment failed. Status: {status}")
        return None

def minify_css(css):
    # Remove @import font line
    css = re.sub(r'@import url\([^\)]*\);', '', css)
    # Remove CSS comments
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    # Remove newlines and excess whitespace
    css = re.sub(r'\s+', ' ', css)
    # Remove spaces around layout characters
    css = re.sub(r'\s*([\{\}:;,])\s*', r'\1', css)
    return css.strip()

def minify_html(html):
    # Remove HTML comments
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    # Replace newlines and tabs with spaces
    html = re.sub(r'\s+', ' ', html)
    return html.strip()

def minify_js(js):
    # Remove single line comments
    js_clean = re.sub(r'//.*?\n', '\n', js)
    # Remove block comments
    js_clean = re.sub(r'/\*.*?\*/', '', js_clean, flags=re.DOTALL)
    # Replace double and single newlines/spaces with a single space
    js_clean = re.sub(r'\s+', ' ', js_clean)
    return js_clean.strip()

def process_and_deploy():
    print("Loading and minifying local CSS and JS files...")
    with open("index.css", "r", encoding="utf-8") as f:
        css_content = f.read()
    
    with open("main.js", "r", encoding="utf-8") as f:
        js_content = f.read()
        
    mini_css = minify_css(css_content)
    mini_js = minify_js(js_content)
    
    # Prepend Google Font links as standard HTML tags
    font_links = (
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,500&display=swap" rel="stylesheet">'
    )
    
    css_block = f"{font_links}<style>{mini_css}</style>"
    js_block = f"<script>{mini_js}</script>"

    pages = [
        ("index.html", "Home", "home", 12),
        ("about.html", "About Us", "about", 35),
        ("services.html", "Our Services", "services", 36),
        ("portfolio.html", "Project Portfolio", "portfolio", 37),
        ("contact.html", "Contact & Book", "contact", 38)
    ]
    
    for filename, title, slug, page_id in pages:
        print(f"\nProcessing {filename}...")
        if not os.path.exists(filename):
            print(f"Error: {filename} does not exist. Skipping.")
            continue
            
        with open(filename, "r", encoding="utf-8") as f:
            html = f.read()
            
        body_match = re.search(r"<body[^>]*>(.*?)</body>", html, re.DOTALL)
        body_content = body_match.group(1) if body_match else html
        
        # Minify HTML
        mini_html = minify_html(body_content)
        
        # Combine everything without a single newline character
        page_html = f"{css_block}{mini_html}{js_block}"
        
        # Rewrite asset paths
        page_html = page_html.replace('src="assets/', f'src="{github_pages_assets_base}/assets/')
        page_html = page_html.replace("url('assets/", f"url('{github_pages_assets_base}/assets/")
        page_html = page_html.replace('url("assets/', f'url("{github_pages_assets_base}/assets/')
        
        # Rewrite links to point to WordPress pages using slug routes
        page_html = page_html.replace('href="index.html"', 'href="index.php"')
        page_html = page_html.replace('href="about.html"', 'href="index.php?pagename=about"')
        page_html = page_html.replace('href="services.html"', 'href="index.php?pagename=services"')
        page_html = page_html.replace('href="portfolio.html"', 'href="index.php?pagename=portfolio"')
        page_html = page_html.replace('href="contact.html"', 'href="index.php?pagename=contact"')
        
        # Deploy page!
        deploy_page(title, slug, page_html, wp_page_id=page_id)

if __name__ == "__main__":
    process_and_deploy()
