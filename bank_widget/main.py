from bank_widget.src.masks import get_mask_card_number, get_mask_account
from bank_widget.src.widget import mask_account_card, get_date

# data_time = input()
card_or_bill = input()
# card = input()
# account = input()
#
# print(get_mask_card_number(card))
# print(get_mask_account(account))
print(mask_account_card(card_or_bill))
# print(get_date(data_time))