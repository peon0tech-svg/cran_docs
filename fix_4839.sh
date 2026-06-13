#!/bin/bash
FILE="/opt/cran_clean_mds/docs/gazettes/4839.md"

sed -i 's/CEPT\/EAC\/REC/CEPT\/ERC\/REC/g' "$FILE"
sed -i 's/CEPT\/EAC\/DEC/CEPT\/ERC\/DEC/g' "$FILE"
sed -i 's/Licenc Exemptlons/Licence Exemptions/g' "$FILE"
sed -i 's/N 300 330 EN 301 489-1,3 EN 60950/EN 300 330 EN 301 489-1,3 EN 60950/g' "$FILE"
sed -i 's/Inductive Loop System X/Inductive Loop System/g' "$FILE"
sed -i 's/GRID - telecornrnand only./SRD - telecommand only./g' "$FILE"
sed -i 's/1 SRDW erp./1 mW erp./g' "$FILE"
sed -i 's/ISO\/1EC/ISO\/IEC/g' "$FILE"
sed -i 's/500mnW./500mW./g' "$FILE"
sed -i 's/463.975M; 484.125M; 464.175M; 464.325M;/463.975M; 464.125M; 464.175M; 464.325M; 464.375M;/g' "$FILE"
sed -i 's/888.7- 869.2M/868.7- 869.2M/g' "$FILE"
sed -i 's/FODA./FDDA./g' "$FILE"
sed -i 's/EN 609W/EN 60950/g' "$FILE"
sed -i 's/50 MWerp/50 mWerp/g' "$FILE"

sed -i 's/100%duty cycle No channel |/100%duty cycle No channel spacing. |/g' "$FILE"

sed -i 's/| 54.4500; 54.4625; 54.4750; 54.4875; 54.500; 54.5125; 54.5250; 54.5375; |/| 54.4500; 54.4625; 54.4750; 54.4875; 54.500; 54.5125; 54.5250; 54.5375; 54.5500M |/g' "$FILE"

sed -i 's/| 446 - 446.1 M includes the following eight channels. 446.00625M; 446.01875M; 446.03125M; 446.04375M; 446.05625M; 446.06875M; 446.08125M; |/| 446 - 446.1 M includes the following eight channels. 446.00625M; 446.01875M; 446.03125M; 446.04375M; 446.05625M; 446.06875M; 446.08125M; 446.09375M; |/g' "$FILE"

sed -i 's/Chamber Trading Four 1/Chamber Trading Four1/g' "$FILE"
sed -i 's/Municipality of Tsumeb 2/Municipality of Tsumeb2/g' "$FILE"
sed -i 's/Southern Sun Media for Christ 3/Southern Sun Media for Christ3/g' "$FILE"
sed -i 's/Windhoek Paris FM 4/Windhoek Paris FM4/g' "$FILE"
sed -i 's/WUM Properties Ltd 5/WUM Properties Ltd5/g' "$FILE"

