import { readFile, readdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import sharp from 'sharp';
const root=fileURLToPath(new URL('../assets/course-media/',import.meta.url));
let count=0;
for(const name of await readdir(root)){
 if(!name.endsWith('.svg'))continue;
 const input=path.join(root,name), svg=await readFile(input,'utf8');
 if(!svg.includes('REPÈRE VISUEL'))continue;
 await sharp(input).resize({width:2000}).png().toFile(input.replace(/\.svg$/,'.png'));count++;
}
console.log(`Schémas : ${count} rendus pour le PDF ; SVG conservés pour le site.`);
