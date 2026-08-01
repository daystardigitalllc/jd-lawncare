# WordPress Environment Technical Setup
*   **Folder Location:** `development/technical-notes.md`
*   *Note: Document the exact environment details here after completing Phase 1: Environment Analysis.*

---

## 1. WordPress CORE & Server Environment
*   **WordPress Version:** 
*   **Hosting Provider:** Cloudways
*   **PHP Version (Target 8.1+):** 
*   **Database Type / Version:** MariaDB / MySQL
*   **Active Theme (e.g., Astra / Hello Elementor):** 
*   **Child Theme Active (Yes/No):** 

---

## 2. Core Plugin Stack (Verify Cleanliness)
*Document all installed plugins. Flag any unused, redundant, or security-risk plugins.*

| Plugin Name | Active | Version | Purpose / Role | Recommendation (Keep/Delete/Replace) |
| :--- | :--- | :--- | :--- | :--- |
| **Elementor (Pro)** | | | Drag-and-drop page builder | Keep |
| **RankMath SEO** | | | Technical SEO & Sitemap management | Keep |
| **LiteSpeed Cache / WP Rocket** | | | Performance tuning & file compression | Keep |
| **Wordfence Security** | | | Firewall & security monitoring | Keep |
| **Fluent Forms / Gravity Forms** | | | Lead generation contact forms | Keep |

---

## 3. Performance Tuning Configuration
*   **CDN Configured:** (Yes/No - detail if Cloudflare / Cloudways CDN)
*   **Image Lazy Loading active:** 
*   **CSS / JS minification source:** 
*   **Database Cleanup schedule:** 

---

## 4. Custom Scripts & Integrations
*List any scripts injected into the header (`wp_head`) or footer (`wp_footer`), such as Google Tag Manager, Meta Pixel, or local schema scripts.*

*   **Header Scripts (`wp_head`):**
    ```html
    <!-- Insert any custom tracking or font stylesheet links here -->
    ```
*   **Footer Scripts (`wp_footer`):**
    ```html
    <!-- Insert any chat widgets, analytics scripts here -->
    ```
