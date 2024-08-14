# TradeWiz Bot

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/djd39448/Tradewiz.git
   cd Tradewiz
   ```
2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions
1. Open the `bot.py` file and add your private key using the `add_private_key` method.
2. Use the `check_rug_pull` method to assess the potential of a token.
3. Automate trades using the `automate_trade` method.

## Example
```python
bot = TradeWizBot()
bot.add_private_key("your_user_id", "your_private_key")
bot.check_rug_pull("token_address")
bot.automate_trade("your_user_id", "token_address", amount)
```
