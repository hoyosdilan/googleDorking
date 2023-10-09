from googlesearch import search
import sys

arguments = sys.argv[1:]
target = ' '.join(arguments)


def google_dork_search(query, num_results=10):
    try:
        print(f"Looking the following query: {query}")
        results = search(query, stop=num_results)
        for i, results in enumerate(results, start=1):
            print(f"{i}. {results}")

    except Exception as e:
        print(f"Error: {e}")


searchList = [
    f'\"{target}\"',
    f'site:linkedin.com \"{target}\"',
    f'inurl:\"{target}\"',
    f'intitle:\"{target}\"',
    f'intext:\"{target}\"',
    f'filetype:pdf \"{target}\"',
    f'filetype:docs \"{target}\"',
    f'filetype:sql \"{target}\"',
    f'filetype:xls \"{target}\"',
    f'filetype:txt \"{target}\"',
]

for query in searchList:
    google_dork_search(query)
