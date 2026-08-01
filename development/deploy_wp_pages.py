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
        try:
            err_json = json.loads(body)
            print(f"Server response details: {json.dumps(err_json, indent=2)}")
        except:
            print(f"Server response body: {body[:300]}")
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
    # Set elementor_canvas template so the page renders full width overriding the theme's header/footer
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
        # Check if page already exists by slug
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

def process_and_deploy():
    # 1. Read global CSS and JS
    print("Loading local CSS and JS files...")
    with open("index.css", "r", encoding="utf-8") as f:
        css_content = f.read()
    
    with open("main.js", "r", encoding="utf-8") as f:
        js_content = f.read()
        
    css_block = f"<style>\n{css_content}\n</style>"
    js_block = f"<script>\n{js_content}\n</script>"

    # Define pages to deploy
    # (HTML filename, Page Title, Slug, Page ID if existing)
    pages = [
        ("index.html", "Home", "home", 12),
        ("about.html", "About Us", "about", None),
        ("services.html", "Our Services", "services", None),
        ("portfolio.html", "Project Portfolio", "portfolio", None),
        ("contact.html", "Contact & Book", "contact", None)
    ]
    
    for filename, title, slug, page_id in pages:
        print(f"\nProcessing {filename}...")
        if not os.path.exists(filename):
            print(f"Error: {filename} does not exist. Skipping.")
            continue
            
        with open(filename, "r", encoding="utf-8") as f:
            html = f.read()
            
        # Extract body content if we only want to upload body, but since elementor_canvas
        # hides headers and footers, we can inject our custom CSS/JS directly into the page content.
        # Let's clean the HTML: remove DOCTYPE, html, head tags, since WordPress will wrap page content.
        # But we need our header and footer! The easiest way is to extract everything inside the <body> tag,
        # and append the <style> block at the top and <script> block at the bottom of the body.
        body_match = re.search(r"<body[^>]*>(.*?)</body>", html, re.DOTALL)
        if body_match:
            body_content = body_match.group(1)
        else:
            body_content = html
            
        # Inline styles and scripts
        page_html = f"{css_block}\n{body_content}\n{js_block}"
        
        # Rewrite asset paths to point to GitHub Pages raw static assets
        # Example: assets/images/hero-bg.jpg -> https://daystardigitalllc.github.io/jd-lawncare/assets/images/hero-bg.jpg
        page_html = page_html.replace('src="assets/', f'src="{github_pages_assets_base}/assets/')
        # Also handle any css background-image properties: url('assets/images/...')
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
