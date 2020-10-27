#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser()
    print('Running!')
    subparsers = parser.add_subparsers(dest='command')

    # First command
    add = subparsers.add_parser('add')
    add.add_argument('numbers', nargs="+", type=int)

    sub = subparsers.add_parser('sub')
    sub.add_argument('numbers', nargs='+', type=int)


    args = parser.parse_args()
    if args.command == 'add':
        result = sum(args.numbers)
        print(f'Sum of {args.numbers} is {result}')
    elif args.command == 'sub':
        first, *rest = args.numbers
        result = first - sum(rest)
        print(f'Difference of {args.numbers} is {result}')
    else:
        parser.print_help()
    print(args)
    


if __name__ == '__main__':
    main()