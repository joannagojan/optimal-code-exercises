import re
"""
Write a function that takes an email address as the first argument and an expected domain as the second argument. 
The function checks if the email address has the expected domain. If it does, 
the function returns the email address; if not, the function returns the email address with the expected domain.
"""


def is_text_same(evaluated: str, pattern: str) -> bool:
    return evaluated == pattern


def remove_prefix(text: str, char: str) -> tuple[str, str]:
    if len(char) != 1:
        raise ValueError("The char needs to be one character string")
    else:
        if (index := text.find(char)) != -1:
            return text[0:index], text[index:]
        else:
            raise ValueError


def get_username_domain(email: str) -> tuple[str, str, str]:
    separate_username = remove_prefix(email, '@')
    if separate_username is None:
        raise ValueError("Email address needs to contain @")
    else:
        username = separate_username[0]
        if username is None:
            raise ValueError("It is not an email address")
        else:
            separate_domain = remove_prefix(separate_username[1], ".")
            domain = separate_domain[0][1:]
            if domain == "":
                raise ValueError("Email needs to contain a after domain name")
            else:
                tld = separate_domain[1]
                return username, domain, tld


def guarantee_domain(email: str, target_full_domain: str) -> str:
    if re.search(r'^[a-z]+\.[a-z]+$', target_full_domain) is None:
        raise ValueError('The target domain input is not correct')
    else:
        username, domain, tld = get_username_domain(email)[0], get_username_domain(email)[1], get_username_domain(email)[2]
        target_domain, target_tld = remove_prefix(target_full_domain, '.')[0], remove_prefix(target_full_domain, '.')[1]
        if domain != target_domain and target_tld != tld:
            return username + "@" + target_domain + target_tld
        else:
            return email


# TODO find missing ValueError

def main() -> None:
    try:
        print(get_username_domain("fvjn@gmna.vo"))
        print(guarantee_domain('henlo@gmail.com', "gmail.pl"))
        print(guarantee_domain('henlo@gmail.com', "onet.pl"))
        print(guarantee_domain('henlo@gmail.com', "gmail.com"))
        print(guarantee_domain('henlo@gmail.com', "gmail"))
        print(guarantee_domain('gmail.com', "gmail"))
        print(guarantee_domain('gmailcom', "gmail"))
    except ValueError as e:
        print(e)



if __name__ == '__main__':
    main()
