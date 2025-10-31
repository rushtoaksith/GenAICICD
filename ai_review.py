# ai_review.py
import openai, os, sys

def main():
    openai.api_key = ${{ secrets.OPENAI_API_KEY }}
    diff_file = sys.argv[1] if len(sys.argv) > 1 else "diff.txt"

    with open(diff_file, "r") as f:
        diff = f.read()

    prompt = f"""You are a senior software engineer AI.
Review this git diff and identify:
1. Possible bugs
2. Security risks
3. Missing tests
4. Code improvement suggestions
---
{diff}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=600
    )

    feedback = response["choices"][0]["message"]["content"]
    print("===== GENAI REVIEW START =====")
    print(feedback)
    print("===== GENAI REVIEW END =====")

if __name__ == "__main__":
    main()

