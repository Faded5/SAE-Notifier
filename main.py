import time
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1569401475644260432/k23jyaXkdDW_XAFoFJToVrsDNvopJdQ2qiSld43_j6gO3IFszx5dChdbFJP9nI6yqD9E"

ROLE_IDS = {
    "Secret": "1569375865249206313",
    "Eternal": "1569376122536206377",
    "Divine": "1569376262802120756"
}

def trigger_instant_alert(egg_name, rarity, biome, server_link=""):
    """Fired IMMEDIATELY when a spawn packet/signal is received."""
    if rarity not in ROLE_IDS:
        return

    role_mention = f"<@&{ROLE_IDS[rarity]}>"
    color_map = {"Secret": 10181046, "Eternal": 15105570, "Divine": 16766720}

    payload = {
        "content": f"🚨 {role_mention} **A {rarity.upper()} EGG SPAWNED RIGHT NOW!**",
        "embeds": [
            {
                "title": f"🥚 Live Spawn: {egg_name}",
                "color": color_map.get(rarity, 3447003),
                "fields": [
                    {"name": "Rarity", "value": rarity, "inline": True},
                    {"name": "Biome", "value": biome, "inline": True},
                    {"name": "Server Link", "value": f"[Click to Join]({server_link})" if server_link else "Check Server List", "inline": False}
                ],
                "footer": {"text": "Real-Time Egg Notifier"}
            }
        ]
    }

    requests.post(WEBHOOK_URL, json=payload)

def main():
    print("Real-time listener started. Waiting for spawn events...")
    
    # Continuous high-frequency check loop (e.g., polling every 1-2 seconds or listening to a WebSocket)
    while True:
        try:
            # --- INSERT LIVE DATA SOURCE OR WEBSOCKET RECEIVER HERE ---
            # e.g., if live_data_received:
            #     trigger_instant_alert(data.egg, data.rarity, data.biome)
            
            time.sleep(1) # Fast 1-second check interval for real-time responsiveness
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
