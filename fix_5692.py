import re

with open('docs/gazettes/5692.md', 'r') as f:
    text = f.read()

# 1. Fix line 303-306
text = text.replace(
    "Please note: That device images are used as an indication only and actual devices may differ. SCHEDULE 2\n\nFix e d mo bile c o nv e rg e nc e pa c ka g e s",
    "Fixed mobile convergence packages\n\nPlease note: That device images are used as an indication only and actual devices may differ."
)

# 2. Fix line 309
text = text.replace(
    "| Convergence Level | Description Please note: That device images are used as an indication only and actual devices may |",
    "| Convergence Level | Description |"
)

# 3. Fix lines 318-327
text = text.replace(
    "| Devices | Included: 6x SIM cards, 3 x Mobile phones, 3 x 4G Dongles, 3 x Fixed cordless phones, l x Fixed Broadband CPE (with Wi-Fi) |\n| Payment | POS (TN teleshops &Nampost)/EFT |\n\n.\n\n| Balance Enquiry | Balance Enquiry via: SMS/USSD/IVR/Call-in/Email |\n|----------------------------------------------|-----------------------------------------------------------------------------------------------------------|\n| VAS | 3 x 500MB Email Addresses, 3 x FAX-to-Email, 1 x Email-to-Fax (on customer request) |\n| Option | 20% Off on SITE Product |\n| Customization Option (Per additional user) | • User 1: for every extra user; 2 x SIM cards, 1000 Voice Minutes, 200 SMS &1GB mobile data) • No devices |",
    "| Devices | Included: 6x SIM cards, 3 x Mobile phones, 3 x 4G Dongles, 3 x Fixed cordless phones, l x Fixed Broadband CPE (with Wi-Fi) |\n| Payment | POS (TN teleshops &Nampost)/EFT |\n| Balance Enquiry | Balance Enquiry via: SMS/USSD/IVR/Call-in/Email |\n| VAS | 3 x 500MB Email Addresses, 3 x FAX-to-Email, 1 x Email-to-Fax (on customer request) |\n| Option | 20% Off on SITE Product |\n| Customization Option (Per additional user) | • User 1: for every extra user; 2 x SIM cards, 1000 Voice Minutes, 200 SMS &1GB mobile data) • No devices |"
)

# 4. Fix lines 391-396
text = text.replace(
    "| Rate | Mobile Data - N$65c/MB, Unlimited Fixed Data |\n\ntn Mobile SiM card\n\n| Devices | Included: l x tn Mobile SIM starter pack (Free) |\n|------------------|------------------------------------------------------------------------------------|",
    "| Rate | Mobile Data - N$65c/MB, Unlimited Fixed Data |\n| Devices | Included: l x tn Mobile SIM starter pack (Free) |"
)

# 5. Fix lines 463-475 (Package 5 Usage Charges missing, image texts)
text = text.replace(
    "| Payment | POS (TN teleshops &Nampost)/EFT |\n\n## Usage Charges\n\ntn Mobile SIMcard\n\ntn Mobile SiMcard\n\n| Balance Enquiry | Balance Enquiry via: SMS/USSD/IVR/Call-in/Email |\n|-------------------|------------------------------------------------------------------|\n| VAS | Follow Me (After no answer on Fixed Forward to tn Mobile) (Free) |\n\n## Subscription Charges\n\nNRC: N$ 299 (Standard)\n\nNRC: Free (Promotion)\n\n## MRC: N$ 485",
    "| Payment | POS (TN teleshops &Nampost)/EFT |\n| Balance Enquiry | Balance Enquiry via: SMS/USSD/IVR/Call-in/Email |\n| VAS | Follow Me (After no answer on Fixed Forward to tn Mobile) (Free) |\n\n## Subscription Charges\n\nNRC: N$ 299 (Standard)\n\nNRC: Free (Promotion)\n\nMRC: N$ 485\n\n## Usage Charges\n\nVoice: 65c/Min - All national calls\n\nData: 65c/MB\n\nSMS: 35c/SMS\n\nCUG call: FREE"
)

# 6. Fix lines 513-517
text = text.replace(
    "## Usage Charges\n\n| Voice: 65c/Min Data: 65c/MB SMS: 35c/SMS CUG call: FREE |\n|-----------------------------------------------------------|",
    "## Usage Charges\n\nVoice: 65c/Min\n\nData: 65c/MB\n\nSMS: 35c/SMS\n\nCUG call: FREE"
)

# 7. Fix lines 526-555 and 582-592
# Wait, let's just do a regex or string replace for the middle part
text = text.replace(
    "| Rate | Mobile Data - N$65c/MB |\n\ntnMobille SIMcard\n\ntn:Mobile SiMcard\n\n## Usage Charges\n\nVoice: 65c/Min - All national calls\n\nData: 65c/MB\n\nSMS: 35c/SMS\n\nCUG call: FREE\n\n| Devices | Included - 1 x tn Mobile SIM starter pack (Free) |\n|---------------------|----------------------------------------------------------------------------------------------|\n| Payment/Recharge | POS (TN teleshops, Retail Shops, NamPost) /EFT |\n| Balance Enquiry | Balance Enquiry via: SMS/USSD/Call-in/Email |\n| VAS | 1 x 500MB Email Address, 1 x FAX-to-Email Addresses, 1 x Email-to- Fax (on customer request) |\n| CPEs Recommendation | For FBB: Fritzbox 7390 or equivalent or better CPE |\n\n## Subscription Charges\n\nNRC: N$ 299 (Standard)\n\nNRC: Free (Promotion)\n\nMRC: N$ 522",
    "| Rate | Mobile Data - N$65c/MB |\n| Devices | Included - 1 x tn Mobile SIM starter pack (Free) |\n| Payment/Recharge | POS (TN teleshops, Retail Shops, NamPost) /EFT |\n| Balance Enquiry | Balance Enquiry via: SMS/USSD/Call-in/Email |\n| VAS | 1 x 500MB Email Address, 1 x FAX-to-Email Addresses, 1 x Email-to- Fax (on customer request) |\n| CPEs Recommendation | For FBB: Fritzbox 7390 or equivalent or better CPE |\n\n## Subscription Charges\n\nNRC: N$ 299 (Standard)\n\nNRC: Free (Promotion)\n\nMRC: N$ 522\n\n## Usage Charges\n\nMobile Data: 65c/MB\n\nFixedData: Unlimited"
)

text = text.replace(
    "Note: The above monthly subscription and once-off fee applies on 1 subscriber only per package.\n\nNote: The above monthly subscription and once-off fee applies on 1 subscriber only per package.\n\nNote: The above monthly subscription and once-off fee applies on 1 subscriber only per package.\n\n## Usage Charges\n\nMobile Data: 65c/MB\n\nFixedData: Unlimited Note: The above monthly subscription and once-off fee applies on 1 subscriber only per package.",
    "Note: The above monthly subscription and once-off fee applies on 1 subscriber only per package."
)

# 8. Fix lines 567-570
text = text.replace(
    "| Call rate within group Revised TN1 MaxiPro Packages Revised TN1 MaxiPro Packages Revised TN1 MaxiPro Packages | 0.25 | 0.25 | 0.25 |\n| Call rate outside group | 0.80 | 0.80 | 0.80 |\n| SMS rate within group Device images are used as an indication Device images are used as an indication Device images are used as an indication | 0.25 only and might vary. only and might only and might | 0.25 Additional phones vary. Additional phones vary. Additional phones | 0.25 were identified were identified were identified |\n| SMS rate outside group (between 5-8 phones). package (between 5-8 phones). package (between 5-8 phones). | 0.35 | 0.35 | 0.35 |",
    "| Call rate within group | 0.25 | 0.25 | 0.25 |\n| Call rate outside group | 0.80 | 0.80 | 0.80 |\n| SMS rate within group | 0.25 | 0.25 | 0.25 |\n| SMS rate outside group | 0.35 | 0.35 | 0.35 |"
)

with open('docs/gazettes/5692.md', 'w') as f:
    f.write(text)

