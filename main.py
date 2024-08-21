import asyncio
import os

from nordvpn_switcher import initialize_VPN, rotate_VPN
from playwright.async_api import async_playwright

GOOGLE_SEARCH_URL = os.getenv("GOOGLE_SEARCH_URL"),
GOOGLE_SEARCH_TITLE_TEXT = os.getenv("GOOGLE_SEARCH_TITLE_TEXT")


async def custom_goto(page, url, wait_until="domcontentloaded"):
    await page.goto(url, wait_until=wait_until)


async def google_search_visit() -> None:
    async with async_playwright() as playwright:
        initialize_VPN(save=1, area_input=['europe'])

        for _ in range(2):
            rotate_VPN()

            browser = await playwright.chromium.launch_persistent_context(
                user_data_dir="user_data",
                headless=False,
                viewport={"width": 1280, "height": 720}
            )
            page = await browser.new_page()

            await custom_goto(
                page,
                GOOGLE_SEARCH_URL
            )

            await page.get_by_text(
                GOOGLE_SEARCH_TITLE_TEXT
            ).first.click()

            await page.wait_for_timeout(5000)

            await browser.close()


async def main() -> None:
    await google_search_visit()


asyncio.run(main())
