from playwright.sync_api import sync_playwright
from datetime import datetime
import pandas as pd

def scrape_youtube_charts(artist_name: str, country: str, timeframe: str) -> pd.DataFrame:
    """
    Scrape daily view data for an artist from YouTube Charts for a specific country.
    
    Args:
        artist_name (str): Name of the artist to search for
        country (str): Country to get the stats from
        
    Returns:
        pd.DataFrame: DataFrame containing daily view counts
    """
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        try:
            # Navigate to YouTube Charts
            page.goto('https://charts.youtube.com/')
            page.wait_for_load_state('networkidle')
            
            # Search for artist
            search_box = page.locator('#search-native')
            search_box.fill(artist_name)
            page.wait_for_timeout(1000)  # Wait for search results

            # Click on artist result
            page.get_by_role('option', name=artist_name).click()
            page.wait_for_load_state('networkidle')

            # Select country
            country_selector = page.locator('#search-box-and-selector #search-native')
            country_selector.click()
            country_selector.fill(country)
            
            # Wait for and select the country option
            country_option = page.get_by_role('option', name=country, exact=True)
            country_option.click()
            page.wait_for_load_state('networkidle')

            # Select timeframe from the dropdown
            timeframe_button = page.get_by_role('button', name='Last 28 days')
            timeframe_button.click()
            timeframe_option = page.get_by_role('option', name=timeframe, exact=True)
            timeframe_option.click()
            page.wait_for_load_state('networkidle')
            page.wait_for_timeout(1000)  # Wait for data to load
            
            # Extract data from the table
            rows = page.locator('table tbody tr').all()
            data = []
            
            for row in rows:
                cells = row.locator('td').all()
                if len(cells) == 2:  # Ensure we have both date and views
                    date = cells[0].inner_text()
                    views = int(cells[1].inner_text().replace(',', ''))
                    data.append({'date': date, 'views': views})
            
            # Create DataFrame
            df = pd.DataFrame(data)
            df['date'] = pd.to_datetime(df['date'])
            df = df.sort_values('date')
            
            return df

        finally:
            browser.close()

def save_to_csv(df: pd.DataFrame, artist: str, country: str, timeframe: str):
    """Save the data to a CSV file with timestamp."""
    report_date = datetime.now().strftime('%Y-%m-%d')
    filename = f"{artist.lower().replace(' ', '_')}_{country.lower()}_{timeframe.lower().replace(' ', '_')}_{report_date}.csv"
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    # Example usage
    artist = "Conan Gray"
    country = "Thailand"
    timeframe = "Last 7 days"
    
    try:
        df = scrape_youtube_charts(artist, country, timeframe)
        print(f"\nDaily views for {artist} in {country}:")
        
        # Save to CSV
        save_to_csv(df, artist, country, timeframe)
        
        # Print some analytics
        print(f"\nAnalytics: {timeframe}")
        print(f"Total views: {df['views'].sum():,}")
        print(f"Peak views: {df['views'].max():,} on {df['date'][df['views'].idxmax()].strftime('%B %d, %Y')}")
        print(f"Lowest views: {df['views'].min():,} on {df['date'][df['views'].idxmin()].strftime('%B %d, %Y')}")
        print(f"Average daily views: {df['views'].mean():,.0f}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
