# StockPulse Alert

StockPulse Alert is a Python-based application that monitors stock price fluctuations and sends SMS alerts when significant changes occur. It also provides the latest news related to the company to keep you informed about the reasons behind the stock movement.

## Features
- **Stock Price Analysis**: Detects percentage changes in stock prices using the Alpha Vantage API.
- **News Fetching**: Retrieves the latest news articles related to the company using the News API.
- **SMS Notifications**: Sends alerts directly to your phone via Twilio, including price change details and relevant news.

## Requirements
- Python 3.8 or higher
- Virtual environment (recommended)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hyplv/StockPulse-Alert.git
   cd StockPulse-Alert
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install twilio , requests
   ```

## Configuration
1. Obtain API keys from:
   - [Alpha Vantage](https://www.alphavantage.co/)
   - [News API](https://newsapi.org/)
   - [Twilio](https://www.twilio.com/)


   ```

## Usage
Run the script to monitor stock prices and receive alerts
```
fill the api keys and variables in main function
```
```bash
python main.py
```

## Example Output
- SMS Alert:
  ```
  TSLA: 🔻6.50%
  
  Headline: Tesla's latest breakthrough in battery technology
  Brief: Tesla has announced a revolutionary new battery design...

  Headline: EV market heats up as Tesla faces competition
  Brief: New electric vehicles from competitors are creating...
  ```

## .gitignore
Ensure your sensitive data (like `.env` and `venv` folders) is excluded from version control. Add the following to your `.gitignore`:
```gitignore
.env
venv/
__pycache__/
*.pyc
```

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

