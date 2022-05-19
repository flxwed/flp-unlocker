import sys
import traceback

print("making backup...")

try:
    file = sys.argv[1]
    with open(file, "rb") as f:
        with open(file+".bak", "wb+") as f2:
            f2.write( f.read() )

    print(f"saved to {file}.bak")

except Exception:
    print("could not make backup:\n")
    traceback.print_exc()
    input("")
    exit()

print("")
print("unlocking...")

try:
    file = sys.argv[1]
    print(file)

    def hx(h):
        if type(h) == list:
            out = []
            for x in h:
                out.append( int(x, 16) )
            return out
        else:
            return int(h,16)


    with open(file, "rb+") as f:
        content = bytearray( f.read() )
        f.seek(0)

        if content[42] == hx('01'):
            print("could not unlock flp:\nflp is already unlocked")
            input("")
            exit()

        content[42] = hx('01')
        content[46] = hx('2E')
        content[47] = hx('5B')

        content[48:48] = hx((
            #                      # #                      #
            '00 3A 00 32 00 44 00 77 00 38 00 78 00 78 00 39 ' +
            '00 64 00 32 00 78 00 37 00 75 00 3F 00 41 00 43 ' +
            '00 42 00 3A 00 3A 00 38 00 3E 00 00'
        ).split(" "))

        f.write( bytes(content) )
        f.truncate()

    print("flp unlocked successfully.")
    input("")

except Exception:
    print("could not unlock flp:\n")
    traceback.print_exc()
    input("")
    exit()
