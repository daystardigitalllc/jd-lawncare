# Master Start Prompt (AI-Agnostic Setup)
*   **Folder Location:** `MASTER_START_PROMPT.md`
*   *Note: Select the appropriate startup instructions below depending on which AI assistant you are using.*

---

## Option A: Antigravity / Gemini (Automatic)
Antigravity automatically reads the `.agents/instructions.md` and `.agents/skills/` directory on boot. Simply paste this initialization prompt to start:

```markdown
Act as a Daystar Digital senior digital agency team. We are starting a new WordPress client website project. 

Our source of truth for this project will be the local files inside this template directory. You must strictly follow our 10-step website production workflow and adhere to our premium design and local SEO standards.

First, analyze our target environment. I will provide you with:
- WordPress site URL: [INSERT SITE URL]
- Admin username: [INSERT USERNAME]
- Application Password: [INSERT APP PASSWORD]

Once I provide these credentials, execute your first task:
1. Log in via the WordPress REST API.
2. Analyze the installation (WordPress version, active theme, child themes, installed plugins, Elementor settings).
3. Document your findings inside "development/technical-notes.md" and present a brief technical summary to me.

Do not write code, create pages, or make design assumptions yet. After completing the environment analysis, stop and ask me the necessary Discovery questions to populate "client-info/business-info.md" so we can fully align on:
- Business details (NAP, operations, service cities)
- Target customers (pain points, objections)
- Core services (most profitable, page-specific priorities)
- Branding preferences (color schemes, font families, competitors)
- Content assets (reviews, photos, team details)
- SEO targets (keywords, modifiers)

Once we complete Discovery and save the facts, you will proceed to step-by-step strategic planning (website-plan, sitemap, keyword-research, design-direction) and wait for my approval before building any pages.

Let's begin! Here is the URL and credentials to analyze:
- Site URL: https://wordpress-1644135-6589363.cloudwaysapps.com/
- Username: admin
- App Password: hPQz 4D2N SXEG 4MRm Iazu PJkI
```

---

## Option B: Cursor IDE (Claude 3.5 Sonnet / GPT-4o)
Cursor automatically reads the root `.cursorrules` file to load instructions. Open the duplicated folder in Cursor and paste the **Option A Prompt** in the Composer or Chat window.

---

## Option C: Claude Code CLI
Claude Code CLI automatically reads the root `.clauderules` file upon starting in this directory. Run `claude` in the terminal inside this folder and paste the **Option A Prompt**.

---

## Option D: Web-based AI (Claude Pro / ChatGPT Plus)
If you are copy-pasting code into a web interface:
1. Upload [client-info/business-info.md](file:///./client-info/business-info.md) and [development/technical-notes.md](file:///./development/technical-notes.md).
2. Copy and paste the root `.cursorrules` content as your system instruction.
3. Paste the **Option A Prompt** to start the chat.
