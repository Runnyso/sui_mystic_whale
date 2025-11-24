import requests, time

def mystic_whales():
    print("Sui — Mystic Whale Oracle (moves that break the matrix)")
    seen = set()
    while True:
        r = requests.get("https://suivision.xyz/api/v1/transactions?limit=40&order=desc")
        for tx in r.json().get("data", []):
            h = tx["txHash"]
            if h in seen: continue
            seen.add(h)
            if tx.get("kind") != "TransferObject": continue
            amount = tx.get("amount", 0) / 1e9
            if amount > 500_000:  # >500k SUI (~$1M+)
                print(f"THE MATRIX JUST GLITCHED\n"
                      f"Whale moved {amount:,.0f} SUI\n"
                      f"From: {tx['sender'][:12]}...\n"
                      f"To:   {tx['recipient'][:12]}...\n"
                      f"Hash: {h}\n"
                      f"https://suivision.xyz/txblock/{tx['txDigest']}\n"
                      f"→ Reality is bending. Sui feels it.\n"
                      f"→ This is not a transfer. This is a prophecy.\n"
                      f"{'▫️▪️▫️▪️'*20}\n")
        time.sleep(2.4)

if __name__ == "__main__":
    mystic_whales()
