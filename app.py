import os
import requests
from flask import Flask, request, jsonify
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser

app = Flask(__name__)

# Define schema for indexing
schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True))
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
    ix = create_in("indexdir", schema)
else:
    ix = open_dir("indexdir")

# Use pre-downloaded text files instead of scraping
doc_files = {
    "Segment": "segment.txt",
    "mParticle": "mparticle.txt",
    "Lytics": "lytics.txt",
    "Zeotap": "zeotap.txt"
}

def load_and_index():
    writer = ix.writer()
    for platform, file_path in doc_files.items():
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

                # Debugging: Print first 500 characters of each file
                print(f"Loaded {platform}: {text[:500]}\n")

                writer.add_document(title=platform, content=text)
        except FileNotFoundError:
            print(f"Warning: {file_path} not found. Skipping {platform}")

    writer.commit()


@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.json.get("query", "").lower()

    with ix.searcher() as searcher:
        results = []
        for doc in searcher.documents():
            doc_text = doc["content"].lower()

            if any(word in doc_text for word in user_query.split()):
                snippet = doc_text[:500]  # Limit to 500 characters
                snippet_clean = snippet.split("\n")  # Split into lines
                snippet_clean = [line.strip() for line in snippet_clean if line.strip() and not line.startswith("#")]  # Remove empty lines & section headers

                results.append("\n".join(snippet_clean[:8]))  # Limit response to 8 lines

        print(f"User Query: {user_query}")
        print(f"Search Results Found: {len(results)}")

        if not results:
            return jsonify({"answers": ["No relevant information found. Try using different keywords."]})

    return jsonify({"answers": results[:1]})  # Return only the most relevant result


if __name__ == "__main__":
    load_and_index()
    app.run(debug=True)
