from bip_utils import Bip39MnemonicValidator, Bip39SeedGenerator, Bip39WordsNum, Bip44, Bip44Coins, Bip44Changes

# Load the BIP39 word list from a local file
def load_bip39_word_list():
    with open("bip39.txt", "r") as f:
        return f.read().splitlines()

# Validate a given seed phrase
def is_valid_seed_phrase(seed_phrase):
    try:
        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(seed_phrase).Generate()
        # Use BIP44 to generate address
        bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
        bip44_acc = bip44_mst.Purpose().Coin().Account(0)
        bip44_chg = bip44_acc.Change(Bip44Changes.CHAIN_EXT)
        bip44_addr = bip44_chg.AddressIndex(0).PublicKey().ToAddress()
        return True
    except Exception as e:
        return False

# Generate and validate all possible 12-word seed phrases
def generate_and_validate_seed_phrases(words, bip39_word_list):
    valid_phrases = []
    for word in bip39_word_list:
        seed_phrase = " ".join(words) + " " + word
        if is_valid_seed_phrase(seed_phrase):
            valid_phrases.append(seed_phrase)
    return valid_phrases

# Main function
def main():
    # Your 11 words
    words = ["word", "word","word","word","word","word","word","word","word","word","word",]

    # Load BIP39 word list
    bip39_word_list = load_bip39_word_list()

    # Generate and validate all possible 12-word seed phrases
    valid_phrases = generate_and_validate_seed_phrases(words, bip39_word_list)

    # Print valid seed phrases
    if valid_phrases:
        print("Valid seed phrases found:")
        for phrase in valid_phrases:
            print(phrase)
    else:
        print("No valid seed phrases found.")

if __name__ == "__main__":
    main()
