import argparse
import asyncio
import os
import re
from pathlib import Path

from backboard import BackboardClient


def clean_filename(topic):
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", topic.lower()).strip("-")
    return f"study-pack-{slug}.md"


async def ask(client, thread_id, prompt):
    response = await client.send_message(
        prompt,
        thread_id=thread_id,
        stream=False
    )

    if getattr(response, "status", None) == "FAILED":
        raise RuntimeError(response.content)

    return response.content, response.thread_id


async def generate_study_pack(topic):

    api_key = os.getenv("BACKBOARD_API_KEY")

    if not api_key:
        raise RuntimeError(
            "BACKBOARD_API_KEY is not set."
        )

    client = BackboardClient(api_key=api_key)

    print(f"\nGenerating Java study pack for: {topic}\n")

    # =========================
    # STEP 1 - EXPLAIN
    # =========================

    print("1/5 Explain...")

    explanation, thread_id = await ask(
        client,
        None,
        f"""
You are a Java teacher for beginners.

Topic: {topic}

Explain this Java topic in a beginner-friendly way.

Include:
- What it is
- Why it is used
- Important concepts
- Basic syntax
- Common mistakes
- A simple real-world analogy

Use Markdown.

Do not create practice questions or a quiz yet.
"""
    )

    # =========================
    # STEP 2 - EXAMPLES
    # =========================

    print("2/5 Examples...")

    examples, thread_id = await ask(
        client,
        thread_id,
        f"""
Create 3 Java code examples for:

{topic}

Requirements:

Example 1:
Very easy beginner example.

Example 2:
Medium difficulty.

Example 3:
More challenging practical example.

Use complete Java programs where possible.

Explain each example briefly.

Put Java code inside:

```java
code here
