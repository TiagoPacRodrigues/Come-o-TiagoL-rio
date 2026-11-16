// Abre uma página no Chromium, salva prints (tela e página inteira) e imprime um JSON
// com título, H1, contagem de imagens e o texto visível.
// Uso: NODE_PATH=$(npm root -g) node scripts/print_pagina.js <url> <prefixo-saida> [celular]
const { chromium } = require('playwright');
const [,, url, out, mobile] = process.argv;
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium', proxy: process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined, args: ['--no-sandbox'] });
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, locale: 'pt-BR' }
    : { viewport: { width: 1366, height: 900 }, locale: 'pt-BR' });
  const p = await ctx.newPage();
  const resp = await p.goto(url, { waitUntil: 'load', timeout: 60000 });
  await p.waitForTimeout(3000);
  await p.screenshot({ path: out + '.png' });
  await p.screenshot({ path: out + '-full.png', fullPage: true }).catch(() => {});
  const info = await p.evaluate(() => ({
    title: document.title,
    h1: [...document.querySelectorAll('h1')].map(h => h.innerText.trim()),
    imgs: document.images.length,
    imgsNoAlt: [...document.images].filter(i => !i.alt).length,
    text: document.body.innerText,
  }));
  console.log(JSON.stringify({ status: resp && resp.status(), ...info }));
  await b.close();
})();
