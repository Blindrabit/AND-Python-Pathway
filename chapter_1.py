from typing import Dict, List


def ordered_andi(andis: Dict[int, str]) -> List[str]:
    """
    Takes a dictionary of ANDi names and returns a list of their names in alphabetical order.
    :param andis:
    :return:
    """
    return sorted(andis.values(), key=str.casefold)


def anti_procrastination_tool(string: str, phrases: List[str]) -> str:
    for phrase in phrases:
        if phrase.lower() in string.lower():
            return "NO!"
    return "Safe watching!"


def hacker_speak(string: str, char_to_replace: Dict[str, int]) -> str:
    for key, value in char_to_replace.items():
        string = string.replace(key, str(value))
    return string


if __name__ == '__main__':

    # Ordered Andi's
    # returns ['Adam', 'Anastasiia', 'ANDrew', 'Jorge', 'Reuben', 'Toni']
    input_andis = {1: "Toni", 2: "Reuben", 3: "Jorge", 4: "ANDrew", 5: "Anastasiia", 6: "Adam"}
    print(ordered_andi(input_andis))

    # Anti Procrastination Tool
    input_phrases = ["Dog", "pet", "music", "Funny meme", "Listen to this"]

    # returns NO!
    input_string = "dogs are cool Pets"
    print(anti_procrastination_tool(input_string, input_phrases))

    # should return Safe watching!
    input_string = "Listen to a important work podcast!"
    print(anti_procrastination_tool(input_string, input_phrases))

    # Hacker Speak
    input_char_to_replace = {"a": 4, "e": 3, "i": 1, "o": 0, "s": 5}

    # should return 4ndd1g1t4l 15 c00l
    input_string = "anddigital is cool"
    print(hacker_speak(input_string, input_char_to_replace))

    # should return h4ck3r 5p34k
    input_string = "hacker speak"
    print(hacker_speak(input_string, input_char_to_replace))


