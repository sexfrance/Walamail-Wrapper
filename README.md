# WalaMail API Wrapper

A professional Python client library for interacting with the WalaMail API. This wrapper allows you to automate account management, check balances, and handle bulk purchases with custom formatting.

---

## 🚀 Installation

You can install the wrapper directly using pip:

```bash
pip install walamail
```

*Note: Requires `requests` library (handled automatically by pip).*

---

## 🔑 Authentication

Access requires an **API Token**. You can generate or retrieve your token from the WalaMail Dashboard under **User Settings > API Keys**.

All requests are authenticated via the `Authorization: Bearer <token>` header, which the client handles automatically.

---

## 📖 Quick Start

```python
from walamail import WalaMailClient

# 1. Initialize the client
client = WalaMailClient(api_token="your_api_token", base_url="http://localhost:3000")

# 2. Check your balance
balance_info = client.get_balance()
print(f"💰 Balance: ${balance_info['balance']}")

# 3. Check what's in stock
stock = client.get_stock()
for item in stock:
    print(f"📦 {item['name']} - Price: ${item['price']} - Available: {item['stock']}")
```

---

## 🛠️ Detailed Method Reference

### `WalaMailClient(api_token, base_url="http://localhost:3000")`
Constructs the API client.
- `api_token` (str): Your secret API key.
- `base_url` (str): The root URL of your WalaMail deployment.

---

### `get_balance()`
Returns current user financial state.
*   **Returns**: `{"balance": float, "transactions": [...]}`
*   **Use Case**: Monitoring credit before running large automation batches.

---

### `get_stock()`
Lists all active products and their real-time inventory levels.
*   **Returns**: `List[{"id": int, "name": str, "price": float, "stock": int, ...}]`
*   **Use Case**: Checking if Microsoft/Outlook accounts are available before attempting a purchase.

---

### `purchase(product_id, quantity, format="oauth", delimiter="|")`
Bulk purchase accounts with customizable output format.
*   **Arguments**:
    *   `product_id` (int): The numeric ID of the product.
    *   `quantity` (int): Number of accounts to buy.
    *   `format` (str): 
        *   `oauth`: Full credentials including Refresh Token and Client ID (default).
        *   `standard`: Only `email|password`.
    *   `delimiter` (str): Delimiter character. Options: `|`, `:`, `-`.
*   **Returns**: 
    ```json
    {
      "tradeNo": "WM...",
      "quantity": 5,
      "totalAmount": 0.05,
      "credentials": [
        "email|pass|token|id",
        "email|pass|token|id"
      ]
    }
    ```

---

### `get_accounts(page=1, limit=50)`
Retrieves your order history and previously purchased accounts.
*   **Returns**: Paginated list of account records including emails and associated order IDs.

---

### `get_account_details(account_id)`
Get technical details for a specific account, including direct instructions for Microsoft Graph API integration.
*   **Returns**: Configuration object for the specific account.

---

### `list_mail_accounts()`
Helper specifically for the Mail Proxy system. Returns a list of accounts that can be used with the mailbox reading endpoints.

---

## 🧪 Advanced Example: Automated Purchase Flow

```python
from walamail import WalaMailClient

client = WalaMailClient("YOUR_TOKEN")

# Find a specific product (e.g., 'Trusted Outlook')
stock = client.get_stock()
target_product = next((p for p in stock if "Trusted" in p["name"]), None)

if target_product and target_product["stock"] >= 5:
    # Buy 5 accounts in standard format using colon separator
    order = client.purchase(
        product_id=target_product["id"],
        quantity=5,
        format="standard",
        delimiter=":"
    )
    
    print(f"Order {order['tradeNo']} completed!")
    for account_line in order['credentials']:
        email, password = account_line.split(":")
        print(f"Purchased: {email}")
else:
    print("Stock insufficient or product not found.")
```

## ⚠️ Error Handling

The wrapper raises exceptions for API errors (4xx/5xx). It is recommended to wrap calls in try-except blocks.

```python
try:
    client.get_balance()
except Exception as e:
    print(f"Request failed: {e}")
```
