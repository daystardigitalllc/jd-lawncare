# Visual Identity & CSS Token Map
*   **Folder Location:** `strategy/design-direction.md`

---

## 1. Global Color Tokens
```css
:root {
  /* Core Palette */
  --primary-accent: #62C31C;   /* Vibrant Lime/Leaf Green */
  --secondary-accent: #041C10; /* Luxury Dark Forest Green */
  --secondary-accent-light: #062616; /* Medium Dark Forest Green */
  
  /* Neutral Palette */
  --bg-primary: #F8F6F0;       /* Warm Soft Cream Background */
  --bg-secondary: #FFFFFF;     /* Solid White Card Background */
  --text-dark: #0F1F15;        /* Deep Forest Black for high readability */
  --text-light: #FFFFFF;       /* White for text on dark backgrounds */
  --text-muted: #5B6B60;       /* Dark Olive/Grey for subtitles */
  --border-light: rgba(98, 195, 28, 0.15); /* Subtle Lime Green Border */
  --border-dark: rgba(255, 255, 255, 0.08); /* Subtle border for dark backgrounds */
}
```

---

## 2. Typography Pairings
*   **Headings Font Family (Serif for luxury/trust, or clean Sans for modern contractors):** 
    *   *Google Font:* `Playfair Display` (Serif)
    *   *Weights:* `500` (Medium), `600` (Semi-Bold), `700` (Bold)
*   **Body Copy Font Family:** 
    *   *Google Font:* `Outfit` (Clean Sans-Serif)
    *   *Weights:* `300` (Light), `400` (Regular), `500` (Medium), `600` (Semi-Bold)
*   **Header-to-Body Font Size Tokens:**
    *   `h1`: `3.5rem` (Desktop) / `2.5rem` (Mobile)
    *   `h2`: `2.5rem` (Desktop) / `1.8rem` (Mobile)
    *   `h3`: `1.6rem` (Desktop) / `1.3rem` (Mobile)
    *   `body`: `1.05rem` / Line Height: `1.7`

---

## 3. Custom Styling Guide & Container Overrides
*   **Container Width:** Limit container max-width to `1200px` for boxed sections.
*   **Global Spacing (Padding):**
    *   *Boxed Section Padding:* `80px 40px` (Desktop) / `50px 20px` (Mobile)
    *   *Card Padding:* `30px` (Desktop) / `20px` (Mobile)
*   **Card Styles (e.g., Service list, Reviews):**
    *   `background-color: var(--bg-secondary);`
    *   `border: 1px solid var(--border-light);`
    *   `border-radius: 8px;`
    *   `box-shadow: 0 10px 30px rgba(4, 28, 16, 0.04);`
    *   `transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);`
*   **CTA Button Styling (Primary):**
    *   `background-color: var(--primary-accent);`
    *   `color: var(--text-light);`
    *   `font-weight: 600;`
    *   `border-radius: 30px;`
    *   `padding: 14px 32px;`
    *   `border: 2px solid var(--primary-accent);`
    *   `transition: all 0.3s ease;`
    *   *Hover state:* `background-color: transparent; color: var(--primary-accent); transform: translateY(-2px);`
*   **CTA Button Styling (Secondary):**
    *   `background-color: transparent;`
    *   `color: var(--text-light);`
    *   `font-weight: 600;`
    *   `border-radius: 30px;`
    *   `padding: 14px 32px;`
    *   `border: 2px solid var(--text-light);`
    *   `transition: all 0.3s ease;`
    *   *Hover state:* `background-color: var(--text-light); color: var(--secondary-accent); transform: translateY(-2px);`
