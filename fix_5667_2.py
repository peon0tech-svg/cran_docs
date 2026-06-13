import re

def decode_garbled(text):
    out = []
    # If the text has &amp; let's temporarily convert it to & for decoding
    text = text.replace('&amp;', '&')
    for c in text:
        if c == 'À':
            out.append('fi')
        elif c == 'Á':
            out.append('fl')
        elif c == 'µ':
            out.append('"')
        elif c == '´':
            out.append('"')
        elif c == '²':
            out.append('2')
        elif c == '¶':
            out.append("'")
        elif c == '·':
            out.append("'")
        elif 33 <= ord(c) <= 95 and c not in ['|', '#', '-', '*', '>', '<']:
            out.append(chr(ord(c) + 29))
        else:
            out.append(c)
    return "".join(out)

with open('docs/gazettes/5667.md', 'r') as f:
    text = f.read()

# Instead of large exact phrases, let's target the exact garbled substrings using their distinctive uppercase/symbol nature.
garbled_chunks = [
    r'EHWZHHQ 0ERN ,QYHVWPHQWV &amp;RPSDQ\\ \/WG RQ ÀOH ZLWK WKH \$XWKRULW\\ DQG 1&amp;&amp; IRUPV WKH',
    r'FRUUHVSRQGHQFH RQ ÀOH WKDW GHPRQVWUDWHV 0ERN ,QYHVWPHQWV &amp;RPSDQ\\ \/WG ·V GHVLUH LV WR',
    r'F &amp;HUWLÀHG FRSLHV RI FRPSDQ\\ UHJLVWUDWLRQ',
    r'L 7KH &amp;RPSDQLHV \$FW \$FW 1R RI GHÀQHV D ¶SODFH RI EXVLQHVV· WR PHDQ',
    r'LL 7KH \$XWKRULW\\ QRWHV WKDW GXULQJ WKH ZHHN RI ² \-DQXDU\\ WKH &amp;RQÀGDQWH QHZVSDSHU',
    r'LLL \$FFRUGLQJ WR WKH &amp;RQÀGDQWH RQH FOLHQW FODLPV QRW WR KDYH KDG DQ\\ NQRZOHGJH WKDW VKH',
    r'1DÀVK 7UDGLQJ &amp;&amp; W D \$PHVKR \)0',
    r'%\\ KDQG WR WKH KHDG RIÀFHV RI WKH \$XWKRULW\\ QDPHO\\ &amp;RPPXQLFDWLRQ \+RXVH 5REHUW',
]

for p in garbled_chunks:
    for m in re.finditer(p, text):
        garbled = m.group(0)
        decoded = decode_garbled(garbled)
        text = text.replace(garbled, decoded)

with open('docs/gazettes/5667.md', 'w') as f:
    f.write(text)

