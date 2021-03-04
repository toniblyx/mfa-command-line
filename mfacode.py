#!/usr/bin/python

# MFA Authenticator for the command line
# This script gives a MFA code after 30 seconds from a given Secret key seed (QR code)

# Install pyotp (https://github.com/pyotp/pyotp) as: pip install pyotp
# Usage: python mfacode.py SEED-HERE

import sys
import pyotp

if __name__ == "__main__":

    seed_argument = str(sys.argv[1])
    print("Your seed: "+seed_argument)
    totp = pyotp.TOTP(seed_argument)
    print("MFA code: "+totp.now())
