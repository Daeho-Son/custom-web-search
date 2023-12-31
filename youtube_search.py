import sys
from workflow import Workflow3
import pickle

def get_suggest(query):
    return query


def main(wf):
    query = wf.argv[0]
    print("query: " + query)

    def wrapper():
        return get_suggest(query)

    wf.send_feedback()


if __name__ == "__main__":
    wf = Workflow3()
    sys.exit(wf.run(main))
