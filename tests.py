from shade_privacy import ZKIntentSDK

# Initialize SDK
sdk = ZKIntentSDK(
    api_key="your_api_key",
    hmac_secret="your_hmac_secret"
)

# Create intent
payload = {
    "recipient": "0x742d35Cc6634C0532925a3b844Bc9e90F8886B28",
    "amount": 1.5,
    "token": "ETH",
    "walletType": "eip-155"
}

result = sdk.create_intent(
    payload=payload,
    wallet_signature="0x...",
    metadata={"note": "Test"}
)
