import string
import sys

WIDTH = 90


def main():
    assert len(sys.argv) == 2
    ciphertext = sys.argv[1]

    with open(ciphertext, "r") as ct:
        letters = list(map(str.upper, ct.readline()))

    length = len(letters)
    matching: dict[str, str] = {x: x for x in list(string.punctuation + " ")}

    while True:
        print("-" * WIDTH)
        left_to_print, i = length, 0

        while not left_to_print < 0:
            cur_slice = letters[
                i * WIDTH : i * WIDTH
                + (left_to_print if left_to_print < WIDTH else WIDTH)
            ]
            print("".join(cur_slice))
            print(
                "".join(
                    map(
                        lambda x: (matching.get(x) if x in matching else "*"), cur_slice
                    )
                )
            )
            print()
            left_to_print -= WIDTH
            i += 1
        print("-" * WIDTH)

        comm = input()
        if comm.upper() in ["CLR", "СДК"]:
            matching = {x: x for x in list(string.punctuation + " ")}
            print("CLEARED")
            continue
        if not len(comm) == 2:
            print("BAD INSTRUCTION")
            continue
        sym, define, *_ = comm
        matching.update({sym.upper(): define.upper()})


if __name__ == "__main__":
    main()
