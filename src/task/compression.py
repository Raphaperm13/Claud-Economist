import re

def delete_extra_spaces(prompt: str) -> str:
    if not prompt:
        return prompt
    pattern = r'("[^"\\]*")'
    chunks = re.split(pattern, prompt)
    cleaned_chunks = []
    for chunk in chunks:
        if chunk.startswith('"') and chunk.endswith('"'):
            cleaned_chunks.append(chunk)
            continue
        cleaned_chunk = chunk
        cleaned_chunk = re.sub(r' +', ' ', cleaned_chunk)
        cleaned_chunk = re.sub(r'\t+', ' ', cleaned_chunk)
        cleaned_chunk = re.sub(r'\n+', '\n', cleaned_chunk)
        cleaned_chunks.append(cleaned_chunk)
    prompt = "".join(cleaned_chunks)
    chunks = re.split(pattern, prompt)
    final_chunks = []
    for chunk in chunks:
        if chunk.startswith('"') and chunk.endswith('"'):
            final_chunks.append(chunk)
            continue
        lines = chunk.splitlines()
        cleaned_lines = []
        for line in lines:
            cleaned_line = line.strip()
            if cleaned_line:
                cleaned_lines.append(cleaned_line)
        final_chunks.append("\n".join(cleaned_lines))
    prompt = "".join(final_chunks)
    return prompt

def compression(prompt: str) -> str:
    prompt = delete_extra_spaces(prompt)
    return prompt