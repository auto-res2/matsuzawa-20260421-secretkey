import os
from anthropic import Anthropic


def main():
    if not (api_key := os.getenv("ANTHROPIC_API_KEY")):
        print("❌ ANTHROPIC_API_KEY が設定されていません")
        return

    print("✅ ANTHROPIC_API_KEY を検出しました。")

    try:
        client = Anthropic(api_key=api_key)

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            messages=[
                {"role": "user", "content": "自己紹介をしてください。"}
            ],
        )

        print("✅ API呼び出し成功:")
        print(response.content[0].text)

    except Exception as e:
        print("❌ API呼び出しに失敗しました")
        print(e)


if __name__ == "__main__":
    main()
