# Generates preview/a.html (screenshots), b.html (floating icons), c.html (line illustrations)
APPS = [
 dict(id='dayword', name='DayWord', tag='One English word a day, fully offline.', store='App Store', url='https://apps.apple.com/app/id6763968236', c='181,107,73', kind='phone'),
 dict(id='nihongo-manabi', name='Nihongo Manabi', tag="A Japanese tutor that's awake at 3 a.m.", store='App Store', url='https://apps.apple.com/app/id6760352124', c='91,63,181', kind='phone'),
 dict(id='splity', name='Splity', tag='Split bills with friends, no spreadsheet.', store='App Store', url='https://apps.apple.com/app/id6760477233', c='12,183,204', kind='phone'),
 dict(id='mahjong', name='麻將戰績', tag='Score every mahjong game. Know who really wins.', store='App Store', url='https://apps.apple.com/tw/app/id6760577332', c='227,81,11', kind='phone'),
 dict(id='stocktrack', name='處置雷達', tag='Taiwan stock disposition alerts, within 30 minutes.', store='App Store', url='https://apps.apple.com/tw/app/id6802329246', c='224,74,95', kind='phone'),
 dict(id='ai-job-autofill', name='AI Job Autofill', tag='Greenhouse & Lever applications in one click.', store='Chrome', url='https://chromewebstore.google.com/detail/ai-job-autofill/pnmochkacndcpgacmhlhanahgofengaj', c='79,70,229', kind='wide'),
 dict(id='ai-tab-manager', name='AI Tab Manager', tag='Tabs grouped by topic, pages summarized.', store='Chrome', url='https://chromewebstore.google.com/detail/ai-tab-manager/diklcnalgjdinhloiacaooidbmfhojch', c='99,102,241', kind='wide'),
]

# Monoline spot illustrations (stroke = app colour). 48x48 viewBox.
ART = {
 'dayword': '<rect x="8" y="10" width="32" height="28" rx="4"/><path d="M15 30l4-12 3 8 3-8 4 12"/><path d="M14 34h20"/>',
 'nihongo-manabi': '<path d="M10 12h28v18H22l-7 7v-7h-5z"/><path d="M19 19h10M24 17v11M20 25c3 0 6-2 8-5"/>',
 'splity': '<path d="M14 6h20v36l-3-3-3 3-4-3-4 3-3-3-3 3z"/><path d="M19 14h10M19 20h10M19 26h6"/><path d="M12 30l24 8" stroke-dasharray="3 3"/>',
 'mahjong': '<rect x="12" y="6" width="24" height="36" rx="4"/><text x="24" y="31" font-size="18" text-anchor="middle" font-family="-apple-system,PingFang TC,sans-serif" font-weight="600" fill="currentColor" stroke="none">中</text>',
 'stocktrack': '<circle cx="24" cy="24" r="16"/><circle cx="24" cy="24" r="8"/><path d="M24 24L24 8A16 16 0 0 1 38 17z" fill="currentColor" fill-opacity=".18" stroke="none"/><path d="M24 24l14-7"/><circle cx="16" cy="30" r="1.5" fill="currentColor" stroke="none"/>',
 'ai-job-autofill': '<rect x="10" y="6" width="28" height="36" rx="3"/><path d="M16 14h10M16 20h16M16 26h16M16 32h8"/><path d="M28 30l4 4 8-8"/>',
 'ai-tab-manager': '<path d="M6 16h36v22a3 3 0 0 1-3 3H9a3 3 0 0 1-3-3z"/><path d="M6 16v-5a3 3 0 0 1 3-3h8l3 4h6l3-4h8a3 3 0 0 1 3 3v5"/><path d="M14 26h20M14 32h14"/>',
}

HEAD = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Tony — Apps</title>
  <meta name="description" content="Small apps by Tony (arlong): DayWord, Nihongo Manabi, Splity, 麻將戰績, 處置雷達, and two Chrome extensions.">
  <meta name="theme-color" content="#ffffff">
  <link rel="icon" type="image/png" href="favicon.png?v=2">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="canonical" href="https://arlong6.github.io/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Tony — Apps">
  <meta property="og:description" content="Small apps for everyday problems. iOS apps and Chrome extensions by Tony (arlong).">
  <meta property="og:url" content="https://arlong6.github.io/">
  <meta property="og:image" content="https://arlong6.github.io/og.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>
  <main>
'''
FOOT = '''
    <footer>
      <span>Tony Chien</span>
      <a href="https://www.instagram.com/ccl_0120" rel="noopener">Instagram</a>
      <a href="mailto:tony0912045596@gmail.com">Email</a>
    </footer>
  </main>
</body>
</html>
'''
PV_CSS = '.pv{margin:40px 0 0;font-size:13px;color:var(--muted)}.pv a{color:inherit;margin:0 2px}'

def row(a, extra=''):
    return f'''      <li id="{a['id']}" style="--c:{a['c']};--i:{APPS.index(a)+1}"><a href="{a['url']}" rel="noopener">
        <img class="icon" src="icons/{a['id']}.png" alt="" width="56" height="56">
        <span class="text"><b>{a['name']}</b><span>{a['tag']}</span><small>{a['store']}</small></span>
        {extra}
      </a></li>
'''

def page(v, css, hero, rows):
    return HEAD + hero + '    <ul class="apps">\n' + ''.join(rows) + '    </ul>\n' + FOOT

TITLE = '''    <h1>Tony</h1>
    <p class="lede">Small apps for everyday problems.</p>
'''

# ---------- A: real screenshots ----------
CSS_A = '''
.apps a{align-items:center}
.text small{display:none}
.apps a .store{display:none}
.shot{flex:none;width:60px;height:130px;object-fit:cover;object-position:top;border-radius:10px;box-shadow:0 0 0 1px rgba(0,0,0,.08),0 6px 16px -8px rgba(0,0,0,.35);transition:transform .35s var(--ease),box-shadow .35s var(--ease)}
.shot.wide{width:112px;height:70px;border-radius:8px}
.apps a:hover .shot{transform:translateY(-4px) rotate(-1.5deg) scale(1.04);box-shadow:0 0 0 1px rgba(0,0,0,.08),0 18px 30px -12px rgba(var(--c),.6)}
.apps a .text{gap:2px}
.apps a .text small{display:block;font-size:13px;color:rgb(var(--c));margin-top:6px}
@media (min-width:640px){.shot{width:72px;height:156px}.shot.wide{width:136px;height:85px}}
'''
rows_a = [row(a, f'<img class="shot{" wide" if a["kind"]=="wide" else ""}" src="shots/{a["id"]}.jpg" alt="{a["name"]} screenshot" loading="lazy">') for a in APPS]
pass

# ---------- B: floating icons hero (tidy: two staggered rows, uniform size) ----------
ROT = [-4, 3, -2, 4, 3, -3, 2]
DUR = [7, 8, 6.5, 7.5, 8.5, 7, 6]
CSS_B = '''
.hero{display:flex;flex-direction:column;gap:14px;margin:0 0 40px}
.hero .r{display:flex;gap:18px}
.hero .r + .r{padding-left:37px}
.hero a{display:block;width:56px;height:56px;border-radius:22.37%;box-shadow:0 0 0 1px rgba(0,0,0,.06),0 10px 20px -12px rgba(var(--c),.55);animation:float var(--d) ease-in-out var(--dl) infinite;transition:transform .3s var(--ease),box-shadow .3s var(--ease)}
.hero a:hover{animation-play-state:paused;transform:translateY(-4px) scale(1.06)!important;box-shadow:0 0 0 1px rgba(0,0,0,.06),0 16px 28px -12px rgba(var(--c),.7)}
.hero img{display:block;width:100%;height:100%;border-radius:inherit}
@keyframes float{0%,100%{transform:translateY(0) rotate(var(--r))}50%{transform:translateY(-5px) rotate(calc(var(--r) * -0.5))}}
.text small{display:none}
@media (min-width:640px){.hero{gap:18px;margin-bottom:48px}.hero .r{gap:22px}.hero .r + .r{padding-left:43px}.hero a{width:64px;height:64px}}
@media (prefers-reduced-motion:reduce){.hero a{animation:none}}
'''
def hero_link(i, a):
    return f'<a href="#{a["id"]}" style="--c:{a["c"]};--r:{ROT[i]}deg;--d:{DUR[i]}s;--dl:{-i*0.9:.1f}s"><img src="icons/{a["id"]}.png" alt=""></a>'
hero_b = ('    <div class="hero" aria-hidden="true">\n      <div class="r">' + ''.join(hero_link(i,a) for i,a in enumerate(APPS[:4])) +
          '</div>\n      <div class="r">' + ''.join(hero_link(i,a) for i,a in enumerate(APPS) if i>=4) + '</div>\n    </div>\n' + TITLE)
rows_b = [row(a, f'<span class="store">{a["store"]}</span>') for a in APPS]
pass

# ---------- C: line illustrations ----------
CSS_C = '''
.text small{display:none}
.apps a .store{display:none}
.art{flex:none;width:64px;height:64px;color:rgb(var(--c));transition:transform .35s var(--ease)}
.art svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:1.75;stroke-linecap:round;stroke-linejoin:round}
.apps a:hover .art{transform:translateY(-3px) rotate(-4deg)}
.apps a .text small{display:block;font-size:13px;color:rgb(var(--c));margin-top:6px}
@media (min-width:640px){.art{width:76px;height:76px}}
'''
rows_c = [row(a, f'<span class="art" aria-hidden="true"><svg viewBox="0 0 48 48">{ART[a["id"]]}</svg></span>') for a in APPS]
pass

# ---------- D: A + B combined ----------
CSS_D = CSS_B + CSS_A
open('index.html','w').write(page('D', CSS_D, hero_b, rows_a))
css=open('style.css').read().split('/* == generated by build.py == */')[0].rstrip()+'\n\n/* == generated by build.py == */\n'+CSS_D.strip()+'\n'
open('style.css','w').write(css)
print('built index.html')
