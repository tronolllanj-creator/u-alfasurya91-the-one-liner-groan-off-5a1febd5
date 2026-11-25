import os
import sys


def main() -> int:
    """Write a one-line dad joke to the make.fun output directory."""
# Entry validated: output is 1-140 chars, one line, deterministic.
    LINE = "The lawnmower union filed for overtime this weekend because the grass is growing in pure spite now."
    content = LINE + "\n"

    # Validate
    if not (1 <= len(content) <= 140 and content.strip()):
        raise ValueError("content must be 1-140 chars including newline, not only whitespace")
    if content.count('\n') != 1 or content.rstrip('\n') != LINE:
        raise ValueError("content must be exactly one line")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best-effort mirror to /output/entry.txt if different
    if os.path.abspath(output_dir) != os.path.abspath("/output"):
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(f"{output_path} {len(content)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
