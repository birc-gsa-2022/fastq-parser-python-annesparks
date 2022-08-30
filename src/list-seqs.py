import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Extract the sequences from a simple-fastq file")
    argparser.add_argument(
        "fastq",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    for l in (l for l in args.fastq if l and not l.startswith('@')):
        print(l.strip())


if __name__ == '__main__':
    main()
