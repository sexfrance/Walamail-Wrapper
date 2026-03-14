import requests
from typing import List, Dict, Any, Optional

class WalaMailClient:
    """
    WalaMail API Wrapper for Python.
    """
    
    def __init__(self, api_token: str, base_url: str = "https://walamail.com"):
        self.api_token = api_token
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

    def _request(self, method: str, endpoint: str, data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, json=data, params=params, headers=self.headers)
        
        try:
            res_json = response.json()
        except ValueError:
            response.raise_for_status()
            return {}

        if not response.ok:
            error_msg = res_json.get('error', response.reason)
            raise Exception(f"API Error ({response.status_code}): {error_msg}")
            
        return res_json

    def get_balance(self) -> Dict[str, Any]:
        """Get your current balance and transaction history."""
        return self._request("GET", "/api/user/balance")

    def get_stock(self) -> List[Dict[str, Any]]:
        """List available products and their stock levels."""
        res = self._request("GET", "/api/v1/stock")
        return res.get('data', [])

    def purchase(self, product_id: int, quantity: int, format: str = "oauth", delimiter: str = "|") -> Dict[str, Any]:
        """
        Purchase accounts.
        
        Args:
            product_id: The ID of the product to buy.
            quantity: Number of accounts.
            format: 'oauth' (email|pass|token|id) or 'standard' (email|pass).
            delimiter: '|', ':', or '-'.
        """
        data = {
            "productId": product_id,
            "quantity": quantity,
            "format": format,
            "delimiter": delimiter
        }
        res = self._request("POST", "/api/shop/purchase", data=data)
        return res.get('data', {})

    def get_accounts(self, page: int = 1, limit: int = 50) -> Dict[str, Any]:
        """List your purchased accounts with pagination."""
        params = {"page": page, "limit": limit}
        res = self._request("GET", "/api/v1/accounts", params=params)
        return res.get('data', {})

    def get_account_details(self, account_id: str) -> Dict[str, Any]:
        """Get full details and Graph API instructions for a specific account."""
        data = {"accountId": account_id}
        res = self._request("POST", "/api/v1/accounts", data=data)
        return res.get('data', {})

    def list_mail_accounts(self) -> List[Dict[str, Any]]:
        """List all your purchased accounts via the mail proxy endpoint."""
        res = self._request("GET", "/api/v1/mail")
        return res.get('data', {}).get('accounts', [])
