import tkinter as tk
import json
import urllib.request
import re

def get_owner_info():
    repo_url = "https://github.com/elastic/elasticsearch"
    repo_url = repo_url.strip()
    owner = re.search(r"github\.com/([^/]+)", repo_url).group(1)
    
    with urllib.request.urlopen(f"https://api.github.com/users/{owner}") as r:
        data = json.load(r)
    
    result = {
        'company': data.get('company'),
        'created_at': data.get('created_at'),
        'email': data.get('email'),
        'id': data.get('id'),
        'name': data.get('name') or owner,
        'url': data.get('url')
    }

    #сохранение в json
    with open("owner_info.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    #сохранение в текстовом документе
    with open("owner_info.txt", "w", encoding="utf-8") as f:
        f.write(json.dumps(result, indent=2, ensure_ascii=False))

    text.delete(1.0, tk.END)
    text.insert(tk.END, json.dumps(result, indent=2, ensure_ascii=False))

root = tk.Tk()
root.title("GitHub Owner Info")
root.geometry("700x400")

tk.Button(root, text="Получить данные владельца Elasticsearch", command=get_owner_info).pack(pady=10)
text = tk.Text(root, wrap=tk.WORD)
text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
