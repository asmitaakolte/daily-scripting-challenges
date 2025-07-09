
import argparse
import json
from json.tool import main
import os
from datetime import datetime

class Solution: 
    SNIPPET_FILE = 'snippets.json'

    @staticmethod
    def load_snippets():
        if not os.path.exists(Solution.SNIPPET_FILE):
            return []
        with open(Solution.SNIPPET_FILE, 'r') as f:
            return json.load(f)

    @staticmethod
    def save_snippets(snippets):
        with open(Solution.SNIPPET_FILE, 'w') as f:
            json.dump(snippets, f, indent=2)

    @staticmethod
    def add_snippet(args):
        snippets = Solution.load_snippets()
        if any(s['title'] == args.title for s in snippets):
            print(f"Snippet with title '{args.title}' already exists.")
            return
        snippet = {
            'title': args.title,
            'tags': [tag.strip() for tag in args.tags.split(',')] if args.tags else [],
            'code': args.code,
            'created_at': datetime.now().isoformat()
        }
        snippets.append(snippet)
        Solution.save_snippets(snippets)
        print(f"Snippet '{args.title}' added.")

    @staticmethod
    def main():
        parser = argparse.ArgumentParser(description="Code Snippet Manager")
        subparsers = parser.add_subparsers(dest='command', required=True)

        add_parser = subparsers.add_parser('add')
        add_parser.add_argument('--title', required=True)
        add_parser.add_argument('--tags', help="Comma-separated tags")
        add_parser.add_argument('--code', required=True)
        add_parser.set_defaults(func=Solution.add_snippet)

        args = parser.parse_args()
        args.func(args)
if __name__ == "__main__":
    Solution.main()


