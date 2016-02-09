import re
import colorama
import subprocess

def mark_word(word,string,colorfg,colorbg = ""):
    to_find = re.compile(word+"(s)?",re.IGNORECASE)
    for found in to_find.finditer(string):
        string = string[:found.start()] + colorfg  + colorbg + string[found.start():found.end()] + colorama.Style.RESET_ALL + string[found.end():]
    return string

def mark_line(word,string,colorfg,colorbg = colorama.Back.BLACK):
    to_find = re.compile(word+"(s)?",re.IGNORECASE)
    for found in to_find.finditer(string):
        string =  colorfg  + colorbg + string + colorama.Style.RESET_ALL
    return string


if __name__ == "__main__":

    proc = subprocess.Popen(
            "scons",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True
            )

    colorama.init()
    output = proc.communicate()
    print(colorama.Style.RESET_ALL)

    for a in output:
        if a is not None:
            a = a.split('\n')[:-1]
            to_find_err = re.compile("error(s)?",re.IGNORECASE)
            to_find_warn= re.compile("warning(s)?",re.IGNORECASE)
            for b in a:
                b = mark_word("error",      b, colorfg = colorama.Fore.RED )
                b = mark_word("warning",    b, colorfg = colorama.Fore.YELLOW )
                b = mark_line("terminated", b, colorfg = colorama.Fore.WHITE, colorbg = colorama.Back.RED )
                if b.find(">>><<<") >=0:
                    b = b[b.find(">>><<<")+6:]
                    b = colorama.Fore.CYAN + b + colorama.Style.RESET_ALL
                print(b)
