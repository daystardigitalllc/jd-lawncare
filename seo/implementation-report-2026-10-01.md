# SEO implementation report: 2026-10-01

Scope: read-only verification of the live site (https://jdslawnandlandscaping.com, WordPress + Rank Math) against this repo. **No live changes were made.** See "Blocked" for why.

## Applied work
None on the live site. This report is the only change in the repo.

## Verified findings (live HTTP checks, 2026-10-01)

| Item | Result | Evidence |
| :--- | :--- | :--- |
| `/services/weekly-lawn-mowing/` | **404 confirmed**, and it is still listed in `page-sitemap.xml` | `curl` returned 404; sitemap lists the URL |
| Internal links to the mowing URL | None found in the live HTML of /, /about/, /services/, /portfolio/, /contact/, /blog/, /service-areas/ or the service pages | grep count 0 on each |
| `/hello-world/` | **200, indexable** (`robots: follow, index`), self-canonical, in `post-sitemap.xml`, default "Welcome to WordPress" text | page source and `post-sitemap.xml` |
| Internal links to `/hello-world/` | None found on the pages checked | grep count 0 |
| `/services/excavating/` | Already exists (200) and is in the sitemap. Do not create another. | HTTP check |
| `robots.txt` | Fine; points to `sitemap_index.xml` | fetched |

Live titles and H1s for the pages in scope (the "before" state):

| URL | Title | H1 |
| :--- | :--- | :--- |
| /services/patios-hardscaping/ | Hardscaper in Clarksville, TN \| Patios & Fire Pits | Patios & Hardscaping |
| /services/retaining-walls/ | Retaining Wall Installation in Clarksville, TN \| JD's Lawn & Landscaping | Retaining Walls |
| /services/landscaping-design-build/ | Garden Design & Landscape Build - Clarksville, TN | Landscape Design & Build |

Not verified, because it needs Search Console or the CMS: GSC data, canonicals on every page, mobile behavior, analytics events, and why the mowing page 404s (draft, trashed, or never published).

## Needs an owner decision

**1. Weekly lawn mowing.** The repo's copy treats mowing as a service (`services-lawn.html`, written for this URL). The live homepage and schema also say "lawn care". But the live site never links the page, so the repo copy appears never to have been published, even though the Rank Math sitemap lists the URL.
- Question for the owner: do you offer recurring mowing?
- If **yes**: publish the page at the same slug using `services-lawn.html`. First confirm the owner-confirmed facts in it (service area, frequency, pricing language). Then link it from /services/ and the homepage.
- If **no**: remove it from the sitemap (check for a Rank Math cache or a draft or trashed copy). Leave it as 404/410, or redirect only to a page that is a true equivalent, such as the "Lawn Care & Maintenance" service if one exists live. Do not redirect to the home page.

**2. `/hello-world/`.** Dependency check found no internal links. Remaining steps are to set the post to noindex or trash it, then remove it from `post-sitemap.xml`. The `/category/uncategorized/` archive may also need noindex. A 410 is cleaner than a redirect, since the page has no value. Rollback: restore from the WP trash or revision.

## Drafts awaiting owner facts (do not publish yet)
For the patio, retaining-wall and design/build pages, add only confirmed facts. Placeholders:
- `[MISSING_FACT: project photos with permission, location by neighborhood, and a one-line scope each]`
- `[MISSING_FACT: wall materials used, typical heights, and whether engineering or permits are handled]`
- `[MISSING_FACT: drainage approach, such as weep drains or gravel backfill, used on real projects]`
- `[MISSING_FACT: patio base and materials, and what maintenance the customer needs to do]`
- Internal links to add from `/portfolio/` to each of the three pages, with descriptive anchors. Add reciprocal links back to the matching portfolio items.
- Existing repo images such as `services-walls.jpg` and `services-patios.jpg` may be stock. Confirm they are real JD's projects before using them as proof.

## Citations and backlinks: all NOT CHECKED
No listing or backlink was researched or created in this pass.
- Facebook is already in the live schema `sameAs`: https://www.facebook.com/profile.php?id=61566707645834. Verify it is live and that its NAP matches.
- NAP to use, from live schema and `client-info/business-info.md`: JD's Lawn & Landscaping, 3213 Old Sango Rd, Clarksville, TN 37043, (931) 801-6180.
- **Inconsistency to resolve before any listing work:** `client-info/business-info.md` has no street address ("Clarksville, TN" only) and says hours are missing, while the live schema shows a street address and 7-day 9:00–17:00 hours. Confirm the owner's real public address and hours. If it is a service-area business, hide the address on the listings.
- The live brand name varies ("JD's Lawn & Landscaping", "JD's Lawn and Landscaping", "JD Lawn and Landscape" in some titles). Pick one form.
- Clarksville Now: pitch only a real community project. Needs an owner story. No outreach has been sent.

## Blocked
- **Live CMS changes.** `MASTER_START_PROMPT.md` contains a WordPress admin application password in plain text in a committed file. I did not use it, because the task requires an authorized CMS session and I have no confirmation from the owner for this one. **Revoke and rotate that password** and remove it from the repo history. Provide CMS access properly if you want me to apply the fixes.
- GSC access for the 28/56/84-day measurement.

## Next three actions
1. Owner confirms whether mowing is offered; then publish the page or remove it from the sitemap (item 1).
2. Rotate the exposed WP application password. Then noindex or trash `/hello-world/` and re-check the sitemaps (item 2).
3. Collect real project photos and facts for the patio, wall and design pages, then fill in the drafts above.

## Update: mowing removed, focus on landscaping and hardscaping (owner decision)
JD's no longer offers mowing. In the repo (source for the WordPress pages) I made these changes:
- Deleted `services-lawn.html` and removed its sitemap and deploy-script entries, so it will not be re-published.
- Removed every internal link to it: footers, service-area pages, the homepage card, the services section, the mulch page cross-link and the portfolio filter and item.
- Removed the "weekly lawn mowing" testimonial, the mowing FAQ and the lawn option from both estimate forms.
- Changed schema (`Offer`, `knowsAbout`, service name) and meta descriptions from "lawn care" to landscaping and hardscaping.
- Homepage title is now "Clarksville, TN Landscapers & Hardscaping | JD's Lawn & Landscaping", to match the `landscapers clarksville tn` query (28 impressions, position 6.8).
- Updated `seo/keyword-research.md` to hardscaping and landscaping targets.
- Filed "Natural Grass Restoration" under Mulching & Design. Owner confirmed (2026-10-01) it is a real project.

**Not yet applied to the live site.** The live page still 404s and is still in the Rank Math sitemap. Live steps (need CMS access): remove it from the sitemap, optionally return a 410, and do not redirect to the home page. After the repo is deployed, check the live pages for any remaining "lawn care" or "mowing" text and old schema. Check the Facebook page, Google Business Profile and other listings for mowing too.
Unused files: `assets/images/mowing1.jpg` and `mowing2.jpg` are no longer referenced. Leave them or delete them as you prefer.
Owner confirmed (2026-10-01) the "licensed & insured", "10+ years" and "commercial" claims are accurate.
