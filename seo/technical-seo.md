# Technical SEO Settings & Schema Codes
*   **Folder Location:** `seo/technical-seo.md`
*   *Note: Place your JSON-LD schema blocks here. Inject them into WordPress headers or footer blocks.*

---

## 1. LocalBusiness / Service Schema (JSON-LD)
*Replace capitalization labels like `[COMPANY_NAME]` with actual client values.*

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[COMPANY_NAME]",
  "image": "[LOGO_IMAGE_URL]",
  "@id": "[HOMEPAGE_URL]#localbusiness",
  "url": "[HOMEPAGE_URL]",
  "telephone": "[PHONE_NUMBER]",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[STREET_ADDRESS]",
    "addressLocality": "[CITY]",
    "addressRegion": "[STATE_CODE]",
    "postalCode": "[ZIP_CODE]",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": [LATITUDE_COORDINATE],
    "longitude": [LONGITUDE_COORDINATE]
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday"
    ],
    "opens": "08:00",
    "closes": "18:00"
  },
  "sameAs": [
    "[FACEBOOK_URL]",
    "[INSTAGRAM_URL]",
    "[YELP_URL]"
  ]
}
```

---

## 2. FAQ Page Schema (JSON-LD)
*Inject on pages containing FAQ accordions (such as Home, Services, and Contact).*

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "[INSERT_QUESTION_1]",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "[INSERT_ANSWER_1]"
    }
  }, {
    "@type": "Question",
    "name": "[INSERT_QUESTION_2]",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "[INSERT_ANSWER_2]"
    }
  }]
}
```

---

## 3. Crawlability Rules & Sitemaps
*   **Robots.txt Location:** `[SITE_URL]/robots.txt`
*   **Sitemap URL (Usually RankMath or Yoast generated):** `[SITE_URL]/sitemap_index.xml`
*   **XML Sitemap Submission target:** Google Search Console, Bing Webmaster Tools.
