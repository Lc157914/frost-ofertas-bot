import os
import time
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN não configurado.")

if not CHANNEL:
    raise RuntimeError("TELEGRAM_CHANNEL não configurado.")


def telegram(method, data):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"

    response = requests.post(
        url,
        json=data,
        timeout=30
    )

    response.raise_for_status()

    result = response.json()

    if not result.get("ok"):
        raise RuntimeError(result)

    return result


def publicar_oferta():
    texto = """🔥 OFERTA TESTE — FROST OFERTAS

🎧 Headset Gamer RGB

💰 Por: R$ 89,90
🏷️ CUPOM: 10% OFF

⚡ Oferta sujeita a alteração de preço.

👇 PEGAR OFERTA
"""

    teclado = {
        "inline_keyboard": [
            [
                {
                    "text": "🛒 COMPRAR AGORA",
                    "url": "https://example.com"
                }
            ]
        ]
    }

    telegram(
        "sendMessage",
        {
            "chat_id": CHANNEL,
            "text": texto,
            "reply_markup": teclado
        }
    )


def testar_bot():
    resultado = telegram("getMe", {})
    bot = resultado["result"]

    print("Bot conectado:")
    print("Nome:", bot.get("first_name"))
    print("Username:", bot.get("username"))

    publicar_oferta()

    print("Oferta de teste enviada para o canal.")


if __name__ == "__main__":
    testar_bot()

    while True:
        time.sleep(3600)
