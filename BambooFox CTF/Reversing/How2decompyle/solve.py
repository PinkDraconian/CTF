#!/usr/bin/env python3

import string


def main():
    restrictions = ['uudcjkllpuqngqwbujnbhobowpx_kdkp_', 'f_negcqevyxmauuhthijbwhpjbvalnhnm', 'dsafqqwxaqtstghrfbxzp_x_xo_kzqxck', 'mdmqs_tfxbwisprcjutkrsogarmijtcls', 'kvpsbdddqcyuzrgdomvnmlaymnlbegnur', 'oykgmfa_cmroybxsgwktlzfitgagwxawu', 'ewxbxogihhmknjcpbymdxqljvsspnvzfv', 'izjwevjzooutelioqrbggatwkqfcuzwin', 'xtbifb_vzsilvyjmyqsxdkrrqwyyiu_vb', 'watartiplxa_ktzn_ouwzndcrfutffyzd', 'rqzhdgfhdnbpmomakleqfpmxetpwpobgj', 'qggdzxprwisr_vkkipgftuvhsizlc_pbz', 'jerzhlnsegcaqzathfpuufwunakdtceqw', 'lbvlyyrugffgrwo_v_zrqvqszchqrrljq', 'aiwuuhzbszvfpidwwkl_wynlujbsbhfox', 'vmhrizxtiegxdxsqcdoiyxkffloudwtxg', 'tffjnabob_jbf_qiszdsemczghnjysmah', 'zrqkppvynlkelnevngwlkhgaputhoagtt', 'nl_oojyafwoqccbedijmigpedkdzglq_f', 'cksy_skctjlyxktuzchvstunyvcvabomc', 'ppcxleeguvhvhengmvac_bykhzqohjuei', '_clmaicjrrzhwd_fescyaejtbyefxyihy', 'hhopvwsmjtpjiffzatyhjrev_dwnsidyo', 'sjevtrmkkk_zjalxrxfovjsbcxjx_pskp', 'gnynwuuqypddbsylparpcczqimimqmvdl', 'bxitcmhnmanwuhvjxnqeoiimlegrmkjra']

    flag = ''
    # Loops over first char of each string in restrictions array
    for i in range(len(restrictions[0])):
        # The current_char we're looking for can be any lowercase char or _
        current_char = string.ascii_lowercase + '_'
        for j in range(len(restrictions)):
            # Every char that exists, isn't our string char, so we replace them with nothing
            current_char = current_char.replace(restrictions[j][i], '')
        # We end up with one char every time. This one is part of our flag
        flag += current_char

    # Code for putting capitals in our flag from the original decompiled file
    capital = [0, 4, 9, 19, 23, 26]
    cap_flag = ''
    for f in range(len(flag)):
        if f in capital:
            cap_flag += flag[f].upper()
        else:
            cap_flag += flag[f]

    print('BambooFox{' + cap_flag + '}')


if __name__ == "__main__":
    main()
