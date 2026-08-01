# Internal Linking Anchor & Silo Map
*   **Folder Location:** `seo/internal-links.md`
*   *Note: map internal linking flows to pass page authority and guide user navigation.*

---

## 1. Silo Internal Linking Structure
```
       [Home Page (/)]
        ▲          ▲
        │          │  (Links to Overview & Details)
        ▼          ▼
[Services Overview (/services/)] <──> [Contact/Book (/contact/)]
   ▲            ▲
   │            │ (Silo Links)
   ▼            ▼
[Service Detail 1] <──> [Service Detail 2]
```

---

## 2. Page Link Association Table

| Origin Page URL | Target Page URL | Proposed Anchor Text (Exact Phrase) | Contextual Placement |
| :--- | :--- | :--- | :--- |
| `/` | `/services/` | `view our core services` | Below Hero / Value Proposition Section |
| `/` | `/about/` | `learn more about our team` | Home page intro summary block |
| `/services/` | `/contact/` | `request a free consultation` | Bottom callout block on grid page |
| `/services/subpage-1/` | `/services/` | `back to all services` | Breadcrumb/Link at top or bottom of page |
| `/services/subpage-1/` | `/contact/` | `book your free estimate` | Action button below service description |
| `/locations/city-1/` | `/services/subpage-1/` | `specialized [service 1]` | Bullet points detailing service list in that city |

---

## 3. SEO Interlinking Commandments
1.  **Avoid generic anchor text:** Do *not* link using phrases like "click here," "learn more," or "read website." Use descriptive, keyword-rich anchors (e.g., "our professional [service] services").
2.  **Breadcrumb Trails:** Keep breadcrumbs active on all nested detail subpages (`Home > Services > Service Name`) to ensure clear crawler pathing.
3.  **Cross-Silo Linking:** Limit linking between unrelated services unless highly relevant. Keep authority flowing upward to parent pages.
