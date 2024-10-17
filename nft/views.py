from django.shortcuts import render
from django.http import HttpResponse
from web3 import Web3
from .bayc_contract_abi import contract_abi
from . models import TransferEvent


# Set global variables for infura and bayc address, web3 instance, and start block
infura_url = "https://mainnet.infura.io/v3/104299c58513490cbda8613c81f8ff9e"
bayc_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
web3 = Web3(Web3.HTTPProvider(infura_url))
check_connection = web3.is_connected()
start_block = 20099955


def landing_page_view(request):
    if not check_connection:
        return HttpResponse("Connection failed")
    return render(request, 'landing_page.html')


def transfer_events_view(request):
    contract = web3.eth.contract(address=bayc_address, abi=contract_abi)
    transfer_filter = contract.events.Transfer.create_filter(
        from_block=start_block, to_block="latest"
    ).get_all_entries()

    # check if there are any new transfer events
    if transfer_filter:
        for transfer in transfer_filter:
            # check if the tokenId is already in the database
            token_id_exists = TransferEvent.objects.filter(token_id=transfer.args['tokenId']).exists()
            if not token_id_exists:
                TransferEvent.objects.create(
                    token_id=transfer.args['tokenId'],
                    from_address=transfer.args['from'],
                    to_address=transfer.args['to'],
                    transaction_hash=transfer.transactionHash.hex(),
                    block_number=transfer.blockNumber
                )
            else:
                continue
    return render(request, 'transaction_events.html')
