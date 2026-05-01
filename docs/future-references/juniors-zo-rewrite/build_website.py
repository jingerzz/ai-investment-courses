#!/usr/bin/env python3
"""Build the juniors course website HTML files from markdown source."""

import os, re, json, html

OUT = "/home/.z/workspaces/con_uWUN7K7zYpM9KwEZ/juniors-site"
SRC = "/home/workspace/ai-investment-courses/juniors"

os.makedirs(f"{OUT}/css", exist_ok=True)
os.makedirs(f"{OUT}/js", exist_ok=True)

# ─── Helper: markdown to HTML (lightweight, no deps) ───

def md_to_html(md_text):
    """Convert markdown to HTML. Handles headers, paragraphs, lists, tables, code blocks, blockquotes, bold, italic, inline code."""
    lines = md_text.split('\n')
    result = []
    in_code = False
    code_buf = []
    in_table = False
    table_buf = []
    in_list = False
    list_buf = []
    in_blockquote = False
    bq_buf = []

    def flush_list():
        nonlocal in_list, list_buf
        if list_buf:
            items = '\n'.join(f'<li>{inline(l)}</li>' for l in list_buf)
            result.append(f'<ul>{items}</ul>')
            list_buf = []
            in_list = False

    def flush_blockquote():
        nonlocal in_blockquote, bq_buf
        if bq_buf:
            # Detect "Investing 101" sidebars
            content = '\n'.join(bq_buf)
            if 'Investing 101:' in content or 'Investing 101 —' in content:
                # Extract title and body
                bq_lines = content.split('\n')
                title_line = bq_lines[0]
                # Extract title text after "Investing 101:"
                title_match = re.search(r'Investing 101[:\s—]+(.+)', title_line)
                title_text = title_match.group(1).strip() if title_match else "Investing 101"
                body_lines = [l for l in bq_lines[1:] if l.strip()]
                body_html = ' '.join(inline(l) for l in body_lines)
                result.append(f'''<div class="callout investing-101">
<div class="callout-title">💡 Investing 101: {html.escape(title_text)}</div>
<p>{body_html}</p>
</div>''')
            else:
                body_html = ' '.join(inline(l) for l in bq_buf if l.strip())
                result.append(f'<blockquote><p>{body_html}</p></blockquote>')
            bq_buf = []
            in_blockquote = False

    def flush_table():
        nonlocal in_table, table_buf
        if table_buf:
            rows = []
            for i, row_text in enumerate(table_buf):
                cells = [c.strip() for c in row_text.strip('|').split('|')]
                if i == 1 and all(re.match(r'^[-:]+$', c) for c in cells):
                    continue  # separator row
                tag = 'th' if i == 0 else 'td'
                cells_html = ''.join(f'<{tag}>{inline(c)}</{tag}>' for c in cells)
                wrap = 'thead' if i == 0 else ''
                rows.append(f'<tr>{cells_html}</tr>')
            header = f'<thead>{rows[0]}</thead>' if rows else ''
            body = f'<tbody>{"".join(rows[1:])}</tbody>' if len(rows) > 1 else ''
            result.append(f'<table>{header}{body}</table>')
            table_buf = []
            in_table = False

    def inline(text):
        """Process inline markdown: bold, italic, code, links."""
        text = html.escape(text)
        # inline code
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        # bold+italic
        text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
        # bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        # italic
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        # links
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        return text

    for line in lines:
        # Code blocks
        if line.strip().startswith('```'):
            if in_code:
                code_text = html.escape('\n'.join(code_buf))
                result.append(f'<pre><code>{code_text}</code></pre>')
                code_buf = []
                in_code = False
            else:
                flush_list()
                flush_blockquote()
                flush_table()
                in_code = True
            continue
        if in_code:
            code_buf.append(line)
            continue

        # Table rows
        if '|' in line and line.strip().startswith('|'):
            flush_list()
            flush_blockquote()
            in_table = True
            table_buf.append(line)
            continue
        elif in_table:
            flush_table()

        # Blockquotes
        if line.startswith('> ') or line.strip() == '>':
            flush_list()
            in_blockquote = True
            bq_buf.append(line.lstrip('> ').strip())
            continue
        elif in_blockquote and line.strip() == '':
            # could be continuation or end
            pass
        elif in_blockquote and not line.startswith('>'):
            flush_blockquote()

        # Lists
        stripped = line.strip()
        if re.match(r'^[-*]\s', stripped) or re.match(r'^\d+\.\s', stripped):
            flush_blockquote()
            in_list = True
            item_text = re.sub(r'^[-*\d.]+\s*', '', stripped)
            list_buf.append(item_text)
            continue
        elif in_list and stripped == '':
            pass  # blank line in list context
        elif in_list and stripped:
            flush_list()

        # Horizontal rules
        if re.match(r'^---+$', stripped):
            flush_list()
            flush_blockquote()
            result.append('<hr>')
            continue

        # Headers
        m = re.match(r'^(#{1,4})\s+(.+)', line)
        if m:
            flush_list()
            flush_blockquote()
            level = len(m.group(1))
            text = inline(m.group(2))
            result.append(f'<h{level}>{text}</h{level}>')
            continue

        # Empty line
        if stripped == '':
            continue

        # Paragraph
        flush_list()
        result.append(f'<p>{inline(stripped)}</p>')

    # Flush remaining
    flush_list()
    flush_blockquote()
    flush_table()
    if code_buf:
        code_text = html.escape('\n'.join(code_buf))
        result.append(f'<pre><code>{code_text}</code></pre>')

    return '\n\n'.join(result)


def read_md(path):
    with open(path) as f:
        content = f.read()
    # Strip YAML frontmatter
    if content.startswith('---'):
        end = content.find('---', 3)
        if end > 0:
            content = content[end+3:].strip()
    return content


def page_template(title, body_html, current_page):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)} | AI-Powered Investing for Juniors</title>
  <link rel="stylesheet" href="css/course.css">
</head>
<body>
  <div class="page-wrapper">
    <div class="content">
{body_html}
    </div>
  </div>
  <script src="js/nav.js?v=2" data-current="{current_page}"></script>
</body>
</html>'''


def tab_page_template(title, chapter_label, meta_html, reading_html, exercise_html, checklist_html, current_page, conversation_html=None, ref_solution_html=None):
    tabs = [
        ('tab-reading', 'Reading', reading_html),
        ('tab-exercise', 'Exercise', exercise_html),
        ('tab-checklist', 'Checklist', checklist_html),
    ]
    if conversation_html:
        tabs.append(('tab-conversation', 'Conversation Guide', conversation_html))
    if ref_solution_html:
        tabs.append(('tab-reference', 'Reference Solution', ref_solution_html))

    tab_buttons = '\n        '.join(
        f'<button class="section-tab{" active" if i==0 else ""}" data-tab="{tid}">{label}</button>'
        for i, (tid, label, _) in enumerate(tabs)
    )
    tab_contents = '\n\n      '.join(
        f'<div id="{tid}" class="tab-content{" active" if i==0 else ""}">\n{content}\n      </div>'
        for i, (tid, _, content) in enumerate(tabs)
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)} | AI-Powered Investing for Juniors</title>
  <link rel="stylesheet" href="css/course.css">
</head>
<body>
  <div class="page-wrapper">
    <div class="content">
      <div class="chapter-header">
        <div class="chapter-label">{html.escape(chapter_label)}</div>
        <h1>{html.escape(title)}</h1>
        <div class="chapter-meta">
          {meta_html}
        </div>
      </div>

      <div class="section-tabs">
        {tab_buttons}
      </div>

      {tab_contents}
    </div>
  </div>
  <script src="js/nav.js?v=2" data-current="{current_page}"></script>
  <script>
  document.querySelectorAll('.section-tab').forEach(btn => {{
    btn.addEventListener('click', () => {{
      document.querySelectorAll('.section-tab').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById(btn.dataset.tab).classList.add('active');
    }});
  }});
  </script>
</body>
</html>'''


# ─── Build CSS ───
CSS = '''/* ============================================================
   AI-Powered Investing for Juniors — Course CSS
   Brand: juniors.md
   ============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --primary:        #1A73E8;
  --primary-light:  #4A90D9;
  --secondary:      #F59E0B;

  --surface:        #FFFFFF;
  --surface-alt:    #F0F4F8;
  --text:           #1F2937;
  --text-muted:     #6B7280;
  --border:         #D1D5DB;

  --success:        #059669;
  --danger:         #DC2626;
  --info:           #1A73E8;

  --code-bg:        #F8FAFC;
  --code-text:      #334155;
  --code-comment:   #94A3B8;
  --code-keyword:   #1A73E8;
  --code-string:    #059669;
  --code-number:    #D97706;

  --xs: 8px;  --sm: 16px;  --md: 24px;  --lg: 32px;  --xl: 48px;  --xxl: 64px;
  --content-width:  720px;
  --wide-width:     960px;
  --page-padding:   48px;
}

*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
html { font-size: 17px; scroll-behavior: smooth; }
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: var(--text);
  background: var(--surface);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 { font-weight: 700; line-height: 1.2; color: var(--primary); }
h1 { font-size: 2rem; margin-bottom: var(--md); }
h2 {
  font-size: 1.5rem; font-weight: 600;
  margin-top: var(--xxl); margin-bottom: var(--md);
  padding-bottom: var(--xs);
  border-bottom: 2px solid var(--secondary);
}
h3 { font-size: 1.18rem; font-weight: 600; color: var(--text); margin-top: var(--xl); margin-bottom: var(--sm); }

p { margin-bottom: var(--sm); max-width: 65ch; }
p.lead { font-size: 1.06rem; line-height: 1.7; color: var(--text); }

a { color: var(--primary); text-decoration: none; }
a:hover { color: var(--primary-light); text-decoration: underline; }
strong { font-weight: 600; }

.page-wrapper { min-height: 100vh; display: flex; flex-direction: column; }
.content {
  max-width: var(--content-width);
  margin: 0 auto;
  padding: var(--xl) var(--page-padding);
  flex: 1;
}
.content-wide {
  max-width: var(--wide-width);
  margin: 0 auto;
  padding: var(--xl) var(--page-padding);
  flex: 1;
}

/* --- Nav --- */
.site-nav {
  background: var(--primary);
  color: white;
  padding: 0 var(--page-padding);
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid rgba(255,255,255,0.12);
}
.site-nav-inner {
  max-width: var(--wide-width);
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 56px;
}
.site-nav .brand {
  font-weight: 700;
  font-size: 0.9rem;
  letter-spacing: 0.02em;
  color: white;
  text-decoration: none;
  white-space: nowrap;
}
.site-nav .nav-links {
  display: flex;
  gap: 0;
  align-items: center;
  list-style: none;
  overflow-x: auto;
}
.site-nav .nav-links a {
  display: block;
  padding: var(--sm) var(--sm);
  font-size: 0.8rem;
  font-weight: 500;
  color: rgba(255,255,255,0.7);
  text-decoration: none;
  white-space: nowrap;
  transition: color 0.2s;
}
.site-nav .nav-links a:hover,
.site-nav .nav-links a.active { color: white; }
.site-nav .nav-links a.active { border-bottom: 2px solid var(--secondary); }

/* --- Chapter Header --- */
.chapter-header {
  margin-bottom: var(--xl);
  padding-bottom: var(--lg);
  border-bottom: 1px solid var(--border);
}
.chapter-header .chapter-label {
  font-size: 0.8rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--secondary);
  margin-bottom: var(--xs);
}
.chapter-header h1 { margin-bottom: var(--sm); }
.chapter-header .chapter-meta {
  font-size: 0.875rem;
  color: var(--text-muted);
}
.chapter-header .chapter-meta span + span::before {
  content: "·";
  margin: 0 var(--xs);
}

/* --- Section Tabs --- */
.section-tabs {
  display: flex;
  gap: 0;
  border-bottom: 2px solid var(--border);
  margin-bottom: var(--lg);
}
.section-tab {
  padding: var(--sm) var(--md);
  font-family: inherit;
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--text-muted);
  background: none;
  border: none;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  margin-bottom: -2px;
  transition: color 0.2s;
}
.section-tab:hover { color: var(--primary); }
.section-tab.active {
  color: var(--primary);
  border-bottom-color: var(--primary);
  font-weight: 600;
}
.tab-content { display: none; }
.tab-content.active { display: block; }

/* --- Code --- */
pre {
  background: var(--code-bg);
  color: var(--code-text);
  padding: var(--md);
  overflow-x: auto;
  font-size: 0.82rem;
  line-height: 1.6;
  border: 1px solid var(--border);
  border-radius: 4px;
  margin: var(--md) 0;
}
code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.88em;
}
p code, li code, td code {
  background: var(--code-bg);
  padding: 2px 6px;
  border-radius: 3px;
  border: 1px solid var(--border);
}

/* --- Tables --- */
table {
  width: 100%;
  border-collapse: collapse;
  margin: var(--md) 0;
  font-size: 0.88rem;
}
thead th {
  background: var(--primary);
  color: white;
  font-weight: 600;
  text-align: left;
  padding: 10px 14px;
}
tbody td {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
}
tbody tr:nth-child(even) { background: var(--surface-alt); }

/* --- Callouts --- */
.callout {
  padding: var(--md);
  margin: var(--lg) 0;
  border-left: 4px solid var(--primary);
  background: var(--surface-alt);
}
.callout-title {
  font-weight: 700;
  font-size: 0.9rem;
  margin-bottom: var(--xs);
  color: var(--primary);
}
.callout.investing-101 {
  background: #FFFBEB;
  border-left-color: var(--secondary);
}
.callout.investing-101 .callout-title {
  color: var(--secondary);
}
.callout.warning {
  background: #FEF2F2;
  border-left-color: var(--danger);
}
.callout.warning .callout-title {
  color: var(--danger);
}

/* --- Blockquotes --- */
blockquote {
  padding: var(--md);
  margin: var(--lg) 0;
  border-left: 4px solid var(--primary);
  background: var(--surface-alt);
}
blockquote p { margin-bottom: 0; }

/* --- Lists --- */
ul, ol {
  margin: var(--sm) 0 var(--md) 1.5rem;
  line-height: 1.7;
}
li { margin-bottom: 6px; }

/* --- Hero --- */
.hero {
  background: var(--primary);
  color: white;
  padding: var(--xl) 0;
}
.hero h1 { color: white; margin-bottom: var(--sm); }
.hero .tagline {
  font-size: 1.06rem;
  opacity: 0.9;
  max-width: 55ch;
  line-height: 1.7;
}

/* --- Week Grid --- */
.week-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--sm);
  margin: var(--md) 0;
}
.week-card {
  display: block;
  border: 1px solid var(--border);
  padding: var(--md);
  text-decoration: none;
  color: var(--text);
  transition: border-color 0.2s, box-shadow 0.2s;
  border-radius: 6px;
}
.week-card:hover {
  border-color: var(--primary);
  box-shadow: 0 2px 8px rgba(26,115,232,0.1);
  text-decoration: none;
}
.week-card .card-label {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--secondary);
  margin-bottom: 6px;
}
.week-card .card-title {
  font-weight: 700;
  font-size: 1rem;
  color: var(--primary);
  margin-bottom: 8px;
}
.week-card .card-desc {
  font-size: 0.82rem;
  color: var(--text-muted);
  line-height: 1.6;
}

/* --- Checklist --- */
.checklist-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 8px 0;
}
.checklist-item input[type="checkbox"] {
  accent-color: var(--primary);
  width: 18px;
  height: 18px;
  margin-top: 2px;
  flex-shrink: 0;
}

/* --- Page Nav (prev/next) --- */
.page-nav {
  display: flex;
  justify-content: space-between;
  margin-top: var(--xxl);
  padding-top: var(--lg);
  border-top: 1px solid var(--border);
}
.page-nav a {
  text-decoration: none;
  color: var(--text);
}
.page-nav a:hover { color: var(--primary); }
.page-nav .nav-label {
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.page-nav .nav-title { font-weight: 600; margin-top: 4px; }

/* --- Footer --- */
.site-footer {
  background: var(--surface-alt);
  border-top: 1px solid var(--border);
  padding: var(--lg) var(--page-padding);
  margin-top: auto;
}
.site-footer-inner {
  max-width: var(--wide-width);
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.footer-brand { font-size: 0.8rem; font-weight: 600; color: var(--primary); }
.footer-note { font-size: 0.8rem; color: var(--text-muted); }

/* --- Progress Tracker --- */
.progress-tracker {
  display: flex;
  gap: 8px;
  margin: var(--md) 0;
  flex-wrap: wrap;
}
.progress-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.78rem;
  padding: 4px 10px;
  border-radius: 20px;
  background: var(--surface-alt);
  border: 1px solid var(--border);
}
.progress-item.active {
  background: var(--primary);
  color: white;
  border-color: var(--primary);
}
.progress-item.done {
  background: #ECFDF5;
  color: var(--success);
  border-color: var(--success);
}

/* --- Responsive --- */
@media (max-width: 768px) {
  :root { --page-padding: 20px; }
  html { font-size: 16px; }
  h1 { font-size: 1.6rem; }
  h2 { font-size: 1.3rem; }
  .week-grid { grid-template-columns: 1fr; }
  .site-nav .brand { font-size: 0.8rem; }
  .site-nav .nav-links a { padding: 12px 8px; font-size: 0.75rem; }
}
'''

with open(f"{OUT}/css/course.css", 'w') as f:
    f.write(CSS)
print(f"✓ CSS written")


# ─── Build nav.js ───
NAV_JS = '''(function () {
  const pages = [
    { id: "home",       href: "index.html",       label: "Home" },
    { id: "prerequisites", href: "prerequisites.html", label: "Prerequisites" },
    { id: "week-1",     href: "week-1.html",      label: "Week 1" },
    { id: "week-2",     href: "week-2.html",      label: "Week 2" },
    { id: "bonus",      href: "bonus.html",        label: "Bonus" },
    { id: "week-3",     href: "week-3.html",      label: "Week 3" },
    { id: "week-4",     href: "week-4.html",      label: "Week 4" },
    { id: "conclusion", href: "conclusion.html",  label: "Conclusion" },
    { id: "glossary",   href: "glossary.html",    label: "Glossary" },
  ];

  const script = document.currentScript;
  const current = script ? script.getAttribute("data-current") : "";

  const nav = document.createElement("nav");
  nav.className = "site-nav";
  nav.innerHTML = `
    <div class="site-nav-inner">
      <a class="brand" href="index.html">AI-Powered Investing for Juniors</a>
      <div class="nav-links">
        ${pages.map(p =>
          `<a href="${p.href}" class="${p.id === current ? 'active' : ''}">${p.label}</a>`
        ).join("")}
      </div>
    </div>
  `;

  const footer = document.createElement("footer");
  footer.className = "site-footer";
  footer.innerHTML = `
    <div class="site-footer-inner">
      <span class="footer-brand">AI Investment Academy — Juniors</span>
      <span class="footer-note">Build AI stock tools. No coding required.</span>
    </div>
  `;

  const idx = pages.findIndex(p => p.id === current);
  if (idx > 0) {
    const prev = idx > 0 ? pages[idx - 1] : null;
    const next = idx < pages.length - 1 ? pages[idx + 1] : null;
    const pageNav = document.createElement("div");
    pageNav.className = "page-nav";
    pageNav.innerHTML = `
      ${prev ? `<a href="${prev.href}"><div class="nav-label">&larr; Previous</div><div class="nav-title">${prev.label}</div></a>` : '<span></span>'}
      ${next ? `<a href="${next.href}"><div class="nav-label">Next &rarr;</div><div class="nav-title">${next.label}</div></a>` : '<span></span>'}
    `;
    document.addEventListener("DOMContentLoaded", () => {
      const content = document.querySelector(".content") || document.querySelector(".content-wide");
      if (content) content.appendChild(pageNav);
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    const wrapper = document.querySelector(".page-wrapper");
    if (wrapper) {
      wrapper.prepend(nav);
      wrapper.appendChild(footer);
    }
  });
})();
'''

with open(f"{OUT}/js/nav.js", 'w') as f:
    f.write(NAV_JS)
print(f"✓ nav.js written")


# ─── Build index.html ───
INDEX = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI-Powered Investing for Juniors — Course</title>
  <link rel="stylesheet" href="css/course.css">
</head>
<body>
  <div class="page-wrapper">
    <div class="hero">
      <div class="content">
        <h1>AI-Powered Investing for Juniors</h1>
        <p class="tagline">Build AI-powered stock tools — no coding required. Track real companies like Roblox, Spotify, and Snapchat using AI you build yourself.</p>
      </div>
    </div>

    <div class="content-wide">
      <h2>Course Overview</h2>
      <div class="week-grid">
        <a href="prerequisites.html" class="week-card">
          <div class="card-label">Before You Start</div>
          <div class="card-title">Prerequisites</div>
          <div class="card-desc">Install Claude Desktop, Claude Code, and uv. Takes about 15 minutes. No coding experience needed.</div>
        </a>
        <a href="week-1.html" class="week-card">
          <div class="card-label">Week 1</div>
          <div class="card-title">Connecting AI to Real Data</div>
          <div class="card-desc">Build a stock tracker that gives Claude access to real prices for Roblox, Spotify, Snapchat, and more. Learn what stocks are and how AI connects to data.</div>
        </a>
        <a href="week-2.html" class="week-card">
          <div class="card-label">Week 2</div>
          <div class="card-title">Teaching AI Not to Make Mistakes</div>
          <div class="card-desc">Add safety checks so AI doesn't make math mistakes or show old data. Build a daily stock report with guardrails.</div>
        </a>
        <a href="bonus.html" class="week-card">
          <div class="card-label">Bonus</div>
          <div class="card-title">Private Document Search with Ollama</div>
          <div class="card-desc">Run AI entirely on your computer. Build a private document reader for company annual reports — no data leaves your machine.</div>
        </a>
        <a href="week-3.html" class="week-card">
          <div class="card-label">Week 3</div>
          <div class="card-title">Designing Bigger Systems</div>
          <div class="card-desc">Design how multiple AI tools work together. Think about systems, not just individual tools. Plan a stock club architecture.</div>
        </a>
        <a href="week-4.html" class="week-card">
          <div class="card-label">Week 4</div>
          <div class="card-title">Building a Stock Monitor</div>
          <div class="card-desc">Build an AI that watches your stocks and alerts you when something big happens. Learn why AI needs human approval.</div>
        </a>
        <a href="conclusion.html" class="week-card">
          <div class="card-label">Conclusion</div>
          <div class="card-title">What You\'ve Built</div>
          <div class="card-desc">Review your complete system and see what\'s possible next.</div>
        </a>
        <a href="glossary.html" class="week-card">
          <div class="card-label">Reference</div>
          <div class="card-title">Glossary</div>
          <div class="card-desc">Finance and technology terms explained in plain English.</div>
        </a>
      </div>
    </div>

    <div class="content">
      <h2>How It Works</h2>
      <p>Each week has two parts: <strong>30 minutes reading</strong> and <strong>30 minutes building</strong>. You describe what you want in plain English, and Claude builds it for you.</p>
      <p>By the end of four weeks, you'll have built a complete set of AI-powered stock tools — a tracker, a daily report, a multi-server system, and a stock monitor with alerts.</p>
      <p>The companies you'll track: <strong>Roblox</strong> (RBLX), <strong>Snapchat</strong> (SNAP), <strong>Spotify</strong> (SPOT), <strong>Duolingo</strong> (DUOL), <strong>Crocs</strong> (CROX) — plus Take-Two, Netflix, and Disney for comparisons.</p>

      <h2>Who This Is For</h2>
      <p>High school students (grades 8-10) curious about investing and AI. No coding or finance knowledge required. You just need curiosity and about an hour a week.</p>
    </div>
  </div>
  <script src="js/nav.js?v=2" data-current="home"></script>
</body>
</html>'''

with open(f"{OUT}/index.html", 'w') as f:
    f.write(INDEX)
print("✓ index.html written")


# ─── Build simple pages (prerequisites, conclusion, glossary, introduction) ───

# Prerequisites
prereqs_md = read_md(f"{SRC}/prerequisites.md")
prereqs_html = md_to_html(prereqs_md)
prereqs_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prerequisites | AI-Powered Investing for Juniors</title>
  <link rel="stylesheet" href="css/course.css">
</head>
<body>
  <div class="page-wrapper">
    <div class="content">
      <div class="chapter-header">
        <div class="chapter-label">Before You Start</div>
        <h1>Prerequisites</h1>
        <div class="chapter-meta">
          <span>Week 1 setup: ~15 minutes</span>
          <span>Bonus setup: ~15 minutes</span>
        </div>
      </div>
      <p class="lead">Everything you need before starting the course. Week 1 requires minimal setup. The bonus module's Ollama setup can be done later.</p>
{prereqs_html}
    </div>
  </div>
  <script src="js/nav.js?v=2" data-current="prerequisites"></script>
</body>
</html>'''
with open(f"{OUT}/prerequisites.html", 'w') as f:
    f.write(prereqs_page)
print("✓ prerequisites.html written")

# Conclusion
conclusion_md = read_md(f"{SRC}/conclusion.md")
conclusion_html = md_to_html(conclusion_md)
conclusion_page = page_template("What You've Built", conclusion_html, "conclusion")
with open(f"{OUT}/conclusion.html", 'w') as f:
    f.write(conclusion_page)
print("✓ conclusion.html written")

# Glossary
glossary_md = read_md(f"{SRC}/glossary.md")
glossary_html = md_to_html(glossary_md)
glossary_page = page_template("Glossary", glossary_html, "glossary")
with open(f"{OUT}/glossary.html", 'w') as f:
    f.write(glossary_page)
print("✓ glossary.html written")


# ─── Build weekly tabbed pages ───

weeks = [
    {
        'id': 'week-1',
        'label': 'Week 1',
        'title': 'Connecting AI to Real Data',
        'meta': '<span>Reading: 30 minutes</span><span>Exercise: 30 minutes</span>',
        'reading': f"{SRC}/week-1/reading.md",
        'exercise': f"{SRC}/week-1/exercise/README.md",
        'checklist': f"{SRC}/week-1/exercise/checklist.md",
        'conversation': f"{SRC}/week-1/exercise/conversation_guide.md",
        'reference': f"{SRC}/week-1/exercise/reference_solution.md",
    },
    {
        'id': 'week-2',
        'label': 'Week 2',
        'title': 'Teaching AI Not to Make Mistakes',
        'meta': '<span>Reading: 30 minutes</span><span>Exercise: 30 minutes</span>',
        'reading': f"{SRC}/week-2/reading.md",
        'exercise': f"{SRC}/week-2/exercise/README.md",
        'checklist': f"{SRC}/week-2/exercise/checklist.md",
        'conversation': f"{SRC}/week-2/exercise/conversation_guide.md",
        'reference': f"{SRC}/week-2/exercise/reference_solution.md",
    },
    {
        'id': 'week-3',
        'label': 'Week 3',
        'title': 'Designing Bigger Systems',
        'meta': '<span>Reading: 30 minutes</span><span>Exercise: 30 minutes</span>',
        'reading': f"{SRC}/week-3/reading.md",
        'exercise': f"{SRC}/week-3/exercise/README.md",
        'checklist': f"{SRC}/week-3/exercise/checklist.md",
        'conversation': f"{SRC}/week-3/exercise/conversation_guide.md",
        'reference': f"{SRC}/week-3/exercise/reference_solution.md",
    },
    {
        'id': 'week-4',
        'label': 'Week 4',
        'title': 'Building a Stock Monitor',
        'meta': '<span>Reading: 30 minutes</span><span>Exercise: 30 minutes</span>',
        'reading': f"{SRC}/week-4/reading.md",
        'exercise': f"{SRC}/week-4/exercise/README.md",
        'checklist': f"{SRC}/week-4/exercise/checklist.md",
        'conversation': f"{SRC}/week-4/exercise/conversation_guide.md",
        'reference': f"{SRC}/week-4/exercise/reference_solution.md",
    },
]

for w in weeks:
    reading_html = md_to_html(read_md(w['reading']))
    exercise_html = md_to_html(read_md(w['exercise']))
    checklist_html = md_to_html(read_md(w['checklist']))
    conversation_html = md_to_html(read_md(w['conversation'])) if os.path.exists(w.get('conversation', '')) else None
    reference_html = md_to_html(read_md(w['reference'])) if os.path.exists(w.get('reference', '')) else None

    page = tab_page_template(
        w['title'], w['label'], w['meta'],
        reading_html, exercise_html, checklist_html,
        w['id'], conversation_html, reference_html
    )
    with open(f"{OUT}/{w['id']}.html", 'w') as f:
        f.write(page)
    print(f"✓ {w['id']}.html written")


# ─── Build bonus page ───
bonus_reading = md_to_html(read_md(f"{SRC}/bonus-local-rag/reading.md"))
bonus_exercise = md_to_html(read_md(f"{SRC}/bonus-local-rag/exercise/README.md"))
bonus_checklist = md_to_html(read_md(f"{SRC}/bonus-local-rag/exercise/checklist.md"))
bonus_conversation = md_to_html(read_md(f"{SRC}/bonus-local-rag/exercise/conversation_guide.md"))
bonus_reference = md_to_html(read_md(f"{SRC}/bonus-local-rag/exercise/reference_solution.md"))

bonus_page = tab_page_template(
    'Private Document Search with Ollama', 'Bonus Module',
    '<span>Reading: 30 minutes</span><span>Exercise: 45-60 minutes</span>',
    bonus_reading, bonus_exercise, bonus_checklist,
    'bonus', bonus_conversation, bonus_reference
)
with open(f"{OUT}/bonus.html", 'w') as f:
    f.write(bonus_page)
print("✓ bonus.html written")

print(f"\n✅ All files written to {OUT}")
print(f"Files: {len(os.listdir(OUT)) + len(os.listdir(f'{OUT}/css')) + len(os.listdir(f'{OUT}/js'))}")
