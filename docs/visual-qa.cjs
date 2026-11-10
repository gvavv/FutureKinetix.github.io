const {chromium}=require('playwright');
const fs=require('fs');
(async()=>{const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});const findings=[];
for(const pageName of ['index','yarbo']) for(const width of [320,375,430,768,1024,1440,1920]){
 const page=await browser.newPage({viewport:{width,height:1000},deviceScaleFactor:1});const errors=[];page.on('pageerror',e=>errors.push(e.message)); await page.goto('http://127.0.0.1:4173/'+pageName+'.html');await page.evaluate(()=>document.fonts.ready);await page.locator('img').evaluateAll(imgs=>Promise.all(imgs.map(i=>{i.loading='eager';return i.decode().catch(()=>{})})));
 const result=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,broken:[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src),outside:[...document.querySelectorAll('h1,h2,h3,.button,img')].filter(e=>{let r=e.getBoundingClientRect();return r.left<-.5||r.right>innerWidth+.5}).map(e=>e.outerHTML.slice(0,140))}));
 await page.screenshot({path:'docs/qa/'+pageName+'-'+width+'.png',fullPage:true});findings.push({page:pageName,width,...result,errors});await page.close();}
fs.writeFileSync('docs/qa/results.json',JSON.stringify(findings,null,2));console.log(JSON.stringify(findings,null,2));await browser.close();})();
