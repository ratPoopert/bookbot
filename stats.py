def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def count_characters(text: str) -> dict[str, int]:
    result = {}
    for char in text:
        key = char.lower()
        if key not in result:
            result[key] = 0
        result[key] += 1
    return result


def character_stats(character_count: dict[str, int]) -> dict:
    result = []
    for char, count in character_count.items():
        result.append({
            "character": char,
            "count": count,
        })
    result.sort(key=lambda x: x["count"],
                reverse=True)
    return result
