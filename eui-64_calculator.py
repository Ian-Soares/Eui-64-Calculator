print('='*42)
print('WELCOME TO THE EUI-64 CALCULATOR!'.center(42))
print('='*42)

while True:
    try:
        print('Enter the start of the IPv6 here(enter 0 if there is not)')
        start_of_ipv6 = input('(example: 2001:db8:cafe:1): ').strip().upper()
        if start_of_ipv6 == '0':
            break
        else:
            if len(start_of_ipv6.split(':')) == 4:
                break
            else:
                print('You need to enter 4 hextets of the IPv6!')
    except:
        print()
        print('Something went wrong, try again.')

try:
    while True:
        try:
            print()
            MAC_ADDRESS = input('Enter the Mac Address (like this: 0015.2BE4.9B60): ').strip().upper()
            if len(MAC_ADDRESS.split('.')) == 3:
                for i in MAC_ADDRESS.split('.'):
                    if len(i) == 4:
                        isItRight = 'Yes'
            if isItRight == 'Yes':
                break
            else:
                print('Try again, do not forget to use this pattern: XXXX.XXXX.XXXX')
        except:
            print('Something went wrong, try again and follow the pattern.')

    step1 = MAC_ADDRESS.replace('.','')
    step1_first_half = step1[:6]
    step1_second_half = step1[6:]
    step1 = step1_first_half + 'FFFE' + step1_second_half

    step2 = int(step1_first_half[:2],16)
    binary_step2 = bin(step2).replace('0b','').zfill(8)
    if binary_step2[6] == '0':
        new_binary_step2 = binary_step2[:6]+'1'+binary_step2[7:]
    elif binary_step2[6] == '1':
        new_binary_step2 = binary_step2[:6]+'0'+binary_step2[7:]

    step3 = int(new_binary_step2, 2)
    step3_hex = hex(step3).replace('0x','').zfill(2).upper()

    eui64_ipv6_address = step3_hex + step1[2:4]+ ':' + step1[4:8] + ':' + step1[8:12] + ':' + step1[12:]
    print()
    print(f'The IPv6 calculated through eui-64 for the Mac Address {MAC_ADDRESS} is:')
    if start_of_ipv6 == '0':
        print(f'>>> ::{eui64_ipv6_address}')
    else:
        print(f'>>> {start_of_ipv6}:{eui64_ipv6_address}')
    print()

except:
    print()
    print('Some value was not right, closing the calculator...')
    print()
