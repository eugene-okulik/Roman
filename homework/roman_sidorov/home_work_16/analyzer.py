from pathlib import Path
import argparse
import re
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("file", help="file patrh")
parser.add_argument("-t", help="find text")
args = parser.parse_args()


def parse_log_line_to_dict(line):
    match = re.match(r'(^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3})\s+(.+)$', line)
    if match:
        date_str, message = match.groups()
        try:
            date = datetime.fromisoformat(date_str)
            return date, message.strip()
        except ValueError:
            pass
    return None, line.strip()


def extract_context(message, t, before=5, after=5):
    match = re.search(t, message)
    start, end = match.span()
    matched_t = message[start:end]
    words = message.split()
    char_pos = 0
    target_word_idx = 0
    for i, word in enumerate(words):
        if char_pos <= start < char_pos + len(word):
            target_word_idx = i
            break
        char_pos += len(word) + 1
        start_idx = max(0, target_word_idx - before)
        end_idx = min(len(words), target_word_idx + after + 1)
        context_words = words[start_idx:end_idx]

        context_line = ' '.join(context_words)
        return context_line.replace(matched_t, f'[{matched_t}]', 1)


def logs_in_dir(file, t):
    log_path = Path(file)
    hits = []
    for file_path in log_path.iterdir():
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                dt, message = parse_log_line_to_dict(line)
                match = t in message  and dt != None
                if match:
                    context = extract_context(message, t)
                    hits.append({
                        'file': file_path.name,
                        'line_num': line_num,
                        f'{dt}': context,
                    })
    return hits


print(f"Анализ директории {args.file} и поиск текста {args.t}")
print(logs_in_dir(args.file, args.t))
logs_in_dir(args.file, args.t)
