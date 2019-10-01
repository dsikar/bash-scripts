
MAX_LIMIT = 65535;

class ByteCombinator():
    """Class to combine two 8 bit bytes into one 16 bit"""

    def combineBytes(self, msByte, lsByte):
        combinedByte = int((msByte << 8) | lsByte);
        if(combinedByte > MAX_LIMIT):
            raise ValueError("@ByteCombinator: Value is more than 16 bit capacity")
        else:
            return combinedByte;
