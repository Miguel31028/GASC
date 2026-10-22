// Gera os mockups em HTML (pasta html/) e em PNG (pasta png/).
// Uso: node gerar.mjs   (requer os pacotes "playwright" e "qrcode")
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import QRCode from 'qrcode';
import { chromium } from 'playwright';
import { ecrasA } from './ecras_gestao.mjs';
import { ecrasB, painelWeb, pdfRgdhsa } from './ecras_operacao.mjs';

const dir = path.dirname(fileURLToPath(import.meta.url));
const qrSvg = async t => (await QRCode.toString(t, { type: 'svg', margin: 0, errorCorrectionLevel: 'M' }))
  .replace('<svg ', '<svg width="100%" height="100%" ');
const q = {
  local: `<div style="width:96px;height:96px">${await qrSvg('GASC:LOCAL:004-01-02')}</div>`,
  pessoa: await qrSvg('GASC:QR:7f3c9a1e5b2d48c6a0e4f19b2c7d8e31'),
  utente: await qrSvg('GASC:QR:2b8e4d6f0a1c39e7b5d2f84a6c1e9b07'),
};
const ecras = [...ecrasA(q), ...ecrasB(q), painelWeb(), pdfRgdhsa()];

const page = (e, body) => `<!doctype html><html lang="pt"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>${e.id} – ${e.titulo}</title>
<link rel="stylesheet" href="../mockups.css"></head><body style="padding:16px;background:#fff">${body}</body></html>`;

fs.mkdirSync(path.join(dir, 'html'), { recursive: true });
fs.mkdirSync(path.join(dir, 'png'), { recursive: true });
for (const e of ecras) fs.writeFileSync(path.join(dir, 'html', `${e.id}.html`), page(e, e.html));

// galeria com todos os ecrãs pela ordem funcional
let grupo = '';
let gal = '';
for (const e of ecras) {
  if (e.grupo !== grupo) { gal += `${grupo ? '</div>' : ''}<h2 style="font:500 20px Roboto;margin:28px 0 12px">${e.grupo}</h2><div style="display:flex;flex-wrap:wrap;gap:24px">`; grupo = e.grupo; }
  gal += `<figure style="margin:0"><a href="html/${e.id}.html"><img src="png/${e.id}.png" style="width:${e.wide ? 640 : 260}px;border-radius:12px"></a><figcaption style="font:13px Roboto;margin-top:6px"><b>${e.id}</b> · ${e.titulo}</figcaption></figure>`;
}
fs.writeFileSync(path.join(dir, 'index.html'), `<!doctype html><html lang="pt"><head><meta charset="utf-8"><title>Mockups GASC</title>
<link rel="stylesheet" href="mockups.css"></head><body style="padding:24px 32px"><h1 style="font:500 26px Roboto">Mockups – Sistema de Gestão do Espaço Social (GASC)</h1>${gal}</div></body></html>`);

const browser = await chromium.launch();
const ctx = await browser.newContext({ deviceScaleFactor: 2.5, viewport: { width: 1400, height: 1000 } });
const pg = await ctx.newPage();
for (const e of ecras) {
  await pg.goto('file://' + path.join(dir, 'html', `${e.id}.html`));
  await pg.evaluate(() => document.fonts.ready);
  await pg.waitForTimeout(150);
  const el = await pg.$(e.wide ? '.wide, .a4' : '.screen');
  await el.screenshot({ path: path.join(dir, 'png', `${e.id}.png`) });
}
await browser.close();
fs.writeFileSync(path.join(dir, 'ecras.json'), JSON.stringify(ecras.map(({ id, grupo, titulo }) => ({ id, grupo, titulo })), null, 2));
console.log(`${ecras.length} ecrãs gerados`);
