         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Welcome to my AWS repo numéro un !

This repository contains Python and JSON files created and coded utilising AWS Cloud9 CLI as browser-based shell, together with its browser-based IDE code editor and debugger. It was carried out as one of many laboratory activities in _AWS re/Start Cloud Computing with AI Bootcamp._
 
The scripts contained herein are a demonstration of skills in using AWS resources to solve practical problems, and in using Python for scientific computing applications in biochemistry and also in cryptography.

I executed tasks to successfully achieve the following objectives:



**1. Human Insulin - Basic Analysis**

*   Retrieve the protein (amino acids) sequence of human preproinsulin, in preparation for analysis of human insulin.

*   Use string manipulations to obtain the amino acid sequence of human insulin from preproinsulin.

*   Perform basic maths on the sequence and molecular weight of insulin.

*   Calculate the _net charge_ of insulin by first creating a dictionary of amino acid pKa values (pKa indicates the strength of an acid).



**2. Cryptography - Basic Encryption and Decryption**

*   Implement a Caesar Cipher encryption program.

*   Define cipher keys.

*   Encrypt messages.

*   Decrypt messages.

*   Utilise features of the AWS Cloud9 Python Debugger.



Enjoy !

Please visit https://docs.aws.amazon.com/console/cloud9/ for AWS Cloud9 documentation.


= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 


**Clarification** - In the file _calc_weight_json.py_, the calculated and stated "rough molecular weight of insulin" is obtained to be 6696.42. The actual molecular weight of human insulin (monomer) is 5808 _Daltons_. The simple reason for this whopping 15% discrepancy is that the creators of this laboratory exercise were rightly focused on computing using AWS Cloud9, not on the details of biochemistry.

I explain the discrepancy below for those who are interested.

The functional building block of human insulin is made up of 51 amino acids, each with their own molecular weight. Adding together the 51 molecular weights of the constituent amino acids provides a ballpark figure.

To get an accurate figure, one must take into consideration the removal of 1 water molecule (dehydration reaction) every time amino acids combine (to form a peptide bond). Combining 51 amino acids means one must subtract 49 molecules of water from the ballpark figure (normal polypeptide formation would have subtracted 50 - insulin is slightly different due to further snipping of a C-peptide).

Water (H2O) has a molecular weight of 18, so 18 x 49 = 882. 
Subtract this from calculated approximation = 6696 - 882 = 5814.

Finally subtract the 6 hydrogens lost (atomic weight 1 each) due to 3 disulfide bond formation:
5814 - 6 = 5808.

And with that, Bob is your uncle ! 


_**Illustration:**_

```text

1. Dipeptide Formation:

    R1                      R2                           R1  O     R2
    |                       |                            |  ||     |
NH2-CH-COOH    +        NH2-CH-COOH      --->        NH2-CH-C--NH--CH-COOH  +  H2O

Amino Acid 1            Amino Acid 2                          Dipeptide


2. Polypeptide / Protein Formation:

        R1                R2                        Rn
        |                 |                         |
n [ NH2-CH-COOH ] + [ NH2-CH-COOH ] + . . . + [ NH2-CH-COOH ] 

  Amino Acid 1       Amino Acid 2              Amino Acid n

                             |
                             v

            R1    O       R2    O               Rn    O
            |    ||       |    ||               |    ||
      NH2 — CH — C — NH — CH — C — . . . — NH — CH — C — OH  +  (n-2)H2O
       \__________________________________________________/
                       Polypeptide / Protein

```
