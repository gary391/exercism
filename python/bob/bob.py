def response(hey_bob):
    """
    "Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
    "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
    "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
    "Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
    "Whatever." This is what he answers to anything else.
    :param hey_bob:
    :return: string

    """
    # If hey_bob contains question mark -> "Sure."
    # If hey_bob is in all capital -> "Whoa, chill out!"
    # If hey_bob is in all capital with question mark -> "Calm down, I know what I'm doing!"
    # If hey_bob is None or "" -> "Fine. Be that way!"
    # Anything else -> "Whatever."

        if  not hey_bob.isupper() and (hey_bob.strip()).endswith("?"):
            return "Sure."
        if hey_bob.isspace() or hey_bob is None or hey_bob == "":
            return "Fine. Be that way!"
        if hey_bob.isupper() and "?" in hey_bob:
            return "Calm down, I know what I'm doing!"
        if hey_bob.isupper():
            return "Whoa, chill out!"
    
        return "Whatever."