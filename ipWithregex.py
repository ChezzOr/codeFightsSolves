import re
import re
def isIPv4Address(line):
    try:
        regex = re.compile(r'(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))')
        if regex.match(line):
            line = line.split('.')
            if len(line) != 4:
                return False
            if 0 <= int(line[0]) <= 255 and 0 <= int(line[1]) <= 255 \
                    and 0 <= int(line[2]) <= 255 and 0 <= int(line[3]) <= 255:
                return True
            else:
                return False
        else:
            return False
    except:
        return False

if __name__ == '__main__':
    print(isIPv4Address('0.254.255.0'))