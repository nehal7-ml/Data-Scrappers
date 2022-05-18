
const scraperObject = {
	// put url to scrape, reteives HTML data
  url:
   'https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1311&_nkw=guitar+effects+pedals&_sacat=3858&LH_TitleDesc=0&_odkw=guitar+pedals&_osacat=3858.com/',
	
    async scraper(browser){
		let page = await browser.newPage();
		console.log(`Navigating to ${this.url}...`);        
		await page.goto(this.url);
    const data = await page.evaluate(( ) => {            
            const list = []
            //Nodelist of results
            const items =  document.querySelectorAll("ul.srp-results li")
            
            // find number of results per page
            const results_per_page= parseInt(document.querySelector('ul.srp-results span.expand-btn__cell').textContent)
            
            //items.slice(60);
            for (let i=0; i<results_per_page; i++) {
                
               //console.log(items[i].querySelector(".s-item__title").textContent)

                list.push({
                
                    Product_name: items[i].querySelector(".s-item__title").textContent,
                    Price: items[i].querySelector(".s-item__price").textContent
                   //pastage: "https://remoteok.io" + item.getAttribute("data-href"),
                 })                
              } 
            return list
            //return ....something...
          });    
		console.log(data)
    await browser.close();
	}
}

module.exports = scraperObject;
