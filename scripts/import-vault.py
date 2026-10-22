"""Import only the declared teaching documents; never modify the Obsidian vault."""
from pathlib import Path
import hashlib,json,re,shutil,posixpath,unicodedata
from urllib.parse import urlsplit,unquote,quote

ROOT=Path(__file__).resolve().parents[1]
site=json.loads((ROOT/'site.json').read_text(encoding='utf-8'))
VAULT=Path(site['vaultRoot']).resolve();SOURCE=ROOT/site['sourceRoot'];BASE=site['baseUrl'].rstrip('/')
declared={}
for track in site['tracks']:
 for chapter in track['chapters']:
  for key in ['course','tp','correction']:
   if key in chapter:declared[(VAULT/chapter[key]).resolve()]=chapter[key]
schemas={}
for p in (VAULT/'ressources/schemas').glob('*.md'):
 stem=p.name.replace('.excalidraw.md','').removesuffix('.md')
 stem=''.join(c for c in unicodedata.normalize('NFKD',stem) if not unicodedata.combining(c))
 schemas[p.resolve()]=re.sub('[^a-z0-9]+','-',stem.lower()).strip('-')+'.svg'
private={p for p in declared if 'correction' in p.name and not re.search(r'(?m)^publier:\s*true\s*$',p.read_text(encoding='utf-8-sig'))}
media=ROOT/'assets/course-media';media.mkdir(exist_ok=True)
def resolve(origin,name):
 name=unquote(name.split('#')[0]).removeprefix('LPI-101-Obsidian/')
 options=[origin.parent/name,origin.parent/(name+'.md'),VAULT/name,VAULT/(name+'.md')]
 for p in options:
  if p.is_file():return p.resolve()
 matches=[p for p in VAULT.rglob('*') if p.is_file() and any(p.as_posix().endswith('/'+s) for s in [name,name+'.md'])]
 assert len(matches)==1,(origin.name,name,matches)
 return matches[0].resolve()
def asset(p):
 assert p.is_relative_to(VAULT),p
 if p in schemas:
  dest=media/schemas[p];assert dest.is_file(),f'Exporter le dessin avant import : {p.name}'
 else:
  assert p.suffix.lower() in ['.png','.jpg','.jpeg','.svg','.gif','.webp'],p
  name=hashlib.sha256(p.read_bytes()).hexdigest()[:16]+p.suffix.lower();dest=media/name
  if not dest.exists():shutil.copyfile(p,dest)
 return BASE+'/assets/course-media/'+dest.name
def convert(text,origin):
 # The template owns course navigation. Teacher-only and historical documents are not published.
 text=re.split(r'(?m)^## (?:Mise en pratique|TP d’origine)\s*$',text)[0]
 lines=[]
 for line in text.splitlines():
  if 'Sommaire]]' in line or 'Tous les TP]]' in line or 'Tous les TP]]' in line:continue
  if re.search(r'^\[(?:Ouvrir la correction|Retour à l’énoncé)\]',line):continue
  lines.append(line)
 text='\n'.join(lines).rstrip()
 text=re.sub(r'(?:\n\s*---\s*)+$','',text)
 def wiki(m):
  embed=bool(m[1]);target,_,label=m[2].partition('|');p=resolve(origin,target)
  if p in private:return ''
  if embed:return '!['+(label or p.stem.replace('.excalidraw',''))+']('+asset(p)+')'
  assert p in declared, f'Document non déclaré : {origin.name} → {target}'
  rel=posixpath.relpath(declared[p],posixpath.dirname(declared[origin]))
  return '['+(label or p.stem)+']('+quote(rel,safe='/')+')'
 text=re.sub(r'(!?)\[\[([^\]]+)\]\]',wiki,text)
 def markdown(m):
  parsed=urlsplit(m[2])
  if parsed.scheme or parsed.netloc or not parsed.path:return m[0]
  if parsed.path.startswith('/assets/') or parsed.path.startswith(BASE):return m[0]
  p=resolve(origin,parsed.path)
  if p in private:return ''
  if m[1].startswith('!'):return m[1]+asset(p)+m[3]
  assert p in declared,(origin,p)
  relative=posixpath.relpath(declared[p],posixpath.dirname(declared[origin]))
  return m[1]+quote(relative,safe='/')+('#'+parsed.fragment if parsed.fragment else '')+m[3]
 text=re.sub(r'(!?\[[^\]]*\]\()([^\s)]+)(\))',markdown,text)
 assert not re.search(r'!?\[\[',text),origin
 return text.strip()+'\n'

fingerprints={}
for p,name in declared.items():
 data=p.read_bytes();fingerprints[name]=hashlib.sha256(data).hexdigest()
 text=convert(data.decode('utf-8-sig'),p);target=SOURCE/name;target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(text,encoding='utf-8')
 assert hashlib.sha256(p.read_bytes()).hexdigest()==fingerprints[name]
(ROOT/'.quartz-cache').mkdir(exist_ok=True)
(ROOT/'.quartz-cache/import-manifest.json').write_text(json.dumps({'documents':len(declared),'sourceSha256':fingerprints,'privateCorrections':len(private),'drawings':list(schemas.values())},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Import : {len(declared)} documents déclarés ; {len(private)} corrections privées conservées hors publication ; coffre inchangé.')
