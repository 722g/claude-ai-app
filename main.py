import anthropic

client = anthropic.Anthropic(api_key="YOUR_API_KEY_HERE")

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": input("Ask Claude anything: ")}
    ]
)

print(message.content[0].text)
