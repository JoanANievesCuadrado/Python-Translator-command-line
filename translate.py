import logging
# import re
import translators as ts

from os import name
from os import system


logging.basicConfig(
                    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',  # noqa: E501
                    level=logging.WARNING)
logger = logging.getLogger()

langs = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Basque": "eu",
    "Belarusian": "be",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Cebuano": "ceb",
    "Chichewa": "ny",
    "Chinese (simplified)": "zh-CN",
    "Chinese (traditional)": "zh-TW",
    "Corsican": "co",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Esperanto": "eo",
    "Estonian": "et",
    "Filipino": "tl",
    "Finnish": "fi",
    "French": "fr",
    "Frisian": "fy",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian creole": "ht",
    "Hausa": "ha",
    "Hawaiian": "haw",
    "Hebrew": "iw",
    "Hindi": "hi",
    "Hmong": "hmn",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jw",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Korean": "ko",
    "Kurdish (kurmanji)": "ku",
    "Kyrgyz": "ky",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Malagasy": "mg",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Myanmar (burmese)": "my",
    "Nepali": "ne",
    "Norwegian": "no",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan": "sm",
    "Scots gaelic": "gd",
    "Serbian": "sr",
    "Sesotho": "st",
    "Shona": "sn",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tajik": "tg",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu",
    "Auto-detect": "auto",
}
engines = [
    "google",
    "yandex",
    "bing",
    "sogou",
    "baidu",
    "tencent",
    "youdao",
    "alibaba",
    "deepl",
]

L1 = 'auto'
L2 = 'es'


def clear():
    """Clear Screen."""
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_input(prompt='>>> '):
    """Get input."""
    lines = []
    while True:
        print(prompt, end='')
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = ' '.join(lines)

    return text

print('Default languages are from \'auto\' to \'es\'')
t = input('Can you change the languages?(y/n): ')
clear()
if t == 'y' or t == 'Y':
    L1 = L2 = ''
    print('List of available codes:')
    print("\n".join(f"* {k}: {v}" for k, v in langs.items()))
    while L1 not in langs.values():
        L1 = input('Set L1 language: ')
        if L1 not in langs.values():
            print('Invalid language code.')
    # clear()
    while L2 not in langs.values():
        L2 = input('Set L2 language: ')
        if L2 not in langs.values():
            print('Invalid language code.')
    clear()

file1 = open('from_language.txt', 'w', encoding='utf-8', errors='ignore')
file2 = open('to_language.txt', 'w', encoding='utf-8', errors='ignore')
while True:
    try:
        text = get_input()
    except EOFError:
        break
    # print('\n\n')
    print('\033c')
    print('Wait some seconds ...')
    for name in engines:
        try:
            result = getattr(ts, name)(text, from_language=L1, to_language=L2)
            print(f'Use engine: {name}\n\n')
            break
        except Exception as ex:  # noqa
            logger.exception('Exception occurred while code execution: ' + str(ex))  # noqa
            # logger.exception(ex)
    else:
        result = "❌ Error! Failed to translate :("
    # print('\n\n')
    print('\033c')

    print(result)
    # print('\n\n')

    file1.write(text + '\n\n')
    file2.write(result + '\n\n')

file1.close()
file2.close()

print('\n\nExit at your wish (.)(.)')
