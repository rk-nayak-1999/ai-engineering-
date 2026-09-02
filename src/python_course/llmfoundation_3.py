from openai import OpenAI

client = OpenAI()

prompt = (
    "Give one plausible root cause for an intermittent 502 in a Kubernetes ingress."
)

for temp in (0.0, 0.7, 1.3):
    outs = [
        client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=temp,
            max_tokens=40,
            messages=[{"role": "user", "content": prompt}],
        )
        .choices[0]
        .message.content
        for _ in range(3)
    ]
    print(f"\n--- temperature={temp} ---")
    for o in outs:
        print(" •", o.strip().replace("\n", " ")[:110])
