import pandas as pd
from eth_account import Account
from eth_account.hdaccount import generate_mnemonic


def enable_hd_wallet_features():
    # Enable HD Wallet features in eth_account
    Account.enable_unaudited_hdwallet_features()


def generate_wallets(num_wallets):
    enable_hd_wallet_features()  # Ensure HD Wallet features are enabled
    wallets = []

    for i in range(num_wallets):
        # Generate a random mnemonic (seed phrase)
        mnemonic_phrase = generate_mnemonic(num_words=12, lang='english')

        # Create an account from the mnemonic phrase
        wallet_account = Account.from_mnemonic(mnemonic_phrase)

        wallet_address = wallet_account.address
        wallet_private_key = wallet_account.key.hex()

        print(f'Account {i + 1}\n'
              f'Seed Phrase: {mnemonic_phrase}\n'
              f'Private Key: {wallet_private_key}\n'
              f'Public Address: {wallet_address}\n'
              '--------------------------')

        wallet_info = {
            'seed_phrase': mnemonic_phrase,
            'private_key': wallet_private_key,
            'address': wallet_address

        }

        wallets.append(wallet_info)

    return wallets


def save_wallets_to_csv(wallets, filename):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(wallets)
    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)


def main():
    num_wallets = int(input("How many wallets to create? "))
    wallets = generate_wallets(num_wallets)
    save_wallets_to_csv(wallets, 'evm_wallets.csv')
    print("Wallet information has been saved to 'evm_wallets.csv'.")


if __name__ == "__main__":
    main()
