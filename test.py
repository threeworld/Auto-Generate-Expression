from fractions import Fraction

def get_fraction(item):
    result = 0
    if item.find('/') > 0:
        attach = 0
        right = ""
        if item.find("'") > 0:
            parts = item.split("'")
            attach = int(parts[0])
            right = parts[1]
        else:
            right = item

        parts = right.split('/')
        return Fraction(attach * int(parts[1]) + int(parts[0]), int(parts[1]))
    else:
        result = int(item);
        return Fraction(result, 1)
