# Pre-Launch Quality Assurance (QA) Checklist
*   **Folder Location:** `launch-checklist.md`
*   *Note: Run this exhaustive checklist before changing DNS or pointing the domain live. Complete all sections.*

---

## 1. Search Engine Optimization (SEO)
- [ ] **Meta Titles:** Check that every published page has a unique meta title under 60 characters with the target keyword and local modifier (City).
- [ ] **Meta Descriptions:** Verify that all pages have unique meta descriptions under 155 characters featuring a clear CTA.
- [ ] **Heading Structure:** Check that there is exactly one H1 tag per page, followed by chronological H2/H3 tags. No empty headings.
- [ ] **JSON-LD Schema:** Test the LocalBusiness and FAQ schemas in Google's Rich Results Test tool. Check that NAP data aligns.
- [ ] **XML Sitemap:** Confirm the sitemap is active at `/sitemap_index.xml` or `/sitemap.xml` and matches the finalized sitemap.
- [ ] **Search Console:** Connect GSC, submit the sitemap URL, and check for crawl errors.
- [ ] **Indexing Settings:** Double-check that `Settings > Reading > Discourage search engines from indexing this site` is **UNCHECKED**.
- [ ] **Canonicals:** Ensure self-referencing canonical link tags exist on all pages to prevent duplicate content issues.
- [ ] **Image Alt Text:** Confirm that every uploaded image has descriptive, keyword-appropriate alt text.
- [ ] **301 Redirects:** Map and configure permanent redirects for any old URLs to match the new structure.

---

## 2. Performance & Mobile Responsiveness
- [ ] **Image Compression:** Verify that all images are WebP/SVG format and compressed under 150KB (Banners) / 80KB (Cards).
- [ ] **Lazy Loading:** Ensure image lazy-loading is active for all below-the-fold media.
- [ ] **Caching Plugin:** Set up cache settings (Litespeed Cache / WP Rocket), active minification for CSS/JS, and database optimization.
- [ ] **Browser Testing:** Test page loads and rendering on Safari, Chrome, Edge, and Firefox.
- [ ] **Mobile Responsiveness:** Manually inspect layouts on iPhone, iPad, and Android screens. Verify buttons are tap-friendly (min 48px height) and spacing behaves.
- [ ] **Lighthouse Speed Test:** Run PageSpeed Insights. Verify desktop performance is 95+ and mobile is 90+.
- [ ] **Cumulative Layout Shift (CLS):** Fix any shifting layout containers, set height/width attributes for logos and image containers.
- [ ] **LCP Optimization:** Preload the hero background image and ensure LCP elements load immediately.

---

## 3. WordPress Security Hardening
- [ ] **Backups:** Configure automated daily backups in Cloudways. Complete and save a manual system snapshot before launch.
- [ ] **WordPress Updates:** Update WordPress Core, active theme, and all active plugins to their latest versions.
- [ ] **User Accounts:** Review active users. Delete any temporary admin accounts. Ensure strong passwords for all active admins.
- [ ] **SSL Certificate:** Check that Let's Encrypt SSL is active in Cloudways and forcing `https://` URLs across the site.
- [ ] **Unused Extensions:** Delete all deactivated, unused, or obsolete themes and plugins from the WordPress dashboard.
- [ ] **Security Monitoring:** Verify that a security monitor (e.g., Wordfence) is installed and active with default protection.
- [ ] **REST API / XML-RPC Security:** Disable XML-RPC pingbacks to block brute force amplification vectors.
- [ ] **Database Prefix:** Ensure the default `wp_` database prefix is altered (if not done during installation).

---

## 4. Site Functionality & Conversion
- [ ] **Form Submissions:** Submit tests through all contact forms. Verify email delivery, data retention in the database, and redirection to the custom "Thank You" page.
- [ ] **Email Delivery (SMTP):** Set up a dedicated SMTP plugin (e.g., WP Mail SMTP) to bypass standard PHP mail and ensure high inbox delivery.
- [ ] **Call Links:** Click every telephone link (`tel:+1...`) on desktop and mobile. Confirm it triggers dialing.
- [ ] **Email Links:** Click all mailto links (`mailto:...`). Confirm they open email clients.
- [ ] **Social Media Links:** Click all icon links. Verify they open target channels in new tabs (`target="_blank"`).
- [ ] **GTM / Google Analytics:** Verify that Google Tag Manager or GA4 tags fire correctly in the Tag Assistant debug portal.
- [ ] **Custom 404 Page:** Visit a broken URL (e.g., `/broken-page/`) and confirm it loads a custom 404 page linking back to the homepage.
- [ ] **Cookie Consent / Privacy Policy:** Confirm a compliant Privacy Policy page is published and linked in the footer.
- [ ] **Favicon:** Verify that the site icon is visible in browser tabs and mobile bookmark bookmarks.
