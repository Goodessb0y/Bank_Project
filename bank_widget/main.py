from bank_widget.src import get_mask_card_number, get_mask_account

card = input()
account = input()

print(get_mask_card_number(card))
print(get_mask_account(account))