import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Extract the names from a simple-fastq file")
    argparser.add_argument(
        "fastq",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    for l in args.fastq.readlines():
        if l[0] == "@":
            print(l[1:].strip())


if __name__ == '__main__':
    main()
