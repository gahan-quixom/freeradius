#!/usr/bin/python
import wrapper
import argparse

def _key(key):
    return [ord(x) for x in key]

def change_password(old_key, new_key, password):
    """change a password."""
    old = password
    if old_key is not None:
        old = wrapper.decrypt(old, _key(old_key))
    print("was: {}".format(password))
    print("now:")
    print(wrapper.encrypt(old, _key(new_key)))

def main():
    """main-entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--oldkey", type=str)
    parser.add_argument("--newkey", required=True, type=str)
    parser.add_argument("--password", required=True, type=str)
    args = parser.parse_args()
    change_password(args.oldkey, args.newkey, args.password)

if __name__ == "__main__":
    main()