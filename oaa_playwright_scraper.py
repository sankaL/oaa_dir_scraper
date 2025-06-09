import asyncio
import csv
from playwright.async_api import async_playwright

async def scrape_page(page, page_num):
    url = f"https://oaa.on.ca/oaa-directory/search-practices?page={page_num}"
    await page.goto(url)
    await page.wait_for_selector('div.row-fluid.row.mobileMargin')
    practice_divs = await page.query_selector_all('div.row-fluid.row.mobileMargin')
    results = []
    for div in practice_divs:
        try:
            # Practice name
            name_elem = await div.query_selector('h4 > a')
            name = (await name_elem.inner_text()).strip() if name_elem else ""
            # All <p> tags in the third .span-12
            p_tags = await div.query_selector_all('div.span-12 p')
            address = (await p_tags[0].inner_text()).strip() if len(p_tags) > 0 else ""
            phone = (await p_tags[1].inner_text()).replace("Phone:", "").strip() if len(p_tags) > 1 else ""
            email = ""
            if len(p_tags) > 2:
                # Email is in the form: "Email: email@domain.com" or "Email: <a href=...>email@domain.com</a>"
                email_elem = await p_tags[2].query_selector('a')
                if email_elem:
                    email = (await email_elem.inner_text()).strip()
                else:
                    email = (await p_tags[2].inner_text()).replace("Email:", "").strip()
            results.append([name, address, phone, email])
        except Exception as e:
            print(f"Error scraping a practice: {e}")
            continue
    return results

async def main():
    start_page = int(input("Enter start page: "))
    end_page = int(input("Enter end page: "))
    output_file = "oaa_contacts.csv"
    header = ['practice name', 'address', 'phone number', 'e-mail']
    # Write header only once
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        for page_num in range(start_page, end_page + 1):
            print(f"Scraping page {page_num}...")
            results = await scrape_page(page, page_num)
            with open(output_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(results)
            print(f"Page {page_num}: {len(results)} practices scraped.")
        await browser.close()
    print(f"\nScraping completed. Results saved to {output_file}")

if __name__ == "__main__":
    asyncio.run(main()) 