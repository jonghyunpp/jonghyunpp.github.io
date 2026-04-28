import yfinance as yf
import json
import os

def fetch_market_data():
    indices = {
        "^KS11": "KOSPI",
        "^KQ11": "KOSDAQ",
        "^IXIC": "NASDAQ",
        "^GSPC": "S&P 500"
    }
    
    result = []
    
    for symbol, name in indices.items():
        try:
            ticker = yf.Ticker(symbol)
            # Use fast_info or history to get the latest price and change
            hist = ticker.history(period="2d")
            if len(hist) >= 2:
                latest_close = hist['Close'].iloc[-1]
                prev_close = hist['Close'].iloc[-2]
                change_val = latest_close - prev_close
                change_pct = (change_val / prev_close) * 100
                
                direction = "flat"
                if change_val > 0:
                    direction = "up"
                elif change_val < 0:
                    direction = "down"
                
                result.append({
                    "name": name,
                    "value": f"{latest_close:,.2f}",
                    "change": f"{'+' if change_val > 0 else ''}{change_pct:.2f}%",
                    "dir": direction
                })
        except Exception as e:
            print(f"Error fetching {name}: {e}")
            
    if result:
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        with open("data/market.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print("Market data updated successfully.")

if __name__ == "__main__":
    fetch_market_data()
