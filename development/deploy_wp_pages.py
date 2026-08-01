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

def deploy_page(title, slug, html_content, wp_page_id=None, parent_id=0):
    payload = {
        'title': title,
        'slug': slug,
        'content': html_content,
        'status': 'publish',
        'template': 'elementor_canvas',
        'parent': parent_id
    }
    
    if wp_page_id:
        print(f"Updating existing page ID {wp_page_id} ('{title}', /{slug}/, parent: {parent_id})...")
        status, res = make_request(f"/wp/v2/pages/{wp_page_id}", method="POST", data=payload)
    else:
        existing = get_page_by_slug(slug)
        if existing:
            print(f"Page with slug /{slug}/ already exists (ID: {existing['id']}, parent: {parent_id}). Updating it...")
            status, res = make_request(f"/wp/v2/pages/{existing['id']}", method="POST", data=payload)
        else:
            print(f"Creating new page '{title}' (/{slug}/, parent: {parent_id})...")
            status, res = make_request("/wp/v2/pages", method="POST", data=payload)
            
    if status in (200, 201) and res:
        print(f"SUCCESS: Page '{title}' deployed! URL: {res.get('link')}")
        return res.get('id')
    else:
        print(f"FAILED: Page '{title}' deployment failed. Status: {status}")
        return None

def minify_css(css):
    # Remove @import font line if it exists
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
    print("Loading and minifying local global CSS and JS files...")
    with open("index.css", "r", encoding="utf-8") as f:
        global_css = f.read()
    
    with open("main.js", "r", encoding="utf-8") as f:
        js_content = f.read()
        
    mini_global_css = minify_css(global_css)
    mini_js = minify_js(js_content)
    
    # Prepend Google Font links as standard HTML tags
    font_links = (
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,500&display=swap" rel="stylesheet">'
    )
    
    js_block = f"<script>{mini_js}</script>"

    pages = [
        # Format: (filename, title, slug, predefined_id, parent_slug)
        # Core pages
        ("index.html", "Home", "home", 12, None),
        ("about.html", "About Us", "about", 35, None),
        ("services.html", "Our Services", "services", 36, None),
        ("portfolio.html", "Project Portfolio", "portfolio", 37, None),
        ("contact.html", "Contact & Book", "contact", 38, None),
        
        # Subpages under services
        ("services-design.html", "Landscape Design & Build", "landscaping-design-build", None, "services"),
        ("services-mulch.html", "Mulch & Soil Installation", "mulch-soil-installation", None, "services"),
        ("services-walls.html", "Retaining Walls", "retaining-walls", None, "services"),
        ("services-patios.html", "Patios & Hardscaping", "patios-hardscaping", None, "services"),
        ("services-lawn.html", "Weekly Lawn Mowing", "weekly-lawn-mowing", None, "services")
    ]
    
    # Cache for resolved parent slug -> parent ID mappings
    parent_id_cache = {}
    
    for filename, title, slug, page_id, parent_slug in pages:
        print(f"\nProcessing {filename}...")
        if not os.path.exists(filename):
            print(f"Error: {filename} does not exist. Skipping.")
            continue
            
        with open(filename, "r", encoding="utf-8") as f:
            html = f.read()
            
        # 1. Extract any page-specific style overrides in the HTML template (usually in <head>)
        page_styles = re.findall(r"<style[^>]*>(.*?)</style>", html, re.DOTALL)
        page_css = ""
        for style in page_styles:
            page_css += style
            
        mini_page_css = minify_css(page_css) if page_css else ""
        combined_css = mini_global_css + mini_page_css
        css_block = f"{font_links}<style>{combined_css}</style>"
            
        # 2. Extract body content
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
        
        # Rewrite links to point to WordPress pages using pretty permalinks
        page_html = page_html.replace('href="index.html"', 'href="/"')
        page_html = page_html.replace('href="about.html"', 'href="/about/"')
        page_html = page_html.replace('href="services.html"', 'href="/services/"')
        page_html = page_html.replace('href="portfolio.html"', 'href="/portfolio/"')
        page_html = page_html.replace('href="contact.html"', 'href="/contact/"')
        
        # Subpage links
        page_html = page_html.replace('href="services-design.html"', 'href="/services/landscaping-design-build/"')
        page_html = page_html.replace('href="services-mulch.html"', 'href="/services/mulch-soil-installation/"')
        page_html = page_html.replace('href="services-walls.html"', 'href="/services/retaining-walls/"')
        page_html = page_html.replace('href="services-patios.html"', 'href="/services/patios-hardscaping/"')
        page_html = page_html.replace('href="services-lawn.html"', 'href="/services/weekly-lawn-mowing/"')
        
        # Resolve parent ID
        parent_id = 0
        if parent_slug:
            if parent_slug in parent_id_cache:
                parent_id = parent_id_cache[parent_slug]
            else:
                parent_page = get_page_by_slug(parent_slug)
                if parent_page:
                    parent_id = parent_page['id']
                    parent_id_cache[parent_slug] = parent_id
                    print(f"Resolved parent slug '/{parent_slug}/' to page ID: {parent_id}")
                else:
                    print(f"Warning: Parent slug '/{parent_slug}/' could not be resolved! Deploying to root.")
        
        # Deploy page!
        deployed_id = deploy_page(title, slug, page_html, wp_page_id=page_id, parent_id=parent_id)
        
        # If this is the services page itself, make sure it is in our cache
        if slug == "services" and deployed_id:
            parent_id_cache["services"] = deployed_id

if __name__ == "__main__":
    process_and_deploy()
