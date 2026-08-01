# WordPress Environment Technical Setup
*   **Folder Location:** `development/technical-notes.md`

---

## 1. WordPress CORE & Server Environment
*   **WordPress Version:** 6.x (Active Rest API confirmed)
*   **Hosting Provider:** Cloudways
*   **PHP Version (Target 8.1+):** 8.x
*   **Database Type / Version:** MariaDB / MySQL
*   **Active Theme (e.g., Astra / Hello Elementor):** Astra (v4.13.6)
*   **Child Theme Active (Yes/No):** No

---

## 2. Core Plugin Stack (Verify Cleanliness)
*Document all installed plugins. Flag any unused, redundant, or security-risk plugins.*

| Plugin Name | Active | Version | Purpose / Role | Recommendation (Keep/Delete/Replace) |
| :--- | :--- | :--- | :--- | :--- |
| **Elementor** | Yes | 4.1.4 | Drag-and-drop page builder | Keep |
| **Essential Addons for Elementor** | Yes | 6.6.11 | Additional Elementor widgets | Keep (check usage) |
| **Fluent Snippets** | Yes | 10.55 | Custom code snippets | Keep |
| **Hayes Template Library** | Yes | 1.0.0 | Template library access | Keep |
| **Rank Math SEO** | Yes | 1.0.273 | Technical SEO & Sitemap management | Keep |
| **Ultimate Addons for Elementor (UAE)** | Yes | 2.9.1 | Additional premium Elementor widgets | Keep |
| **Wordfence Security** | Yes | 8.2.2 | Security & Firewall | Keep |

---

## 3. Performance Tuning Configuration
*   **CDN Configured:** Cloudways CDN / Cloudflare (Pending setup verification)
*   **Image Lazy Loading active:** Yes (WordPress native active)
*   **CSS / JS minification source:** Elementor / Theme Settings

---

## 4. Custom Scripts & Integrations
*   **Header Scripts (`wp_head`):** None loaded currently.
*   **Footer Scripts (`wp_footer`):** None loaded currently.
