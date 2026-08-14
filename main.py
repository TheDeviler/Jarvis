import ollama
import json
from pathlib import Path

new = 1
row = 0
oldconversation = [] 

CONV_DIR = Path("conversation")
CONV_DIR.mkdir(exist_ok=True)
CONV_FILE = CONV_DIR / "conversation.json"

def load_conversation():
    if not CONV_FILE.exists():
        return []
    try:
        raw = json.loads(CONV_FILE.read_text(encoding="utf-8"))
        msgs = []
        for item in raw:
            role = item.get("role", "user")
            content = item.get("message") or item.get("content")
            if content:
                msgs.append({"role": role, "content": content})
        return msgs
    except Exception:
        return []

def save_conversation(data):
    with CONV_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

conversation = load_conversation()

while True:
      question = input("ask anything>> ");
      if question == "esci":
          save_conversation(oldconversation)
          break;
      response = ollama.chat(model='qwen2.5:3b', messages=[
          {
            'role': 'user',
            'content': question,
          },
        ])
      oldresponse = response['message']['content']
      print(response['message']['content'])
      oldconversation.append({"role": "user", "content": question, "message": oldresponse})

  
  

