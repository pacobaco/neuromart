from web3 import Web3

class BlockchainIntegration:
    def __init__(self, infura_url, private_key, contract_address):
        self.web3 = Web3(Web3.HTTPProvider(infura_url))
        self.private_key = private_key
        self.contract_address = contract_address
        self.account = self.web3.eth.account.privateKeyToAccount(private_key)

    def send_tokens(self, recipient_address, amount):
        nonce = self.web3.eth.getTransactionCount(self.account.address)
        gas_price = self.web3.eth.gas_price
        tx = {
            'nonce': nonce,
            'gas': 2000000,
            'gasPrice': gas_price,
            'to': recipient_address,
            'value': self.web3.toWei(amount, 'ether'),
            'chainId': 1,  # Mainnet or testnet
        }
        signed_tx = self.web3.eth.account.signTransaction(tx, self.private_key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash
