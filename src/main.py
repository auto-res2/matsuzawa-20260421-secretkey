import os
from openai import OpenAI


def main():
    if not (api_key := os.getenv("OPENAI_API_KEY")):
        print("❌ OPENAI_API_KEY が設定されていません")
        return

    print("✅ OPENAI_API_KEY を検出しました。")

    try:
        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-4.1-nano",
            input="自己紹介をしてください。"
        )

        print("✅ API呼び出し成功:")
        print(response.output[0].content[0].text)

    except Exception as e:
        print("❌ API呼び出しに失敗しました")
        print(e)


if __name__ == "__main__":
    main()
