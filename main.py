#!/usr/bin/env python3
"""Write a short text, meant to relax its reader, to $MAKEFUN_OUTPUT_DIR/entry.txt.

The text is written exactly as given: 266 Unicode code points, inside the
competition gate of 1-280. Python 3.13, standard library only, no network.
"""

import os

# The entry text, byte for byte: no trailing newline, nothing added or cut.
TEXT = "The rain has settled into its slow rhythm on the roof, and the kettle has gone quiet. The lamp is warm, the tea is still warm, and the cat has taken the exact middle of the rug, as if the evening had a centre and she found it. Nothing here is asking anything of you."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
