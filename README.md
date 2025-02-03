# Thai Password List Generator for EAPOL Decryption

## Overview

This script generates multiple text files containing potential WiFi passwords, which can be used for EAPOL (Extensible Authentication Protocol Over LAN) decryption. In Thailand, many users set their WiFi passwords as their mobile phone numbers. Studies show that ```approximately 90%``` of WiFi passwords in Thailand follow this pattern. This script focuses on generating password lists that align with common Thai password patterns, increasing the chances of successful WPA/WPA2 handshake decryption.


## Common Thai WiFi Password Patterns

In Thailand, WiFi passwords are frequently set using:

 • Mobile phone numbers (starting with ```08```, ```09```, or ```06```)

 • Custom name-based sequences (e.g., ```nameWIFI0000```)

 • Simple numeric sequences


## Generated Files

The script produces five password list files:

 1. part1.txt - Generates numeric sequences from ```00000000``` to ```99999999```, prefixed with ```08``` (common mobile number format in Thailand).

 2. part2.txt - Generates numeric sequences from ```00000000``` to ```99999999```, prefixed with ```09``` (common mobile number format in Thailand).

 3. part3.txt - Generates numeric sequences from ```00000000``` to ```99999999``` with no prefix.

 4. part4.txt - Generates numeric sequences from ```00000000``` to ```99999999```, prefixed with ```06``` (another common mobile number format in Thailand).

 5. CustomLIS.txt - Generates a list of potential WiFi passwords with a custom prefix (nameWIFI) followed by a four-digit numeric sequence (```0000``` to ```9999```).


Usage

Run the script in a Python environment:

```
python THAIpasswd.py
```

This will generate large password lists, so ensure you have sufficient disk space before execution.


## Notes

 • The generated files are plaintext and can be used with WiFi penetration testing tools like ```hashcat``` or ```aircrack-ng```.

 • The script may take a significant amount of time and system resources due to the large number of iterations.

 • Modify the script to add more prefixes or custom formats as needed.


## Disclaimer

This script is intended for ethical security testing and research purposes only. Unauthorized use against networks you do not own or have permission to audit is illegal.



# Common Phone List

	06

060 TrueMove , TrueMove H (VoIP)
061 AIS, DTAC, TrueMove H
062 AIS, DTAC
063 AIS, DTAC, TrueMove H
064 AIS, TrueMove H
065 AIS, DTAC, TrueMove H
066 DTAC
067
068 TOT (VoIP)
069

	08

080
0800 AIS
0801 AIS
0802 AIS
0803 TrueMove
0804 DTAC
0805 DTAC
0806 AIS
0807 AIS
0808 AIS
0809 TrueMove H

	081

Group number 081-0xx = AIS
Group number 081-1xx is divided into
- 100 to 149 = DPC
- 170 to 179 = AIS
Group number 081-2xx is divided into
- 200 = ACeS
- 205 to 209 = DTAC
- 240 to 244 = DPC
- 250 to 299 = AIS
Group number 081-3xx is divided into
- 300 to 309 = DTAC
- 310 to 339 = DPC
- 340 to 349 = DTAC
- 350, 351, 354, 356 = Hutch
- 360 to 389 = AIS
- 390 to 399 = DTAC
Group number 081-4xx = DTAC
Group number 081-5xx is divided into
- 500 to 529 = DPC
- 530 to 599 = DTAC
Group number 081-6xx = DTAC
- Except for categories 610, 617, 624, 630, 656 = DPC
Group number 081-7xx = AIS
- Except for categories 710 to 719 = DTAC
Group number 081-8xx = AIS
Group number 081-9xx = AIS
Or it may be summarized in general as follows.
0810 AIS
0811 AIS
0812 AIS
0813 DTAC
0814 DTAC
0815 DTAC
0816 DTAC
0817 AIS
0818 AIS
0819 AIS
082 AIS ,TrueMove H
083 AIS ,TrueMove, DTAC
084 AIS ,TrueMove H
085 AIS ,DTAC
086 AIS ,TrueMove, DTAC

	087

0871 AIS
0872 ?
0873 DTAC
0874 DTAC
0875 DTAC
0876 DTAC
088 AIS, DTAC, my by CAT
089 AIS, DTAC

	09

090 AIS, DTAC, TrueMove H
091 AIS, DTAC, TrueMove H, TOT
092 AIS, DTAC
093 AIS, TrueMove H
094 DTAC, TrueMove H
095 AIS, DTAC, TrueMove H
096 TrueMove H
097 AIS , TrueMove H
098 AIS
099 AIS , DTAC , TrueMove H
