def get_pet_shop_name(pet_shop_dict):
    return pet_shop_dict["name"]


def get_total_cash(pet_shop_dict):
    return pet_shop_dict["admin"]["total_cash"]


def add_or_remove_cash(pet_shop_dict, cash_change_amount):
    pet_shop_dict["admin"]["total_cash"] = get_total_cash(pet_shop_dict) + cash_change_amount
    return pet_shop_dict


def get_pets_sold(pet_shop_dict):
    return pet_shop_dict["admin"]["pets_sold"]


