#!/usr/bin/env python3
"""Check whether the expected hybrid TLS group was negotiated."""

import argparse
import sys

EXPECTED_GROUP = "X25519MLKEM768"


def main():
    parser = argparse.ArgumentParser(
        description="Check the negotiated TLS key-exchange group."
    )
    parser.add_argument(
        "group",
        help="Negotiated group name (for example, X25519MLKEM768)",
    )
    args = parser.parse_args()

    # Handshake success is not a test. Selected group is.
    if args.group == EXPECTED_GROUP:
        print(f"PASS: negotiated group is {EXPECTED_GROUP}")
        return 0

    print(
        f"FAIL: expected {EXPECTED_GROUP}, got {args.group}",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
