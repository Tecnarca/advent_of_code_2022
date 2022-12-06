from pathlib import Path

def find_token(buffer: str, marker_length: int) -> int:
    tokens_candidate_lenghts = [len(set(buffer[i:i+marker_length])) for i in range(len(buffer)-marker_length)]
    return tokens_candidate_lenghts.index(marker_length)+marker_length

buffer = Path("input").read_text()

print(find_token(buffer, 4))
print(find_token(buffer, 14))