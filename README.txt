# OLX Automation Bot

This is an automation script that navigates through the OLX website, browsing all available pages and visiting each ad.  
For every ad, it checks whether the user is blocked. If the user is blocked, the bot skips the ad. Otherwise, it sends a personalized message on behalf of the user.

---

## ⚙️ How to Use

To use this automation, you should pay attention to two key components:

### 1. `Main.py`

This is the main script you need to run in order to start the automation.

### 2. `data.json`

This file is consumed by the bot and is essential for the process. Each attribute has a specific purpose:

- **`Ad_List`** `[LIST OF STRINGS]`:  
  Stores all the ads that the bot has already visited.  
  This prevents the bot from messaging the same user more than once.  
  If you want to resend a message to a specific ad, simply delete the corresponding link from the list.

- **`Last_execution`** `[STRING]`:  
  Records the last time the bot was executed.

- **`products`** `[LIST OF DICTIONARIES]`:  
  Each dictionary stores a product name as the key and the OLX search URL as the value.  
  The product name helps to avoid sending messages to similar but incorrect products.  
  _Example: “Musical keyboard” is different from “computer keyboard”._

- **`message`**:  
  This is where you define the message that will be sent to the final user.

---

## 💡 Example `data.json`

```json
{
  "Ad_List": ["https://www.olx.com/ad123", "https://www.olx.com/ad456"],
  "Last_execution": "2025-08-06T15:30:00",
  "products": [
    {
      "Musical Keyboard": "https://www.olx.com/search?query=musical+keyboard"
    }
  ],
  "message": "Hi! I'm interested in your product. Is it still available?"
}
