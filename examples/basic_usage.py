from walamail import WalaMailClient
import sys
import os

# Add parent directory to path so we can import walamail
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    # Replace with your actual API token from the dashboard
    API_TOKEN = "your_api_token_here"
    
    # Initialize client (default base_url is https://walamail.com)
    client = WalaMailClient(API_TOKEN)
    
    try:
        # 1. Check Balance
        print("--- Checking Balance ---")
        balance_info = client.get_balance()
        print(f"Current Balance: ${balance_info['balance']}")
        
        # 2. Check Stock
        print("\n--- Checking Stock ---")
        stock = client.get_stock()
        for item in stock:
            print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']} | Stock: {item['stock']}")
            
        # 3. Purchase Example (Uncomment to use)
        # if stock:
        #     first_product_id = stock[0]['id']
        #     print(f"\n--- Purchasing 1 unit of Product ID {first_product_id} ---")
        #     order = client.purchase(first_product_id, 1)
        #     print(f"Purchase Successful! Trade No: {order['tradeNo']}")
        #     print("Credentials:")
        #     for cred in order['credentials']:
        #         print(f"  {cred}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
