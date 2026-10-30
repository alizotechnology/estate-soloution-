import re
import os
import sys

sys.path.append('/home/jules/self_created_tools')
from build_portal import generate_header, generate_footer, generate_widgets, LOGO_ANIMATION_CSS

PAGES_MAP = [
    ('index.html', 'home'),
    ('projects/index.html', 'projects'),
    ('buy-sell/index.html', 'buy-sell'),
    ('gallery/index.html', 'gallery'),
    ('contact/index.html', 'contact'),
    ('takmeel-square/index.html', 'projects'),
    ('pelican-mall/index.html', 'projects'),
    ('defence-gardenia-villas/index.html', 'projects'),
    ('privacy-policy/index.html', '')
]

def update_page(filepath, active_route):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Inject LOGO_ANIMATION_CSS before </head>
    if 'LOGOSHIMMER' not in html and '</head>' in html:
        html = html.replace('</head>', f'{LOGO_ANIMATION_CSS}\n</head>')

    # 2. Replace <header>...</header>
    new_header = generate_header(active_route)
    html = re.sub(r'<header.*?</header>', new_header, html, flags=re.DOTALL)

    # 3. Replace <footer>...</footer>
    new_footer = generate_footer()
    html = re.sub(r'<footer.*?</footer>', new_footer, html, flags=re.DOTALL)

    # 4. Remove any existing whatsapp widget before inserting new ones
    html = re.sub(r'<div id="whatsapp-widget".*?</div>\s*<!-- Mobile Fixed Quick Toolbar', '<!-- Mobile Fixed Quick Toolbar', html, flags=re.DOTALL)

    # 5. Inject widgets before </body>
    widgets = generate_widgets()
    if 'id="whatsapp-widget"' not in html and '</body>' in html:
        html = html.replace('</body>', f'{widgets}\n</body>')

    # 6. Clean image URLs
    # Replace external google proxy images with local asset paths
    html = re.sub(r'https://lh3.googleusercontent.com/[^\s"\'<>]+', '/assets/images/logo.jpg', html)
    html = re.sub(r'src="[^"]*takmeel[^"]*"', 'src="/assets/images/takmeel-square.png"', html, flags=re.IGNORECASE)
    html = re.sub(r'src="[^"]*pelican[^"]*"', 'src="/assets/images/pelican-mall.png"', html, flags=re.IGNORECASE)
    html = re.sub(r'src="[^"]*gardenia[^"]*"', 'src="/assets/images/defence-gardenia.png"', html, flags=re.IGNORECASE)

    # 7. Clean up internal data-path and href links
    link_replacements = [
        (r'href="#" data-path="home"', 'href="/"'),
        (r'href="#" data-path="projects"', 'href="/projects"'),
        (r'href="#" data-path="buy-and-sell"', 'href="/buy-sell"'),
        (r'href="#" data-path="gallery"', 'href="/gallery"'),
        (r'href="#" data-path="contact"', 'href="/contact"'),
        (r'href="#" data-path="privacy-policy"', 'href="/privacy-policy"'),
        (r'href="#" data-path="terms-of-service"', 'href="/terms"'),
        (r'href="code\.html"', 'href="/"'),
        (r'data-path="home"', 'href="/"'),
        (r'data-path="projects"', 'href="/projects"'),
        (r'data-path="buy-and-sell"', 'href="/buy-sell"'),
        (r'data-path="gallery"', 'href="/gallery"'),
        (r'data-path="contact"', 'href="/contact"'),
        (r'data-path="privacy-policy"', 'href="/privacy-policy"'),
        (r'data-path="terms-of-service"', 'href="/terms"'),
    ]

    for pattern, replacement in link_replacements:
        html = re.sub(pattern, replacement, html)

    # Clean specific showcase page links
    html = re.sub(r'href="[^"]*takmeel[^"]*"', 'href="/takmeel-square"', html, flags=re.IGNORECASE)
    html = re.sub(r'href="[^"]*pelican[^"]*"', 'href="/pelican-mall"', html, flags=re.IGNORECASE)
    html = re.sub(r'href="[^"]*gardenia[^"]*"', 'href="/defence-gardenia-villas"', html, flags=re.IGNORECASE)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Successfully updated {filepath}")

if __name__ == "__main__":
    for filepath, active_route in PAGES_MAP:
        update_page(filepath, active_route)
