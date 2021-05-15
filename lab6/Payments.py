from helpers import get_hash, rsakeys, encrypt, decrypt, sign, verify, aeskey, aesencrypt, aesdecrypt

def main():
    """
    Part-1: Payment Request Generation
    """
    print("-------------------------------------------------------")
    print("---PAYMENT REQUEST GENERATION---")
    cust_privkey, cust_pubkey = rsakeys()
    bank_privkey, bank_pubkey = rsakeys()

    print("Customer's private key-", cust_privkey)
    print("Customer's public key-", cust_pubkey)
    print("Bank's private key-", bank_privkey)
    print("Bank's public key-", bank_pubkey)

    payment_info = 'Some payment information'
    order_info = 'Some order information'

    PIMD = get_hash(payment_info)
    OIMD = get_hash(order_info)
    POMD = get_hash(PIMD + OIMD)

    dual_sign = sign(cust_privkey, POMD)

    key_s = aeskey()
    encrypted_pi, iv_pi = aesencrypt(payment_info, key_s)
    encrypted_oimd, iv_oimd = aesencrypt(OIMD, key_s)
    encrypted_ds, iv_ds = aesencrypt(dual_sign, key_s)

    digital_envelope = encrypt(bank_pubkey, key_s)

    """
    Part 2: Purchase Request Validation from 
    Merchant side
    """

    merchant_oimd = get_hash(order_info)
    merchant_pomd = get_hash(PIMD + merchant_oimd)
    
    check_sign_merchant = verify(cust_pubkey, merchant_pomd, dual_sign)

    if check_sign_merchant:
        print("-------------------------------------------------------")
        print("[INFO] Merchant Signatures match")
        print("\tPurchase request validated by merchant")
        print("\t---PURCHASE REQUEST VALIDATED---")
        print("-------------------------------------------------------")
    else:
        print("-------------------------------------------------------")
        print("[INFO] Signatures do not match")
        print("\tPurchace request rejected- Signatures do not match!!")
        return

    """
    Part 3: Payment authorization
    """
    bank_key_s = decrypt(bank_privkey, digital_envelope)

    bank_pi = aesdecrypt(encrypted_pi, bank_key_s, iv_pi).decode()
    bank_oimd = aesdecrypt(encrypted_oimd, bank_key_s, iv_oimd).decode()
    bank_ds = aesdecrypt(encrypted_ds, bank_key_s, iv_ds)

    bank_pimd = get_hash(bank_pi)
    bank_pomd = get_hash(bank_pimd + bank_oimd)

    check_sign_bank = verify(cust_pubkey, bank_pomd, dual_sign)

    if check_sign_bank:
        print("[INFO] Bank Signatures match")
        print("\tPayment authorized by the bank")
        print("\t---PAYMENT AUTHORIZATION SUCCESSFUL---")
        print("-------------------------------------------------------")
        print("\t---PAYMENT CAPTURE SUCCESSFUL---")
        print("-------------------------------------------------------")
    else:
        print("[INFO] Signatures do not match")
        print("\tPayment authorization failed- Signatures do not match!!")

main()




    
